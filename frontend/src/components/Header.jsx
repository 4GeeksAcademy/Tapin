import React from 'react';
import logo from '../../../Design-Assets/Tapin-Logo.png';

export default function Header() {
  return (
    <header className="app-header">
      <div className="brand">
        <img src={logo} alt="Tapin logo" className="logo" />
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
