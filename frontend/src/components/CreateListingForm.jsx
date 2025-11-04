import React, { useState } from 'react';
import { API_BASE } from '../config';

export default function CreateListingForm({ token, onCreated }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [location, setLocation] = useState('');
  const [error, setError] = useState(null);

  async function submit(e) {
    e.preventDefault();
    setError(null);
    try {
      const res = await fetch(`${API_BASE}/listings`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ title, description, location }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'create failed');
      setTitle('');
      setDescription('');
      setLocation('');
      onCreated && onCreated(data);
    } catch (e) {
      setError(e.message);
    }
  }

  return (
    <form onSubmit={submit} className="create-form">
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Title"
        required
      />
      <input
        value={location}
        onChange={(e) => setLocation(e.target.value)}
        placeholder="Location"
      />
      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Description"
      />
      <div style={{ display: 'flex', gap: 8 }}>
        <button type="submit" className="cta">
          Create Listing
        </button>
      </div>
      {error && <div className="error">{error}</div>}
    </form>
  );
}
