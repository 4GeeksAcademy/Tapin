/* eslint-disable unicorn/prefer-module, unicorn/no-process-exit, n/no-process-exit, unicorn/prefer-top-level-await */
// CLI: generate PNG fallbacks from brand SVGs
// Uses: sharp + svgo

const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');
const { optimize } = require('svgo');

const brandDir = path.resolve(__dirname, '..', 'brand');
const svgPath = path.join(brandDir, 'logo.svg');

if (!fs.existsSync(svgPath)) {
  console.error('logo.svg not found in', brandDir);
  process.exit(2);
}

function optimizeSvgSync(inputPath) {
  const svg = fs.readFileSync(inputPath, 'utf8');
  const result = optimize(svg, { multipass: true, path: inputPath });
  return result.data;
}

async function writePngs() {
  console.log('Optimizing SVG...');
  const optSvg = optimizeSvgSync(svgPath);

  const outputs = [
    { name: 'logo@1x.png', height: 72 },
    { name: 'logo@2x.png', height: 144 },
    { name: 'logo@3x.png', height: 216 },
    { name: 'favicon.png', size: 32 },
  ];

  for (const out of outputs) {
    const outPath = path.join(brandDir, out.name);
    console.log('Generating', out.name);
    let pipeline = sharp(Buffer.from(optSvg));
    if (out.size > 0) {
      pipeline = pipeline.resize(out.size, out.size, { fit: 'contain' });
    } else if (out.height) {
      pipeline = pipeline.resize({ height: out.height });
    }
    await pipeline.png({ quality: 90 }).toFile(outPath);
    console.log('Wrote', outPath);
  }
}

writePngs()
  .then(() => console.log('PNG generation complete'))
  .catch((error) => {
    console.error('Error generating PNGs:', error);
    process.exit(1);
  });
