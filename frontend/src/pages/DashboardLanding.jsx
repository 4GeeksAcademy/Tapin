import React from 'react';
import logoTransparent from '../../../Design-Assets/brand/logo-transparent.svg';

export default function DashboardLanding({ onEnter }) {
  return (
    <div className="landing-root">
      <div className="landing-hero">
        <img src={logoTransparent} alt="Tapin logo" className="landing-logo" />
        <h1 className="landing-title">Tapin — discover local talent, fast.</h1>
        <p className="landing-sub">
          A lightweight mobile-first marketplace to find and book local makers, tutors and
          professionals — simple, fast, and privacy-friendly.
        </p>

        <div className="landing-cta-row">
          <button className="btn btn-primary landing-cta" onClick={onEnter}>
            Get started — it's free
          </button>
          <button className="btn btn-outline landing-cta" onClick={onEnter}>
            Log in
          </button>
        </div>

        <ul className="landing-features">
          <li>Fast mobile UX optimized for local discovery</li>
          <li>Private by design — prototype with no tracking</li>
          <li>List a service in under 60 seconds</li>
        </ul>

        <div className="landing-footer-note">No credit card required • Prototype</div>
      </div>
    </div>
  );
}
