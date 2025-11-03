import React from 'react';

export default function Header() {
  return (
    <header className="app-header">
      <div className="brand">
        <div>
          <h1>Tapin</h1>
          <p className="subtitle">Listings prototype</p>
        </div>
      </div>

      <div className="search-row">
        <input className="search" placeholder="Search listings, location or organization" />
      </div>
    </header>
  );
}
