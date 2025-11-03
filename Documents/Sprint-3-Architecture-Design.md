# Sprint 3 Architecture & Infrastructure Design

**Date:** November 3, 2025  
**Agent:** @architect  
**Sprint:** 3 - Map Integration & Deployment  
**Updated:** November 3, 2025 (Changed to free deployment options)

---

## Executive Summary

This document provides architectural recommendations for Sprint 3, covering map integration and deployment options. All recommendations prioritize **zero cost** for school projects, simplicity, and alignment with the current tech stack (Flask + React/Vite + SQLite dev).

**Key Changes:**

- ✅ Map integration: Leaflet + OpenStreetMap (FREE)
- ✅ Deployment option 1: Render free tier (recommended for live demos)
- ✅ Deployment option 2: Local demo with screen recording (recommended for submissions)
- ❌ Removed: Railway ($15/month) - overkill for school projects

---

## Current System Review

### Tech Stack (Sprints 1 & 2)

**Backend:**

- Flask 2.2+ with SQLAlchemy 3.0
- JWT authentication (Flask-JWT-Extended 4.4)
- SQLite (development)
- pytest for testing

**Frontend:**

- React 18.2 + Vite 5.0
- No router (single page app with modals)
- Vitest + React Testing Library

**Deployment Status:**

- ✅ Development: localhost:5173 (frontend) + localhost:5000 (backend)
- ❌ Production: Not deployed
- ❌ CI/CD: Not configured

### Features Implemented

- User authentication (register, login, password reset)
- Listing CRUD with ownership verification
- Sign-up/volunteer connection system
- Reviews and ratings (1-5 stars)
- Comprehensive test suites (32 backend tests, 10+ frontend tests)

---

## Story 3.1: Map Provider Recommendation

### Requirements Analysis

- Display listings on interactive map
- Click pins to show listing previews
- Toggle between list and map view
- Filter by map bounds (optional geofencing)
- Need geocoding for addresses (future)

### Option Comparison

#### ✅ **RECOMMENDED: Leaflet + OpenStreetMap**

**Pros:**

- 100% free, no API keys or usage limits
- Open source with MIT license
- Lightweight (38kb gzipped)
- Easy React integration (`react-leaflet`)
- Great mobile support
- No vendor lock-in
- Community-driven, stable, mature

**Cons:**

- Need separate geocoding service (Nominatim is free but rate-limited)
- Less polished UI than Google Maps
- Fewer built-in features

**Cost:** $0/month forever

**Integration Complexity:** Low

- Install: `npm install leaflet react-leaflet`
- Component: `<MapContainer>` with `<Marker>` components
- Styling: Include Leaflet CSS
- Time estimate: 4-6 hours

**Example Implementation:**

```jsx
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

<MapContainer center={[51.505, -0.09]} zoom={13}>
  <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
  {listings.map((listing) => (
    <Marker key={listing.id} position={[listing.lat, listing.lng]}>
      <Popup>{listing.title}</Popup>
    </Marker>
  ))}
</MapContainer>;
```

#### ❌ Google Maps

**Pros:**

- Best-in-class UI/UX
- Comprehensive features
- Excellent geocoding

**Cons:**

- Requires billing account (even for free tier)
- $200/month free credit, then $7 per 1000 map loads
- Complex setup and API key management
- Vendor lock-in

**Cost:** $0-$100+/month depending on usage

**Recommendation:** Overkill for MVP, save for later if needed

#### ❌ Mapbox

**Pros:**

- Beautiful styling options
- Good React integration
- Better than Google for customization

**Cons:**

- Requires API key
- 50,000 free loads/month, then $5 per 1000
- More complex than Leaflet

**Cost:** $0-$50+/month

**Recommendation:** Good middle ground, but Leaflet is simpler for MVP

### 🎯 Final Recommendation: **Leaflet + OpenStreetMap**

**Rationale:**

1. **Zero cost** - Critical for early-stage MVP
2. **Simple integration** - Well-documented React library
3. **No API key hassles** - No registration, rate limits, billing setup
4. **Sufficient features** - Covers all Story 3.1 requirements
5. **Future-proof** - Can migrate to paid solution later if needed

**Geocoding Strategy:**

- **Now:** Users manually enter lat/lng or use location field text search
- **Later:** Integrate Nominatim (free, rate-limited) or paid service (Google Geocoding, Mapbox)

---

## Story 3.2: Production Infrastructure Design

### Hosting Platform Evaluation

#### ✅ **RECOMMENDED: Railway**

**Why Railway:**

- **Simplicity:** Deploy from GitHub in 5 minutes
- **Pricing:** $5/month per service (predictable)
- **PostgreSQL:** Built-in managed database ($5/month)
- **Environment management:** Easy staging/production splits
- **Zero config:** Detects Flask/Node.js automatically
- **SSL/HTTPS:** Automatic
- **Monitoring:** Built-in logs and metrics
- **Developer experience:** Excellent CLI and dashboard

**Cost Estimate:**

- Backend service: $5/month
- Frontend service: $5/month
- PostgreSQL database: $5/month
- **Total: $15/month**

**Pros:**

- No credit card required for trial
- Free $5 credit for new users
- Simple pricing, no surprises
- Great for Python + React
- Built-in CI/CD

**Cons:**

- Newer platform (less mature than Heroku)
- Smaller community
- Limited free tier (500 hours/month)

## Story 3.2: Deployment Strategy (FREE Options)

### Requirements

- ✅ Zero or minimal cost (school project budget)
- ✅ Easy deployment and updates
- ✅ Support for Flask backend + React frontend
- ✅ PostgreSQL or SQLite database
- ✅ HTTPS/SSL (for security)
- ✅ Suitable for demos and portfolio

---

### 🆓 Option 1: Render (FREE Tier) - **RECOMMENDED FOR LIVE DEMOS**

#### Overview

Render provides a generous free tier perfect for school projects and portfolios.

**Pros:**

- 100% free (no credit card required)
- Auto-deploy from GitHub (push to deploy)
- Free PostgreSQL database (90 days, renewable)
- Free SSL certificates (HTTPS automatic)
- Static site hosting (frontend)
- Web service hosting (backend)

**Cons:**

- Services spin down after 15 min inactivity (30-60s cold start)
- PostgreSQL expires after 90 days (must renew)
- 750 hours/month execution time limit
- Slower than paid services

**Cost:** $0/month

**Setup Time:** ~20 minutes

**Best For:**

- Live demos with shareable URL
- Portfolio projects
- School project presentations
- Testing deployment workflows

#### Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Render Platform (FREE)              │
│                                                      │
│  ┌────────────────┐         ┌──────────────────┐   │
│  │ Static Site    │         │ Web Service      │   │
│  │ (React/Vite)   │◄───────►│ (Flask/Python)   │   │
│  │ Frontend       │         │ Backend          │   │
│  └────────────────┘         └──────────────────┘   │
│                                      │              │
│                                      ▼              │
│                             ┌──────────────────┐   │
│                             │ PostgreSQL       │   │
│                             │ (Free 90 days)   │   │
│                             └──────────────────┘   │
└─────────────────────────────────────────────────────┘
           │
           ▼
    ┌─────────────┐
    │   GitHub    │
    │ Auto-deploy │
    └─────────────┘
```

**Deployment Guide:** See `/Documents/Story-3.2-Render-Deployment.md`

---

### 🖥️ Option 2: Local Demo + Screen Recording - **RECOMMENDED FOR SUBMISSIONS**

#### Overview

Run the application locally and create a professional screen recording for submission.

**Pros:**

- Zero cost (completely free)
- Full control (no cold starts or downtime)
- Easy debugging (see all logs)
- Instant setup (2 minutes)
- Perfect quality (no network issues)
- No deployment complexity

**Cons:**

- Not publicly accessible
- Requires video editing skills
- Need to run servers for live demos

**Cost:** $0

**Setup Time:** 2 minutes (after dependencies installed)

**Best For:**

- Video submissions
- Assignment demonstrations
- Quick testing
- Development workflow
- Offline presentations

#### Setup

```bash
# Terminal 1: Backend
cd backend
source .venv/bin/activate
python app.py

# Terminal 2: Frontend
cd frontend
npm run dev

# Open browser: http://localhost:5173
```

**Demo Guide:** See `/Documents/Local-Demo-Guide.md`

---

### 📊 Deployment Options Comparison

| Feature            | Render (Free)    | Local Demo  | Railway ❌       |
| ------------------ | ---------------- | ----------- | ---------------- |
| **Cost**           | $0/month         | $0          | $15/month        |
| **Setup Time**     | 20 min           | 2 min       | 15 min           |
| **Public URL**     | ✅ Yes           | ❌ No       | ✅ Yes           |
| **SSL/HTTPS**      | ✅ Auto          | N/A         | ✅ Auto          |
| **Database**       | PostgreSQL (90d) | SQLite      | PostgreSQL       |
| **Cold Starts**    | 30-60s           | None        | None             |
| **Auto-Deploy**    | ✅ GitHub        | N/A         | ✅ GitHub        |
| **Best For**       | Live demos       | Submissions | Production       |
| **Recommendation** | ⭐ Yes           | ⭐⭐ Yes    | ❌ Too expensive |

---

### 🎯 Final Recommendation

**For School Projects:**

1. **Primary:** Local demo + screen recording
   - Zero cost
   - Perfect quality
   - Easy to set up
   - Submit video to instructor

2. **Secondary:** Render free tier
   - If you need a live URL
   - For portfolio/resume
   - For peer testing
   - Keep in mind: cold starts

**Avoid for school:**

- Railway ($15/month) - unnecessary expense
- Heroku ($23/month) - too expensive
- AWS/GCP - too complex for MVP

---

### Alternative: Fly.io (If You Want to Explore Later)

**Note:** User mentioned Fly.io as potential alternative to Railway.

**Pros:**

- More generous free tier than Render
- Better performance
- Global edge network

**Cons:**

- Credit card required (even for free tier)
- More complex setup
- Less beginner-friendly

**Cost:** $0-$5/month

**Recommendation:** Good option if Render doesn't meet needs, but adds complexity.

---

## Implementation Summary

### Story 3.1: Map Integration ✅ COMPLETE

**Implemented:**

- Leaflet 1.9.4 + react-leaflet 4.2.1
- OpenStreetMap tile layer (zero cost)
- Interactive markers with popups
- List/Map view toggle
- Optional coordinate input in forms
- Auto-fit bounds to show all markers

**Test Results:** 100% passing - See Story-3.1-Map-Testing.md

---

### Story 3.2: Deployment Strategy ✅ COMPLETE

**Options Documented:**

1. **Render Free Tier** - Live demo deployment (FREE)
2. **Local Demo + Recording** - Video submission (FREE)

**Guides Created:**

- Story-3.2-Render-Deployment.md (350+ lines)
- Local-Demo-Guide.md (450+ lines)

---

## Conclusion

Sprint 3 architecture successfully delivers:

✅ **Zero-cost map integration** using Leaflet + OpenStreetMap  
✅ **Free deployment options** suitable for school projects  
✅ **Comprehensive documentation** for both deployment paths  
✅ **Production-ready architecture** (can upgrade to paid services later)

**Estimated Costs:**

- Development: $0
- Deployment (Option 1): $0 with Render free tier
- Deployment (Option 2): $0 with local demo
- **Total: $0** 🎉

**Time Investment:**

- Map integration: 4-6 hours
- Deployment setup: 20-30 minutes
- Total Sprint 3: ~1 day

---

**Last Updated:** November 3, 2025  
**Status:** ✅ Complete  
**Next Steps:** Choose deployment option and deploy!
