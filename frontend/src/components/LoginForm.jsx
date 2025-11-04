import React, { useState } from 'react';
import { API_BASE } from '../config';

export default function LoginForm({ onLogin, mode = 'login' }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  async function submit(e) {
    e.preventDefault();
    setError(null);
    try {
      const url = mode === 'login' ? `${API_BASE}/login` : `${API_BASE}/register`;
      const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'auth failed');
      onLogin && onLogin(data);
    } catch (e) {
      setError(e.message);
    }
  }

  return (
    <form onSubmit={submit} className="auth-form">
      <input
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
        type="email"
        required
      />
      <input
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        type="password"
        required
      />
      <button type="submit" className="chip">
        {mode === 'login' ? 'Login' : 'Register'}
      </button>
      {error && <div className="error">{error}</div>}
    </form>
  );
}
