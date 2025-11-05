# Tapin - Community Connection Platform

**A Flask + React platform connecting communities through volunteer opportunities and local services**

## 📖 What is Tapin?

Tapin connects communities in two ways:

- **Volunteer Opportunities**: Organizations post volunteer needs, and volunteers discover meaningful community service opportunities
- **Local Services**: Small businesses and professionals list their services for the community

Built with modern web development practices: React, Flask, PostgreSQL, and Leaflet maps.

---

## ✨ Features

### Phase 1 - Core Features ✅ (Current)

- ✅ **Authentication**: Volunteers, organizations, and business registration
- ✅ **Dual Listings**: Post volunteer opportunities OR local services
- ✅ **Signup System**: Volunteers can sign up for opportunities
- ✅ **Reviews & Ratings**: Community feedback system
- ✅ **Ownership Verification**: Users manage their own listings
- ✅ **Password Reset**: Email-based password recovery
- ✅ **Interactive Maps**: View opportunities by location (Leaflet + OpenStreetMap)
- ✅ **List/Map Toggle**: Switch between list and map views
- ✅ **Category Filtering**: Filter by volunteer or business listings
- ✅ **Comprehensive Tests**: 30+ backend tests, 8+ frontend tests

### Phase 2 - Future Enhancements 🔜

- PostgreSQL migration (from SQLite)
- Redis + Celery for async tasks
- Advanced AI agent features
- Semantic search with embeddings

---

## 🛠 Tech Stack

| Layer        | Technologies                                      |
| ------------ | ------------------------------------------------- |
| **Frontend** | React 18.2, Vite 5.0, Tailwind CSS, Leaflet 1.9.4 |
| **Backend**  | Flask 2.2+, SQLAlchemy 3.0, Flask-JWT 4.4         |
| **Database** | SQLite (dev), PostgreSQL (prod ready)             |
| **Testing**  | pytest (backend), Vitest (frontend)               |
| **Maps**     | Leaflet + OpenStreetMap (FREE, no API keys)       |

---

## 📋 Prerequisites

Before starting, ensure you have:

- **Python 3.10+**
- **Node.js 18+**
- **Git**
- **macOS/Linux/Windows with a terminal**

---

## 🚀 Getting Started (5 minutes)

### Step 1: Clone & Navigate

```bash
git clone https://github.com/4GeeksAcademy/Tapin.git
cd Tapin
```

### Step 2: Backend Setup

Open a terminal in the `backend` folder:

```bash
cd backend

# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Initialize database
python -c "from app import app, db; app.app_context().push(); db.create_all()"

# Optionally seed sample data
python seed_sample_data.py

# Start Flask server
python app.py
```

✅ Backend running at: `http://127.0.0.1:5000`

### Step 3: Frontend Setup

Open a **new terminal** in the `frontend` folder:

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

✅ Frontend running at: `http://localhost:5173`

---

## ✅ Running Tests

### Backend Tests

```bash
cd backend
source .venv/bin/activate
pytest tests/
```

### Frontend Tests

```bash
cd frontend
npm run test
```

---

## 📚 Documentation

| Document                                | Purpose                                       |
| --------------------------------------- | --------------------------------------------- |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | System design, database schema, API endpoints |
| [CONTRIBUTING.md](CONTRIBUTING.md)      | How to contribute code                        |
| [API_DOCS.md](backend/API_DOCS.md)      | Complete API reference                        |

---

## 🚢 Deployment

### Deploy to Render (FREE tier)

1. Fork this repository
2. Connect to Render at [render.com](https://render.com)
3. Create Web Service from GitHub
4. Build command: `pip install -r requirements.txt && npm install && npm run build`
5. Start command: `python app.py`
6. Add environment variables from `.env.sample`

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed deployment steps.

---

## � Project Structure

```
Tapin/
├── backend/              # Flask API
│   ├── app.py           # Main Flask app
│   ├── auth.py          # Authentication logic
│   ├── tests/           # Test suite
│   └── requirements.txt  # Python dependencies
│
├── frontend/            # React application
│   ├── src/
│   │   ├── App.jsx      # Main component
│   │   ├── pages/       # Route pages
│   │   └── components/  # React components
│   ├── package.json     # Node dependencies
│   └── vite.config.js   # Vite configuration
│
├── docs/               # Documentation
├── Design-Assets/      # Brand assets, mockups
└── README.md          # This file
```

---

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🆘 Troubleshooting

### Backend won't start

```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Clear cache and reinstall
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Try running directly
python app.py
```

### Port 5000 already in use

```bash
# macOS/Linux: Kill process using port 5000
lsof -ti:5000 | xargs kill -9

# Windows: Use netstat or Task Manager to free port 5000
```

### Frontend won't load

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### Database issues

```bash
cd backend
rm data.db  # Delete old database
python -c "from app import app, db; app.app_context().push(); db.create_all()"
python seed_sample_data.py
```

---

## 🎯 What's Next?

- **Try the app**: Visit http://localhost:5173 and explore listings
- **Create an account**: Sign up as a volunteer or organization
- **Post a listing**: Create a volunteer opportunity or local service
- **View on map**: See all listings on the interactive map
- **Run tests**: Verify everything works with `pytest` and `npm run test`

---

## 📞 Questions or Issues?

- Check [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines
- Review API docs at [backend/API_DOCS.md](backend/API_DOCS.md)
- Check system architecture at [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

**Happy coding! 🚀**
npm run dev

# 4. Open http://localhost:5173

````

**� Complete guide:** [Local-Demo-Guide.md](Documents/Local-Demo-Guide.md)

### Option 2: Deploy to Render (FREE)

For a live demo URL to share:

**📖 Step-by-step guide:** [Story-3.2-Render-Deployment.md](Documents/Story-3.2-Render-Deployment.md)

---

## 📚 Documentation

### Project Documentation

- **[Local Demo Guide](Documents/Local-Demo-Guide.md)** - Run locally + screen recording tips
- **[Render Deployment Guide](Documents/Story-3.2-Render-Deployment.md)** - Deploy to FREE hosting
- **[API Documentation](backend/API_DOCS.md)** - Backend API endpoints
- **[Sprint 3 Architecture](Documents/Sprint-3-Architecture-Design.md)** - Architecture decisions

### Sprint Reports

- **[Sprint 1 Completion](Documents/Sprint-1-Completion-Report.md)** - Core features completed
- **[Sprint 2 QA Report](Documents/Sprint-2-QA-Report.md)** - Testing framework setup
- **[Story 3.1 Map Testing](Documents/Story-3.1-Map-Testing.md)** - Map integration tests

### Setup Guides

- **[Backend README](backend/README.md)** - Backend setup and configuration
- **[Frontend README](frontend/README.md)** - Frontend setup and build
- **[Backend Config Guide](backend/CONFIG.md)** - Environment variables

---

## 🧪 Running Tests

### Backend Tests (32+ test cases)

```bash
cd backend
source .venv/bin/activate
pytest
pytest --cov=. --cov-report=html  # With coverage
````

### Frontend Tests

```bash
cd frontend
npm test                  # Run tests
npm run test:ui          # Interactive UI
npm run test:coverage    # With coverage
```

---

## 🗂 Project Structure

```
Tapin/
├── backend/              # Flask API
│   ├── app.py           # Main application
│   ├── auth.py          # JWT authentication
│   ├── requirements.txt # Python dependencies
│   ├── tests/           # Backend test suite
│   └── data.db          # SQLite database (dev)
├── frontend/            # React app
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── test/        # Frontend tests
│   │   └── App.jsx      # Main app component
│   ├── package.json
│   └── vite.config.js
├── Documents/           # Project documentation
│   ├── Local-Demo-Guide.md
│   ├── Story-3.2-Render-Deployment.md
│   └── Sprint-*.md
└── bmad-core/          # BMad agent framework
```

---

## 🎯 Development Workflow

This project was built using the **BMad Method** - an AI-assisted agile development framework:

1. **Planning Phase** - @analyst, @pm, @architect created requirements and design
2. **Development Phase** - @dev implemented features with @sm guidance
3. **QA Phase** - @qa created test suites and verified quality
4. **Documentation Phase** - Comprehensive guides created throughout

**Learn more about BMad Method below** ⬇️

---

## 🤝 Contributing

This is a school project, but contributions are welcome:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- Built using the [BMad Method](https://github.com/bmadcode/bmad-method) AI agent framework
- Maps powered by [Leaflet](https://leafletjs.com/) + [OpenStreetMap](https://www.openstreetmap.org/)
- Testing with [pytest](https://pytest.org/) and [Vitest](https://vitest.dev/)

---

# 🤖 Built with BMad Method™

This repository contains:

- `backend/` — Flask API (SQLite dev database)
- `frontend/` — React + Vite frontend
- `bmad-core/` — BMad agent files (installed via the BMad installer)

---

# BMAD-METHOD™: Universal AI Agent Framework

> ## 🚨 **IMPORTANT VERSION ANNOUNCEMENT** 🚨
>
> ### Current Stable: v4.x | Next Major: v6 Alpha
>
> - **v4.x** - The current stable release version available via npm
> - **v5** - Skipped (replaced by v6)
> - **[v6-alpha](https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha)** - **NOW AVAILABLE FOR EARLY TESTING!**
>
> ### 🧪 Try v6 Alpha (Early Adopters Only)
>
> The next major version of BMAD-METHOD is now available for early experimentation and testing. This is a complete rewrite with significant architectural changes.
>
> **⚠️ WARNING: v6-alpha is for early adopters who are comfortable with:**
>
> - Potential breaking changes
> - Daily updates and instability
> - Incomplete features
> - Experimental functionality
>
> **📅 Timeline:** Official beta version will be merged mid-October 2025
>
> **To try v6-alpha:**
>
> ```bash
> git clone https://github.com/bmad-code-org/BMAD-METHOD.git
> cd BMAD-METHOD
> git checkout v6-alpha
> ```
>
> ---

[![Version](https://img.shields.io/npm/v/bmad-method?color=blue&label=version)](https://www.npmjs.com/package/bmad-method)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)](https://nodejs.org)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

Foundations in Agentic Agile Driven Development, known as the Breakthrough Method of Agile AI-Driven Development, yet so much more. Transform any domain with specialized AI expertise: software development, entertainment, creative writing, business strategy to personal wellness just to name a few.

**[Subscribe to BMadCode on YouTube](https://www.youtube.com/@BMadCode?sub_confirmation=1)**

**[Join our Discord Community](https://discord.gg/gk8jAdXWmj)** - A growing community for AI enthusiasts! Get help, share ideas, explore AI agents & frameworks, collaborate on tech projects, enjoy hobbies, and help each other succeed. Whether you're stuck on BMad, building your own agents, or just want to chat about the latest in AI - we're here for you! **Some mobile and VPN may have issue joining the discord, this is a discord issue - if the invite does not work, try from your own internet or another network, or non-VPN.**

⭐ **If you find this project helpful or useful, please give it a star in the upper right hand corner!** It helps others discover BMAD-METHOD™ and you will be notified of updates!

## Overview

**BMAD-METHOD™'s Two Key Innovations:**

**1. Agentic Planning:** Dedicated agents (Analyst, PM, Architect) collaborate with you to create detailed, consistent PRDs and Architecture documents. Through advanced prompt engineering and human-in-the-loop refinement, these planning agents produce comprehensive specifications that go far beyond generic AI task generation.

**2. Context-Engineered Development:** The Scrum Master agent then transforms these detailed plans into hyper-detailed development stories that contain everything the Dev agent needs - full context, implementation details, and architectural guidance embedded directly in story files.

This two-phase approach eliminates both **planning inconsistency** and **context loss** - the biggest problems in AI-assisted development. Your Dev agent opens a story file with complete understanding of what to build, how to build it, and why.

**📖 [See the complete workflow in the User Guide](docs/user-guide.md)** - Planning phase, development cycle, and all agent roles

## Quick Navigation

### Understanding the BMad Workflow

**Before diving in, review these critical workflow diagrams that explain how BMad works:**

1. **[Planning Workflow (Web UI)](docs/user-guide.md#the-planning-workflow-web-ui)** - How to create PRD and Architecture documents
2. **[Core Development Cycle (IDE)](docs/user-guide.md#the-core-development-cycle-ide)** - How SM, Dev, and QA agents collaborate through story files

> ⚠️ **These diagrams explain 90% of BMad Method Agentic Agile flow confusion** - Understanding the PRD+Architecture creation and the SM/Dev/QA workflow and how agents pass notes through story files is essential - and also explains why this is NOT taskmaster or just a simple task runner!

### What would you like to do?

- **[Install and Build software with Full Stack Agile AI Team](#quick-start)** → Quick Start Instruction
- **[Learn how to use BMad](docs/user-guide.md)** → Complete user guide and walkthrough
- **[See available AI agents](/bmad-core/agents)** → Specialized roles for your team
- **[Explore non-technical uses](#-beyond-software-development---expansion-packs)** → Creative writing, business, wellness, education
- **[Create my own AI agents](docs/expansion-packs.md)** → Build agents for your domain
- **[Browse ready-made expansion packs](expansion-packs/)** → Game dev, DevOps, infrastructure and get inspired with ideas and examples
- **[Understand the architecture](docs/core-architecture.md)** → Technical deep dive
- **[Join the community](https://discord.gg/gk8jAdXWmj)** → Get help and share ideas

## Important: Keep Your BMad Installation Updated

**Stay up-to-date effortlessly!** If you already have BMAD-METHOD™ installed in your project, simply run:

```bash
npx bmad-method install
# OR
git pull
npm run install:bmad
```

This will:

- ✅ Automatically detect your existing v4 installation
- ✅ Update only the files that have changed and add new files
- ✅ Create `.bak` backup files for any custom modifications you've made
- ✅ Preserve your project-specific configurations

This makes it easy to benefit from the latest improvements, bug fixes, and new agents without losing your customizations!

## Quick Start

### One Command for Everything (IDE Installation)

**Just run one of these commands:**

```bash
npx bmad-method install
# OR if you already have BMad installed:
git pull
npm run install:bmad
```

This single command handles:

- **New installations** - Sets up BMad in your project
- **Upgrades** - Updates existing installations automatically
- **Expansion packs** - Installs any expansion packs you've added to package.json

> **That's it!** Whether you're installing for the first time, upgrading, or adding expansion packs - these commands do everything.

**Prerequisites**: [Node.js](https://nodejs.org) v20+ required

### Fastest Start: Web UI Full Stack Team at your disposal (2 minutes)

1. **Get the bundle**: Save or clone the [full stack team file](dist/teams/team-fullstack.txt) or choose another team
2. **Create AI agent**: Create a new Gemini Gem or CustomGPT
3. **Upload & configure**: Upload the file and set instructions: "Your critical operating instructions are attached, do not break character as directed"
4. **Start Ideating and Planning**: Start chatting! Type `*help` to see available commands or pick an agent like `*analyst` to start right in on creating a brief.
5. **CRITICAL**: Talk to BMad Orchestrator in the web at ANY TIME (#bmad-orchestrator command) and ask it questions about how this all works!
6. **When to move to the IDE**: Once you have your PRD, Architecture, optional UX and Briefs - its time to switch over to the IDE to shard your docs, and start implementing the actual code! See the [User guide](docs/user-guide.md) for more details

### Alternative: Clone and Build

```bash
git clone https://github.com/bmadcode/bmad-method.git
npm run install:bmad # build and install all to a destination folder
```

## 🌟 Beyond Software Development - Expansion Packs

BMAD™'s natural language framework works in ANY domain. Expansion packs provide specialized AI agents for creative writing, business strategy, health & wellness, education, and more. Also expansion packs can expand the core BMAD-METHOD™ with specific functionality that is not generic for all cases. [See the Expansion Packs Guide](docs/expansion-packs.md) and learn to create your own!

## Documentation & Resources

### Essential Guides

- 📖 **[User Guide](docs/user-guide.md)** - Complete walkthrough from project inception to completion
- 🏗️ **[Core Architecture](docs/core-architecture.md)** - Technical deep dive and system design
- 🚀 **[Expansion Packs Guide](docs/expansion-packs.md)** - Extend BMad to any domain beyond software development

## Support

- 💬 [Discord Community](https://discord.gg/gk8jAdXWmj)
- 🐛 [Issue Tracker](https://github.com/bmadcode/bmad-method/issues)
- 💬 [Discussions](https://github.com/bmadcode/bmad-method/discussions)

## Contributing

**We're excited about contributions and welcome your ideas, improvements, and expansion packs!** 🎉

📋 **[Read CONTRIBUTING.md](CONTRIBUTING.md)** - Complete guide to contributing, including guidelines, process, and requirements

### Working with Forks

When you fork this repository, CI/CD workflows are **disabled by default** to save resources. This is intentional and helps keep your fork clean.

#### Need CI/CD in Your Fork?

See our [Fork CI/CD Guide](.github/FORK_GUIDE.md) for instructions on enabling workflows in your fork.

#### Contributing Workflow

1. **Fork the repository** - Click the Fork button on GitHub
2. **Clone your fork** - `git clone https://github.com/YOUR-USERNAME/BMAD-METHOD.git`
3. **Create a feature branch** - `git checkout -b feature/amazing-feature`
4. **Make your changes** - Test locally with `npm test`
5. **Commit your changes** - `git commit -m 'feat: add amazing feature'`
6. **Push to your fork** - `git push origin feature/amazing-feature`
7. **Open a Pull Request** - CI/CD will run automatically on the PR

Your contributions are tested when you submit a PR - no need to enable CI in your fork!

## License

MIT License - see [LICENSE](LICENSE) for details.

## Trademark Notice

BMAD™ and BMAD-METHOD™ are trademarks of BMad Code, LLC. All rights reserved.

[![Contributors](https://contrib.rocks/image?repo=bmadcode/bmad-method)](https://github.com/bmadcode/bmad-method/graphs/contributors)

<sub>Built with ❤️ for the AI-assisted development community</sub>
