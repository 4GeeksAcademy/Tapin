# Local Demo Guide - Tapin

**Perfect for quick demos, testing, and screen recordings**

---

## 🎯 About Tapin

**Tapin** is a dual-purpose community connection platform:

- **🤝 Volunteer Opportunities** (Primary): Find and sign up for community service
- **💼 Local Services** (Secondary): Discover local businesses and professionals

---

## 🎯 Why Demo Locally?

- ✅ **Zero cost** - No deployment needed
- ✅ **Instant setup** - 2 minutes to run
- ✅ **Full control** - No cold starts or downtime
- ✅ **Easy debugging** - See all logs in real-time
- ✅ **Perfect for submissions** - Screen record and submit video

---

## 📋 Prerequisites

- Python 3.9+ installed
- Node.js 18+ installed
- Git repository cloned
- 5 minutes of time

---

## Part 1: Setup (One-Time)

### Step 1.1: Backend Setup

```bash
# Navigate to backend directory
cd /Users/houseofobi/Documents/GitHub/Tapin/backend

# Create virtual environment (if not exists)
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Initialize database
python -c "from app import app, db; app.app_context().push(); db.create_all(); print('✅ Database initialized')"
```

### Step 1.2: Frontend Setup

```bash
# Open new terminal tab
cd /Users/houseofobi/Documents/GitHub/Tapin/frontend

# Install dependencies
npm install

# Verify leaflet packages installed
npm list leaflet react-leaflet
```

---

## Part 2: Running the Application

### Step 2.1: Start Backend Server

```bash
# Terminal 1: Backend
cd backend
source .venv/bin/activate
python app.py
```

**Expected output:**

```
 * Running on http://127.0.0.1:5000
 * Restarting with stat
 * Debugger is active!
```

✅ Backend running at: `http://127.0.0.1:5000`

### Step 2.2: Start Frontend Server

```bash
# Terminal 2: Frontend (new tab)
cd frontend
npm run dev
```

**Expected output:**

```
VITE v5.4.21  ready in 238 ms

➜  Local:   http://localhost:5173/
```

✅ Frontend running at: `http://localhost:5173`

### Step 2.3: Open Application

Open browser and navigate to: **http://localhost:5173**

---

## Part 3: Demo Script

### Complete Feature Walkthrough (5 minutes)

#### 1. **User Registration** (30 seconds)

- Click "Register" button
- Fill in:
  - Username: `demo_user`
  - Email: `demo@example.com`
  - Password: `Demo123!@#`
- Click "Register"
- ✅ Success message appears

#### 2. **Login** (15 seconds)

- Enter credentials
- Click "Login"
- ✅ Dashboard loads with "Create Listing" button

#### 3. **Create Listing Without Coordinates** (45 seconds)

- Click "Create Listing"
- Fill in:
  - Title: `Community Garden Volunteer Day`
  - Location: `San Francisco, CA`
  - Description: `Help us plant vegetables and flowers in the community garden. All ages welcome!`
- Click "Create Listing"
- ✅ Listing appears in list view

#### 4. **Create Listing With Map Coordinates** (60 seconds)

- Click "Create Listing" again
- Fill in:
  - Title: `Beach Cleanup Event`
  - Location: `Santa Monica Beach`
  - Description: `Join us for a morning beach cleanup. Bring reusable bags!`
- Expand "📍 Add map coordinates"
- Enter coordinates:
  - Latitude: `34.0195`
  - Longitude: `-118.4912`
- Click "Create Listing"
- ✅ Listing created with map data

#### 5. **Toggle to Map View** (30 seconds)

- Click "🗺️ Map" button at top
- ✅ Map displays with OpenStreetMap tiles
- ✅ Marker appears for Beach Cleanup Event
- Click marker
- ✅ Popup shows listing details
- Click "View Details"
- ✅ Detail modal opens

#### 6. **Edit Listing** (45 seconds)

- In detail modal, click "Edit"
- Update description
- Expand "📍 Update map coordinates"
- Change coordinates to Golden Gate Park:
  - Latitude: `37.7694`
  - Longitude: `-122.4862`
- Click "Save Changes"
- ✅ Listing updated
- Switch to Map view
- ✅ Marker moved to new location

#### 7. **Sign Up for Listing** (30 seconds)

- Click "View Details" on any listing
- Click "Sign Up" button
- ✅ Success message: "Signed up successfully!"
- ✅ Button changes to "Cancel Sign-up"

#### 8. **Leave Review** (45 seconds)

- In listing detail modal, scroll to Reviews section
- Click star rating (e.g., 5 stars)
- Enter review text: `Great event! Very organized and friendly volunteers.`
- Click "Submit Review"
- ✅ Review appears with star rating
- ✅ Average rating updates

#### 9. **Toggle Back to List View** (15 seconds)

- Click "📋 List" button
- ✅ All listings displayed in list format
- ✅ View persists during session

---

## Part 4: Screen Recording for Submission

### Recommended Tools

**macOS:**

- **QuickTime Player** (Built-in, free)
  - File → New Screen Recording
  - Select area or full screen
  - Record demo following script above

**Windows:**

- **Xbox Game Bar** (Built-in, free)
  - Press `Win + G`
  - Click record button
  - Follow demo script

**Cross-Platform:**

- **OBS Studio** (Free, open source)
  - Download: https://obsproject.com
  - Professional quality
  - Scene switching, overlays

### Recording Tips

1. **Preparation:**
   - Close unnecessary apps/tabs
   - Clear browser history (fresh state)
   - Test microphone (if doing voiceover)
   - Practice demo script once

2. **Recording Settings:**
   - **Resolution:** 1920x1080 (1080p) minimum
   - **Frame rate:** 30 fps minimum
   - **Audio:** Include system audio + microphone (optional)
   - **Format:** MP4 (H.264 codec)

3. **During Recording:**
   - Speak slowly and clearly (if voiceover)
   - Pause 2-3 seconds between actions
   - Show mouse cursor
   - Highlight important UI elements
   - Don't rush - quality > speed

4. **After Recording:**
   - Watch full video
   - Check audio quality
   - Verify all features demonstrated
   - Trim beginning/end if needed

### Sample Voiceover Script

```
"Welcome to Tapin, a community volunteer platform built with Flask and React.

First, I'll register a new user account... [register]

Now logging in with my credentials... [login]

Let me create a new volunteer listing... [create without coordinates]

Notice I can also add map coordinates for events... [create with coordinates]

Switching to map view, we can see our event markers on an interactive map... [toggle to map]

Clicking a marker shows the listing details... [click marker]

I can edit listings and update their locations... [edit]

Users can sign up for events... [sign up]

And leave reviews with star ratings... [leave review]

The map view makes it easy to find nearby volunteer opportunities.

Thank you for watching!"
```

---

## Part 5: Stopping the Application

### Graceful Shutdown

**Backend:**

```bash
# In backend terminal, press:
Ctrl + C

# Deactivate virtual environment:
deactivate
```

**Frontend:**

```bash
# In frontend terminal, press:
Ctrl + C
```

---

## Part 6: Troubleshooting

### Port Already in Use (Backend)

```bash
# Find process using port 5000
lsof -ti:5000

# Kill process
lsof -ti:5000 | xargs kill -9

# Restart backend
python app.py
```

### Port Already in Use (Frontend)

```bash
# Vite will automatically use next available port
# Usually 5174 if 5173 is taken
```

### Database Locked Error

```bash
# Stop backend server
# Delete database file
rm backend/data.db

# Reinitialize database
cd backend
source .venv/bin/activate
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### CORS Errors in Browser

```bash
# Verify backend CORS settings in app.py:
# CORS(app) should allow all origins in development

# Or explicitly set:
# CORS(app, origins=['http://localhost:5173'])
```

### Leaflet Map Not Loading

```bash
# Verify packages installed:
cd frontend
npm list leaflet react-leaflet

# If missing:
npm install leaflet react-leaflet@^4.2.1 --legacy-peer-deps

# Restart frontend server
```

---

## Part 7: Sample Data for Demo

### Pre-Load Test Listings

Create `backend/seed_demo_data.py`:

```python
from app import app, db, User, Listing
from werkzeug.security import generate_password_hash

def seed_demo_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create demo user
        user = User(
            username='demo_user',
            email='demo@example.com',
            password=generate_password_hash('Demo123!@#')
        )
        db.session.add(user)
        db.session.commit()

        # Create sample listings
        listings = [
            {
                'title': 'Beach Cleanup',
                'location': 'Santa Monica Beach',
                'description': 'Join us for a morning beach cleanup!',
                'latitude': 34.0195,
                'longitude': -118.4912,
                'user_id': user.id
            },
            {
                'title': 'Food Bank Volunteers',
                'location': 'Downtown LA',
                'description': 'Help sort and pack food donations.',
                'latitude': 34.0522,
                'longitude': -118.2437,
                'user_id': user.id
            },
            {
                'title': 'Park Tree Planting',
                'location': 'Golden Gate Park',
                'description': 'Plant native trees in the park.',
                'latitude': 37.7694,
                'longitude': -122.4862,
                'user_id': user.id
            }
        ]

        for data in listings:
            listing = Listing(**data)
            db.session.add(listing)

        db.session.commit()
        print(f'✅ Seeded {len(listings)} listings for demo user')

if __name__ == '__main__':
    seed_demo_data()
```

Run before demo:

```bash
cd backend
source .venv/bin/activate
python seed_demo_data.py
```

---

## Part 8: Quick Reference

### One-Command Startup (After Initial Setup)

**macOS/Linux:**

Create `start.sh` in project root:

```bash
#!/bin/bash

# Start backend in background
cd backend && source .venv/bin/activate && python app.py &
BACKEND_PID=$!

# Start frontend in background
cd frontend && npm run dev &
FRONTEND_PID=$!

echo "✅ Backend running (PID: $BACKEND_PID)"
echo "✅ Frontend running (PID: $FRONTEND_PID)"
echo "🌐 Open: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID" INT
wait
```

Make executable and run:

```bash
chmod +x start.sh
./start.sh
```

---

## ✅ Demo Checklist

### Pre-Demo

- [ ] Backend dependencies installed
- [ ] Frontend dependencies installed
- [ ] Database initialized
- [ ] Sample data seeded (optional)
- [ ] Screen recording tool tested
- [ ] Microphone tested (if voiceover)
- [ ] Browser cache cleared

### During Demo

- [ ] Backend server running
- [ ] Frontend server running
- [ ] Register user
- [ ] Login
- [ ] Create listing without coordinates
- [ ] Create listing with coordinates
- [ ] Toggle to map view
- [ ] Click marker, view popup
- [ ] Edit listing
- [ ] Sign up for listing
- [ ] Leave review
- [ ] Toggle back to list view

### Post-Demo

- [ ] Stop both servers
- [ ] Save screen recording
- [ ] Watch recording for quality check
- [ ] Export video (MP4 format)
- [ ] Upload to submission platform

---

## 🎬 Video Export Settings

### Recommended Settings for Submission

```
Format:        MP4
Codec:         H.264
Resolution:    1920x1080 (1080p)
Frame Rate:    30 fps
Bitrate:       5000 kbps (video)
Audio:         AAC, 128 kbps
Duration:      5-10 minutes
File Size:     ~200-500 MB
```

### Compression (if file too large)

**macOS:**

```bash
# Using FFmpeg (install: brew install ffmpeg)
ffmpeg -i input.mp4 -vcodec h264 -acodec aac -b:v 3000k -b:a 128k output.mp4
```

**Online Tool:**

- https://www.freeconvert.com/video-compressor
- Upload, compress, download

---

## 📊 Common Issues & Fixes

| Issue            | Solution                               |
| ---------------- | -------------------------------------- |
| Port 5000 in use | `lsof -ti:5000 \| xargs kill -9`       |
| Database locked  | Delete `backend/data.db`, reinitialize |
| CORS errors      | Check backend CORS config              |
| Map not loading  | Reinstall leaflet packages             |
| Build errors     | `npm install` again                    |
| Python errors    | Check virtual environment active       |

---

## 🎯 Success Criteria

Your demo is ready when:

- ✅ Both servers start without errors
- ✅ Can register and login
- ✅ Can create/edit/delete listings
- ✅ Map view displays correctly
- ✅ Markers appear at correct locations
- ✅ Sign-ups and reviews work
- ✅ Screen recording quality good
- ✅ All features demonstrated in 5-10 minutes

---

**Total Setup Time:** 2 minutes (after dependencies installed)  
**Demo Duration:** 5-10 minutes  
**Cost:** $0 (FREE!)  
**Perfect for:** School submissions, quick demos, testing

---

**Last Updated:** November 3, 2025  
**Prepared by:** @qa
