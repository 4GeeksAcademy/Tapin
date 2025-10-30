import React, { useEffect, useState } from 'react';
import Header from './components/Header';
import ListingCard from './components/ListingCard';
import EmptyState from './components/EmptyState';
import ListingDetail from './components/ListingDetail';
import Filters from './components/Filters';
import LoginForm from './components/LoginForm';
import CreateListingForm from './components/CreateListingForm';

export default function App() {
  const [listings, setListings] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selected, setSelected] = useState(null);
  const [activeFilter, setActiveFilter] = useState('All');
  const [token, setToken] = useState(localStorage.getItem('access_token') || null);
  const [user, setUser] = useState(null);

  // Helper: fetch listings optionally filtered by q
  async function fetchListings(filter) {
    setLoading(true);
    setError(null);
    try {
      const params = new URLSearchParams();
      if (filter && filter !== 'All') params.set('q', filter);
      const url = `http://127.0.0.1:5000/listings${params.toString() ? `?${params.toString()}` : ''}`;
      const res = await fetch(url);
      if (!res.ok) throw new Error(`status ${res.status}`);
      const data = await res.json();
      setListings(data);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }

  // Initialize filter from URL and fetch
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const q = params.get('q') || 'All';
    setActiveFilter(q);
    fetchListings(q);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    async function fetchMe() {
      if (!token) return setUser(null);
      try {
        const res = await fetch('http://127.0.0.1:5000/me', {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (!res.ok) {
          setUser(null);
          return;
        }
        const data = await res.json();
        setUser(data.user);
      } catch (_) {
        setUser(null);
      }
    }
    fetchMe();
  }, [token]);

  function handleSelect(item) {
    setSelected(item);
  }

  function handleFilterChange(filter) {
    setActiveFilter(filter);
    const params = new URLSearchParams(window.location.search);
    if (!filter || filter === 'All') params.delete('q');
    else params.set('q', filter);
    const qs = params.toString();
    const newUrl = qs ? `?${qs}` : window.location.pathname;
    window.history.replaceState(null, '', newUrl);
    fetchListings(filter);
  }

  function SkeletonList({ count = 3 }) {
    return (
      <ul className="listings skeleton-list">
        {Array.from({ length: count }).map((_, i) => (
          <li key={i} className="listing-item">
            <div className="skeleton-card">
              <div className="skeleton-title" />
              <div className="skeleton-line" />
              <div className="skeleton-line" style={{ width: '80%' }} />
            </div>
          </li>
        ))}
      </ul>
    );
  }

  return (
    <div className="app-root">
      <Header />

      <div
        style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: 12 }}
      >
        <Filters active={activeFilter} onChange={handleFilterChange} />
        <div>
          {user ? (
            <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
              <span>Hi, {user.email}</span>
              <button
                className="chip"
                onClick={() => {
                  localStorage.removeItem('access_token');
                  setToken(null);
                }}
              >
                Logout
              </button>
            </div>
          ) : (
            <div style={{ display: 'flex', gap: 8 }}>
              <LoginForm
                mode="login"
                onLogin={(d) => {
                  localStorage.setItem('access_token', d.access_token);
                  setToken(d.access_token);
                }}
              />
              <LoginForm
                mode="register"
                onLogin={(d) => {
                  localStorage.setItem('access_token', d.access_token);
                  setToken(d.access_token);
                }}
              />
            </div>
          )}
        </div>
      </div>

      <main>
        {loading && <SkeletonList count={3} />}
        {error && <p className="error">Error: {error}</p>}

        {!loading && !error && (
          <section>
            {listings.length === 0 ? (
              <EmptyState />
            ) : (
              <ul className="listings">
                {listings.map((l) => (
                  <li key={l.id} className="listing-item">
                    <ListingCard listing={l} onSelect={handleSelect} />
                  </li>
                ))}
              </ul>
            )}
          </section>
        )}

        {user && (
          <div style={{ marginTop: 12 }}>
            <h3>Create a listing</h3>
            <CreateListingForm
              token={token}
              onCreated={(data) => {
                setListings((s) => [data, ...s]);
              }}
            />
          </div>
        )}
      </main>

      {selected && <ListingDetail listing={selected} onClose={() => setSelected(null)} />}

      <footer>
        <small>Tapin prototype</small>
      </footer>
    </div>
  );
}
