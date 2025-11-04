#!/usr/bin/env node
const { spawn, spawnSync } = require('node:child_process');
const { existsSync, readFileSync } = require('node:fs');
const { join } = require('node:path');

function parseDotEnv(path) {
  const env = {};
  try {
    if (!existsSync(path)) return env;
    const content = readFileSync(path, 'utf8');
    for (const line of content.split(/\r?\n/)) {
      const m = line.match(/^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)\s*$/);
      if (!m) continue;
      const key = m[1];
      let val = m[2];
      if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      env[key] = val;
    }
  } catch {}
  return env;
}

function prefixLines(prefix, data) {
  return data
    .toString()
    .split(/\r?\n/)
    .filter(Boolean)
    .map((l) => `[${prefix}] ${l}`)
    .join('\n') + '\n';
}

function safeEnv(obj) {
  const out = {};
  for (const [k, v] of Object.entries(obj || {})) {
    if (v === undefined || v === null) continue;
    out[k] = typeof v === 'string' ? v : String(v);
  }
  return out;
}

function spawnLogged(name, cmd, args, options) {
  const opts = { stdio: ['ignore', 'pipe', 'pipe'], ...options };
  if (opts.env) opts.env = safeEnv(opts.env);
  console.log(`[orchestrator] spawn ${name}: ${cmd} ${args.join(' ')} (cwd=${opts.cwd})`);
  const child = spawn(cmd, args, opts);
  child.stdout.on('data', (d) => process.stdout.write(prefixLines(name, d)));
  child.stderr.on('data', (d) => process.stderr.write(prefixLines(name, d)));
  child.on('error', (err) => {
    if (err && err.code === 'ENOENT') {
      console.error(`[${name}] Failed to start: command not found: ${cmd}`);
    } else {
      console.error(`[${name}] Failed to start:`, err);
    }
  });
  child.on('close', (code) => {
    console.log(`[${name}] exited with code ${code}`);
  });
  return child;
}

async function main() {
  const root = process.cwd();
  // dev.js is intended to run from the Tapin/ folder (package.json location)
  const backendDir = join(root, 'backend');
  const frontendDir = join(root, 'frontend');

  // Load .env for backend to determine HOST/PORT (non-fatal if missing)
  const backendEnv = parseDotEnv(join(backendDir, '.env'));
  const HOST = process.env.BACKEND_HOST || backendEnv.HOST || '127.0.0.1';
  const PORT = String(process.env.BACKEND_PORT || backendEnv.PORT || 5000);

  const FRONTEND_PORT = String(process.env.FRONTEND_PORT || 5173);
  const FRONTEND_HOST = process.env.FRONTEND_HOST || '127.0.0.1';

  console.log('Starting Tapin dev environment...');
  console.log('- Backend:  http://' + HOST + ':' + PORT);
  console.log('- Frontend: http://' + FRONTEND_HOST + ':' + FRONTEND_PORT);
  console.log('(Ctrl+C to stop)\n');

  const children = [];

  // Choose python executable
  function pickPython() {
    if (process.env.PYTHON) return process.env.PYTHON;
    const candidates = process.platform === 'win32' ? ['py', 'python', 'python3'] : ['python3', 'python'];
    for (const c of candidates) {
      const res = spawnSync(c, ['--version'], { stdio: 'ignore' });
      if (!res.error) return c;
    }
    return null;
  }
  const pythonCmd = pickPython();
  if (!pythonCmd) {
    console.error('[orchestrator] Could not find a Python executable. Install Python or set PYTHON env var to full path (e.g. C\\\Python311\\python.exe).');
    process.exit(1);
  }

  // Ensure backend dependencies (Flask, etc.)
  try {
    const chk = spawnSync(pythonCmd, ['-c', 'import flask'], { cwd: backendDir });
    if (chk.status !== 0) {
      console.log('[orchestrator] Installing backend dependencies via pip...');
      const inst = spawnSync(pythonCmd, ['-m', 'pip', 'install', '-r', 'requirements.txt'], {
        cwd: backendDir,
        stdio: 'inherit',
        shell: process.platform === 'win32',
      });
      if (inst.status !== 0) {
        console.error('[orchestrator] Failed to install backend dependencies. Please run:');
        console.error(`  ${pythonCmd} -m pip install -r Tapin/backend/requirements.txt`);
        process.exit(1);
      }
    }
  } catch (e) {
    console.error('[orchestrator] Backend dependency check failed:', e.message);
  }

  // Start backend (Flask)
  children.push(
    spawnLogged('backend', pythonCmd, [join(backendDir, 'app.py')], {
      cwd: backendDir,
      env: { ...process.env, HOST, PORT },
      shell: false,
    })
  );

  // Start frontend (Vite)
  // Use npm to run vite with explicit host/port
  const npmCmd = process.platform === 'win32' ? 'npm.cmd' : 'npm';
  // Ensure frontend dependencies (vite, react, etc.)
  try {
    const viteBin = process.platform === 'win32' ? join(frontendDir, 'node_modules', '.bin', 'vite.cmd') : join(frontendDir, 'node_modules', '.bin', 'vite');
    if (!existsSync(viteBin)) {
      console.log('[orchestrator] Installing frontend dependencies via npm install...');
      const inst = spawnSync(npmCmd, ['install'], {
        cwd: frontendDir,
        stdio: 'inherit',
        shell: process.platform === 'win32',
      });
      if (inst.status !== 0) {
        console.error('[orchestrator] Failed to install frontend dependencies. Please run:');
        console.error('  cd Tapin/frontend && npm install');
        process.exit(1);
      }
    }
  } catch (e) {
    console.error('[orchestrator] Frontend dependency check failed:', e.message);
  }
  children.push(
    spawnLogged(
      'frontend',
      npmCmd,
      ['run', 'dev', '--', '--host', FRONTEND_HOST, '--port', FRONTEND_PORT],
      {
        cwd: frontendDir,
        env: { ...process.env },
        shell: process.platform === 'win32',
      }
    )
  );

  // Graceful shutdown
  const shutdown = () => {
    console.log('\nShutting down...');
    for (const c of children) {
      try {
        if (process.platform === 'win32') {
          spawn('taskkill', ['/pid', String(c.pid), '/T', '/F']);
        } else {
          c.kill('SIGINT');
        }
      } catch {}
    }
    setTimeout(() => process.exit(0), 300);
  };

  process.on('SIGINT', shutdown);
  process.on('SIGTERM', shutdown);
}

main().catch((e) => {
  console.error('Dev orchestrator failed:', e);
  process.exit(1);
});
