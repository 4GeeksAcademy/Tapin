# Tapin Project Roadmap & User Stories

## Project Scope & Strategy

**Tapin** is a dual-purpose community connection platform:

1. **🤝 Volunteer Opportunities** - Primary focus: Organizations post volunteer needs, volunteers discover and sign up for community service opportunities
2. **💼 Local Services** - Secondary: Small businesses and professionals can list services for the community

This dual strategy allows the platform to serve both community service needs and local economic growth while maintaining a clear volunteer-first mission.

---

## Epics & User Stories

### Epic 1: User Authentication & Security

- **US1:** As a user, I want to register and log in so I can access my account and participate. _(High, MVP)_
  - Acceptance: User can register, log in, and session is maintained securely.
- **US2:** As a user, I want to reset my password via email so I can recover access if needed. _(High, MVP)_
  - Acceptance: User requests reset, receives email, and can set a new password (encrypted).

### Epic 2: Dual Listing Management (Volunteer + Business)

- **US3a:** As an organization owner, I want to create volunteer opportunity listings so volunteers can find and sign up for community service. _(High, MVP)_
  - Acceptance: Organization can create, update, and delete volunteer opportunity listings with category, location, and requirements; changes are reflected in UI and DB.
- **US3b:** As a business owner, I want to create service listings so community members can discover my business. _(Medium, MVP)_
  - Acceptance: Business owner can create, update, and delete service listings with category, location, and contact info.
- **US4:** As a volunteer, I want to browse and filter volunteer opportunities by category and location so I can find meaningful ways to contribute. _(High, MVP)_
  - Acceptance: Listings can be filtered by type (Volunteer/Business), category (Community Service, Environmental, etc.), location, and rating.
- **US4b:** As a community member, I want to browse and filter local services so I can find trusted providers. _(Medium, MVP)_
  - Acceptance: Business listings can be filtered by category, location, and rating.
- **US5:** As a user, I want to view a listing detail page (with reviews, contact info, and action buttons) so I can decide to participate or contact. _(High, MVP)_
  - Acceptance: Detail page shows all info, reviews, sign-up button (for volunteer) or contact info (for business).
- **US6a:** As a volunteer, I want to sign up for opportunities so I can contribute to my community. _(High, MVP)_
  - Acceptance: Volunteer can sign up for opportunities and organization is notified.
- **US6b:** As a community member, I want to contact businesses for services. _(Medium, MVP)_
  - Acceptance: Contact information is clearly displayed for business listings.

### Epic 3: Core Platform & Deployment

- **US7:** As a developer, I want to deploy the app live so it’s accessible to users. _(High, MVP)_
  - Acceptance: App is deployed to production and accessible via public URL.
- **US8:** As a team member, I want to document API endpoints and architecture so the project is clear and maintainable. _(Low)_
  - Acceptance: API_DOCS.md and ARCHITECTURE.md are complete and up to date.

### Epic 4: Map Integration & Location-Based Discovery

- **US9:** As a user, I want to see both volunteer opportunities and business listings on an interactive map so I can find options by location. _(High, MVP)_
  - Acceptance: Map view displays both listing types with appropriate markers, clickable popups, and filter by category.
- **US9b:** As a user, I want to toggle between list and map views so I can choose my preferred browsing experience. _(Medium, MVP)_
  - Acceptance: Toggle button switches between list grid and map view seamlessly.
- **US10:** As a user, I want to receive email notifications for key actions (volunteer sign-up confirmation, password reset). _(Medium)_
  - Acceptance: Email notifications are sent for sign-ups and password resets.

## Project Roadmap & Milestones

| Phase | Deliverable                                               | Duration   |
| ----- | --------------------------------------------------------- | ---------- |
| 1     | Auth, DB schema, initial deployment                       | Days 1–5   |
| 2     | Dual listing types CRUD APIs + Frontend list/detail views | Days 6–10  |
| 3     | Sign-up/connection, category filters, map integration     | Days 11–15 |
| 4     | Styling, responsiveness, testing                          | Days 16–20 |
| 5     | Final deployment, documentation, buffer                   | Days 21–28 |

## Project Board Columns

- Backlog
- In Progress
- Review
- Done

## Sprint Planning

- **Sprint 1:** Auth, DB, deployment (US1, US2, US7) ✅ **COMPLETE**
- **Sprint 2:** Listings CRUD, browse/filter, detail (US3a, US3b, US4, US4b, US5) ✅ **COMPLETE**
- **Sprint 3:** Sign-up, map, dual categories (US6a, US6b, US9, US9b) ✅ **COMPLETE**
- **Sprint 4:** Docs, polish, testing (US8, US10, bugfixes) 🔄 **IN PROGRESS**

---

## Summary of Completed Features

### ✅ Sprint 1 - Foundation

- User authentication with JWT
- Password reset via email
- Database schema with SQLAlchemy
- Initial backend API structure

### ✅ Sprint 2 - Core Functionality

- Full CRUD for listings (volunteer + business)
- Category-based filtering
- Reviews and ratings system
- Listing detail views
- Ownership verification

### ✅ Sprint 3 - Map & Discovery

- Interactive map with Leaflet + OpenStreetMap
- List/Map toggle view
- Location-based filtering
- Volunteer sign-up system
- Dual-purpose category filters

### 🔄 Sprint 4 - Polish & Documentation

- Complete API documentation
- Comprehensive user guides
- Test coverage expansion
- Email notifications
- Deployment guides (Render free tier)

---

Assign user stories to team members and update the board as progress is made. Each user story should have clear acceptance criteria and be tracked through the board columns.
