# Tapin Project Roadmap & User Stories

## Epics & User Stories

### Epic 1: User Authentication & Security
- **US1:** As a user, I want to register and log in so I can access my account and participate. *(High, MVP)*
  - Acceptance: User can register, log in, and session is maintained securely.
- **US2:** As a user, I want to reset my password via email so I can recover access if needed. *(High, MVP)*
  - Acceptance: User requests reset, receives email, and can set a new password (encrypted).

### Epic 2: Listings Management (CRUD)
- **US3:** As a business/organization owner, I want to create and edit my listing so I can present my services or opportunities. *(High, MVP)*
  - Acceptance: Owner can create, update, and delete listings; changes are reflected in UI and DB.
- **US4:** As a volunteer, I want to browse and filter local volunteer opportunities/businesses so I can find the right fit. *(Medium, MVP)*
  - Acceptance: Listings can be filtered by category, location, and rating.
- **US5:** As a volunteer, I want to view a listing detail page (with reviews and sign-up option) so I can decide to join. *(Medium, MVP)*
  - Acceptance: Detail page shows all info, reviews, and sign-up button.
- **US6:** As a volunteer, I want to sign up/connect to an opportunity so I can contribute. *(Medium, MVP)*
  - Acceptance: Volunteer can sign up and owner is notified.

### Epic 3: Core Platform & Deployment
- **US7:** As a developer, I want to deploy the app live so it’s accessible to users. *(High, MVP)*
  - Acceptance: App is deployed to production and accessible via public URL.
- **US8:** As a team member, I want to document API endpoints and architecture so the project is clear and maintainable. *(Low)*
  - Acceptance: API_DOCS.md and ARCHITECTURE.md are complete and up to date.

### Epic 4: Integrations & Enhancements
- **US9:** As a user, I want to see listings on a map so I can find opportunities by location. *(Medium)*
  - Acceptance: Map view is available and interactive.
- **US10:** As a user, I want to receive email notifications for key actions (sign-up, password reset). *(Medium)*
  - Acceptance: Email API is integrated and tested.

## Project Roadmap & Milestones

| Phase  | Deliverable                                           | Duration     |
|--------|-------------------------------------------------------|--------------|
| 1      | Auth, DB schema, initial deployment                   | Days 1–5     |
| 2      | Listings CRUD APIs + Frontend list/detail views       | Days 6–10    |
| 3      | Sign-up/connection, search/filter, map integration    | Days 11–15   |
| 4      | Styling, responsiveness, testing                      | Days 16–20   |
| 5      | Final deployment, docs, buffer                        | Days 21–28   |

## Project Board Columns
- Backlog
- In Progress
- Review
- Done

## Sprint Planning
- Sprint 1: Auth, DB, deployment (US1, US2, US7)
- Sprint 2: Listings CRUD, browse/filter, detail (US3, US4, US5)
- Sprint 3: Sign-up, map, notifications (US6, US9, US10)
- Sprint 4: Docs, polish, testing (US8, bugfixes)

---
Assign user stories to team members and update the board as progress is made. Each user story should have clear acceptance criteria and be tracked through the board columns.
