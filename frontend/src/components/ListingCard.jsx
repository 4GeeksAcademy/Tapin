import React from 'react';

export default function ListingCard({ listing, onSelect }) {
  return (
    <article
      className="card"
      role="button"
      tabIndex={0}
      onClick={() => onSelect && onSelect(listing)}
      onKeyDown={(e) => {
        if (e.key === 'Enter') onSelect && onSelect(listing);
      }}
    >
      <div className="card-main">
        <div className="card-title">
          <h3>{listing.title}</h3>
          {listing.location && <small className="location">{listing.location}</small>}
        </div>
        {listing.description && <p className="card-desc">{listing.description}</p>}
      </div>
      <div className="card-meta">
        <button
          className="cta"
          onClick={(e) => {
            e.stopPropagation(); /* protect click */
          }}
        >
          Sign Up
        </button>
      </div>
    </article>
  );
}
