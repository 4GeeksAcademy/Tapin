import React from 'react';

const chips = ['All', 'Events', 'Volunteering', 'Remote', 'Community'];

export default function Filters({ active, onChange }) {
  return (
    <div className="filters">
      <div className="chips">
        {chips.map((c) => (
          <button
            key={c}
            className={`chip ${active === c ? 'active' : ''}`}
            onClick={() => onChange && onChange(c)}
          >
            {c}
          </button>
        ))}
      </div>
      <div className="view-toggle">
        <button className="chip">List</button>
        <button className="chip">Map</button>
      </div>
    </div>
  );
}
