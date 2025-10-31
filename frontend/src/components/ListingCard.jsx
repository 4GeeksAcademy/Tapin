import React from 'react';

export default function ListingCard({ listing = {}, onOpen }) {
  const { title, description, image, location } = listing;

  return (
    <li className="listing-item">
      <article className="card" role="article" aria-label={title || 'Listing'}>
        <div className="card-media" aria-hidden={image ? 'false' : 'true'}>
          {image ? (
            <img src={image} alt={title || 'Listing image'} loading="lazy" />
          ) : (
            <div className="placeholder" aria-hidden="true">
              📷
            </div>
          )}
          {location && <div className="media-caption">{location}</div>}
        </div>

        <h3 className="card-title">{title || 'Untitled listing'}</h3>
        <p className="card-desc">{description || 'No description provided.'}</p>

        <div className="card-meta">
          <span className="muted" aria-hidden="true">
            {location || ''}
          </span>
          <button className="btn-primary" onClick={() => onOpen && onOpen(listing)}>
            View
          </button>
        </div>
      </article>
    </li>
  );
}
