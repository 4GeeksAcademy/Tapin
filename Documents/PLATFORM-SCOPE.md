# Tapin Platform Scope & Strategy

**Last Updated:** November 3, 2025  
**Status:** Active Development

---

## 📋 Platform Overview

**Tapin** is a dual-purpose community connection platform that serves two distinct but complementary needs:

### 1. 🤝 Volunteer Opportunities (Primary Focus)

**Purpose:** Connect volunteers with community service opportunities

**Key Features:**

- Organizations post volunteer needs with location, date, and requirements
- Volunteers browse opportunities by category (Community Service, Environmental, Education, etc.)
- Sign-up system to connect volunteers with organizations
- Location-based discovery via interactive map
- Reviews and ratings for organizations

**User Types:**

- **Volunteers:** Browse, search, filter, and sign up for opportunities
- **Organizations:** Post and manage volunteer opportunities

### 2. 💼 Local Services (Secondary Focus)

**Purpose:** Help small businesses and professionals reach the local community

**Key Features:**

- Businesses list their services with contact information
- Community members discover local providers
- Location-based discovery via interactive map
- Categories: Business, Services, Professional
- Reviews and ratings for service providers

**User Types:**

- **Community Members:** Browse and discover local services
- **Business Owners:** List and manage service offerings

---

## 🎯 Strategic Rationale

### Why Dual Purpose?

1. **Broader Appeal:** Serves both community service and economic needs
2. **Increased Engagement:** More listing types = more active users
3. **Realistic Scope:** Demonstrates full-stack capabilities while remaining focused
4. **School Project Friendly:** Meets "3+ views and CRUD" requirements with clear purpose
5. **Filter Flexibility:** Users can easily toggle between volunteer and business listings

### Volunteer-First Philosophy

While supporting both types of listings, the platform maintains **volunteer opportunities as the primary focus**:

- Marketing copy emphasizes community service first
- Landing page highlights volunteer opportunities prominently
- Default filter view shows all listings with volunteer filter readily available
- Navigation and UX designed for volunteer discovery workflow

---

## 🏗️ Technical Implementation

### Listing Categories

**Volunteer Opportunities:**

- `All` - Show all listings
- `Volunteer` - Filter volunteer opportunities only
- `Community Service` - General community volunteer work
- `Environmental` - Green/sustainability projects

**Business/Services:**

- `Business` - Local businesses
- `Services` - Professional services

### Database Schema

Single `Listing` model supports both types:

```python
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))  # Maps to filter categories
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # ... reviews, sign-ups, etc.
```

### Frontend Components

- **Filters:** Category chips for easy filtering (Volunteer/Business/etc.)
- **MapView:** Unified map showing both listing types with appropriate icons
- **ListingCard:** Displays both volunteer opportunities and service listings
- **CreateListingForm:** Single form with category selector

---

## 📊 User Stories Alignment

### Updated User Stories

**US3a:** As an organization owner, I want to create volunteer opportunity listings so volunteers can find and sign up for them. _(High, MVP)_

**US3b:** As a business owner, I want to create service listings so community members can discover my business. _(Medium, MVP)_

**US4:** As a user, I want to browse and filter listings by type (Volunteer/Business) and category so I can find what I'm looking for. _(High, MVP)_

**US6a:** As a volunteer, I want to sign up for opportunities so I can contribute to my community. _(High, MVP)_

**US6b:** As a community member, I want to contact businesses for services. _(Medium, MVP)_

---

## 🚀 Current Status

### ✅ Completed (Sprint 3)

- [x] Dual-purpose messaging in landing page
- [x] Updated header subtitle to "Community Connections"
- [x] Filter categories support both types
- [x] Map integration works for all listing types
- [x] Documentation updated with scope clarity

### 🔄 In Progress

- [ ] Ensure forms clearly indicate listing type selection
- [ ] Update API documentation with dual listing context
- [ ] Add visual indicators (icons) to differentiate volunteer vs. business listings

### 📝 Future Enhancements

- [ ] Separate "Post Volunteer Opportunity" vs. "List Service" buttons
- [ ] Category-specific fields (e.g., volunteer hours needed, service pricing)
- [ ] Different sign-up flows for volunteer vs. business contact
- [ ] Analytics showing volunteer vs. business listing ratios

---

## 📖 Documentation References

All documentation has been updated to reflect the dual-purpose strategy:

- **[README.md](../README.md)** - Main project description
- **[Project-Roadmap.md](Project-Roadmap.md)** - Updated user stories
- **[Sprint-3-Architecture-Design.md](Sprint-3-Architecture-Design.md)** - Architecture with scope context
- **[Story-3.1-Map-Testing.md](Story-3.1-Map-Testing.md)** - Map testing for both listing types
- **[Local-Demo-Guide.md](Local-Demo-Guide.md)** - Demo guide with platform overview
- **[INDEX.md](INDEX.md)** - Documentation index with scope summary

---

## 🎓 Educational Value

This dual-purpose approach demonstrates:

1. **Product Strategy:** Clear primary/secondary focus
2. **Flexible Architecture:** Single model supporting multiple use cases
3. **User-Centric Design:** Easy filtering between contexts
4. **Scalability:** Architecture supports future listing types
5. **Real-World Thinking:** Platforms often serve multiple audiences

---

**Questions or suggestions?** Update this document and notify the team.
