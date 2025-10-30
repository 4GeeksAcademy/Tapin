import React from 'react';

export default function ListingDetail({ listing, onClose }) {
  if (!listing) return null;
  return (
    <div className="detail-overlay" role="dialog" aria-modal="true">
      <div className="detail-card">
        <header className="detail-header">
          <h2>{listing.title}</h2>
          <button className="close" onClick={onClose} aria-label="Close">
            ×
          </button>
        </header>
        <div className="detail-body">
          {listing.location && (
            <p>
              <strong>Location:</strong> {listing.location}
            </p>
          )}
          {listing.description && <p>{listing.description}</p>}
          <p>
            <small>Created: {new Date(listing.created_at || Date.now()).toLocaleString()}</small>
          </p>
        </div>
        <footer className="detail-footer">
          <button className="cta">Sign Up</button>
        </footer>
      </div>
    </div>
  );
}
