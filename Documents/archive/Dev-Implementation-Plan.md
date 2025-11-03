# Dev Implementation Plan – Tapin Project

## 1. Project Structure

- Create a `frontend/` directory for the React app (using Create React App or Vite).
- Create a `backend/` directory for the Flask API.
- Add `README.md` files in both to document setup and usage.

## 2. Core Feature Implementation

- **Auth:**
  - Implement user registration, login, and password reset in Flask (with JWT or Flask-Login).
  - Use bcrypt/argon2 for password hashing.
  - Build React forms for auth flows, with validation and error handling.
- **Listings CRUD:**
  - Design MySQL schema for users, organizations, listings, sign-ups, reviews.
  - Implement RESTful CRUD endpoints in Flask.
  - Build React pages for listing, detail, create/edit, and sign-up.
- **Map Integration:**
  - Integrate Google Maps or OpenStreetMap in React for listing locations.
  - Display pins for each listing; allow filtering by location.
- **Design System:**
  - Apply design tokens and styles from mockups and UX review.
  - Ensure mobile responsiveness and accessibility (WCAG AA, keyboard navigation, alt text).

## 3. Testing & QA

- Write unit and integration tests for backend (pytest, Flask-Testing).
- Use React Testing Library/Jest for frontend tests.
- Collaborate with @qa to define test cases and review coverage.

## 4. Documentation

- Document API endpoints (OpenAPI/Swagger or markdown).
- Update setup instructions and usage in each `README.md`.
- Provide a Postman collection for API testing.

## 5. Technical Questions/Blockers

- Confirm preferred authentication method (JWT vs Flask-Login).
- Clarify deployment target (Heroku, AWS, etc.).
- Confirm which map API to use (Google Maps vs OpenStreetMap).
- Any additional third-party integrations required?

---

**Next Steps:**

1. Scaffold frontend and backend directories.
2. Set up version control and CI/CD basics.
3. Implement authentication and basic CRUD as first sprint.
4. Review with @qa and @pm before expanding features.
