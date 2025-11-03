import React, { useState, useEffect } from 'react';

export default function ListingCard({ listing = {}, onOpen }) {
  const { title, description, image, location, id } = listing;
  const [averageRating, setAverageRating] = useState(null);
  const [reviewCount, setReviewCount] = useState(0);

  useEffect(() => {
    if (!id) return;

    async function fetchRating() {
      try {
        const [ratingRes, reviewsRes] = await Promise.all([
          fetch(`http://127.0.0.1:5000/listings/${id}/average-rating`),
          fetch(`http://127.0.0.1:5000/listings/${id}/reviews`),
        ]);

        if (ratingRes.ok) {
          const ratingData = await ratingRes.json();
          setAverageRating(ratingData.average_rating);
        }

        if (reviewsRes.ok) {
          const reviewsData = await reviewsRes.json();
          setReviewCount(reviewsData.reviews?.length || 0);
        }
      } catch (err) {
        console.error('Error fetching rating:', err);
      }
    }

    fetchRating();
  }, [id]);

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

        {averageRating !== null && (
          <div style={{ display: 'flex', alignItems: 'center', gap: '4px', marginBottom: '8px' }}>
            <span style={{ color: '#ffc107', fontSize: '16px' }}>★</span>
            <span style={{ fontWeight: 'bold', fontSize: '14px' }}>{averageRating.toFixed(1)}</span>
            <span style={{ color: '#666', fontSize: '12px' }}>({reviewCount})</span>
          </div>
        )}

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
