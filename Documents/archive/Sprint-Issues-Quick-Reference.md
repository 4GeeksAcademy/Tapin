# Sprint 1-4 Issues Quick Reference

**Total Issues:** 23 (8 Existing + 15 New)  
**Total Story Points:** 52  
**Estimated Duration:** 12-14 days  
**Start Date:** Ready Now

---

## 🎯 SPRINT 1: Complete MVP Core (3-4 days)

**Goal:** Implement critical MVP features for volunteer engagement

### Issue #11: Sign-up/Connect to Listings

- **Status:** ❌ Not Started
- **Assigned:** @dev, @qa
- **Priority:** 🔴 HIGH (BLOCKS: #14, #22, #23)
- **Estimate:** 1 day
- **Subtasks:** 7
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/11

### Issue #12: Password Reset UI Flow

- **Status:** ❌ Not Started
- **Assigned:** @dev, @ux-expert, @qa
- **Priority:** 🔴 HIGH
- **Estimate:** 0.5 days
- **Subtasks:** 7
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/12

### Issue #13: Edit and Delete Listings

- **Status:** ❌ Not Started
- **Assigned:** @dev, @qa
- **Priority:** 🔴 HIGH
- **Estimate:** 0.5 days
- **Subtasks:** 8
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/13

### Issue #14: Basic Reviews and Ratings

- **Status:** ❌ Not Started
- **Assigned:** @dev, @ux-expert, @qa
- **Priority:** 🟡 MEDIUM
- **Estimate:** 1 day
- **Subtasks:** 10
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/14

---

## 🧪 SPRINT 2: Testing & Polish (4 days)

**Goal:** Ensure code quality and improve user experience

### Issue #15: Frontend Test Suite

- **Status:** ❌ Not Started
- **Assigned:** @qa (lead), @dev (support)
- **Priority:** 🔴 HIGH
- **Estimate:** 2 days
- **Subtasks:** 8
- **Coverage Target:** 80%
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/15

### Issue #16: Expand Backend Test Coverage

- **Status:** ❌ Not Started
- **Assigned:** @qa (lead), @dev (support)
- **Priority:** 🔴 HIGH
- **Estimate:** 1 day
- **Subtasks:** 8
- **Coverage Target:** 80%+
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/16

### Issue #17: Form Validation and Error Handling

- **Status:** ❌ Not Started
- **Assigned:** @dev, @ux-expert, @qa
- **Priority:** 🟡 MEDIUM
- **Estimate:** 1 day
- **Subtasks:** 9
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/17

---

## 🚀 SPRINT 3: Map Integration & Deployment (3.5 days)

**Goal:** Add map features and deploy MVP to production

### Issue #18: Map Component Integration

- **Status:** ❌ Not Started
- **Assigned:** @architect, @dev, @qa
- **Priority:** 🟡 MEDIUM
- **Estimate:** 1.5 days
- **Subtasks:** 11
- **Tech Decision:** Leaflet vs Google Maps
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/18

### Issue #19: Production Environment Setup ⭐ CRITICAL

- **Status:** ❌ Not Started
- **Assigned:** @architect, @dev
- **Priority:** 🔴 HIGH (BLOCKS: #20, #21)
- **Estimate:** 1 day
- **Subtasks:** 9
- **Decision Needed:** Hosting platform
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/19

### Issue #20: CI/CD Pipeline

- **Status:** ❌ Not Started
- **Assigned:** @architect, @dev
- **Priority:** 🟡 MEDIUM
- **Estimate:** 0.5 days
- **Subtasks:** 10
- **Dependencies:** Issue #19
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/20

### Issue #21: Production Deployment ⭐ CRITICAL

- **Status:** ❌ Not Started
- **Assigned:** @dev, @qa
- **Priority:** 🔴 HIGH (UNBLOCKS: MVP Launch)
- **Estimate:** 0.5 days
- **Subtasks:** 10
- **Dependencies:** Issues #19, #20
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/21

---

## 📈 SPRINT 4: Post-MVP Enhancements (4 days)

**Goal:** Polish and optimize for production readiness

### Issue #22: Advanced Search and Filtering

- **Status:** ❌ Not Started
- **Assigned:** @dev, @architect, @qa
- **Priority:** 🟢 LOW
- **Estimate:** 1 day
- **Subtasks:** 10
- **Dependencies:** Issue #18 (for distance sorting)
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/22

### Issue #23: Email Notifications

- **Status:** ❌ Not Started
- **Assigned:** @dev, @ux-expert, @qa
- **Priority:** 🟢 LOW
- **Estimate:** 1 day
- **Subtasks:** 11
- **Dependencies:** Issue #11 (sign-up system)
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/23

### Issue #24: Performance Optimization

- **Status:** ❌ Not Started
- **Assigned:** @architect, @dev, @qa
- **Priority:** 🟢 LOW
- **Estimate:** 1 day
- **Subtasks:** 11
- **Target:** Lighthouse > 90
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/24

### Issue #25: Security Hardening

- **Status:** ❌ Not Started
- **Assigned:** @architect, @dev, @qa
- **Priority:** 🟡 MEDIUM
- **Estimate:** 1 day
- **Subtasks:** 11
- **Pre-Launch Requirement**
- **Link:** https://github.com/4GeeksAcademy/Tapin/issues/25

---

## 📋 EXISTING ISSUES - Status & Next Steps

| #   | Title                     | Status          | % Complete | Next Step             |
| --- | ------------------------- | --------------- | ---------- | --------------------- |
| 1   | User Registration & Login | ✅ Complete     | 90%        | Polish errors (#17)   |
| 2   | Password Reset via Email  | ✅ Backend Done | 70%        | UI (#12)              |
| 3   | Business Listing CRUD     | ✅ Backend Done | 80%        | Edit/Delete UI (#13)  |
| 4   | Browse & Filter Listings  | ⏳ Partial      | 75%        | Adv. Search (#22)     |
| 5   | Listing Detail & Reviews  | ⏳ Partial      | 75%        | Reviews (#14)         |
| 6   | Volunteer Sign-up ❌      | ❌ Blocked      | 0%         | **Sprint 1 #11**      |
| 7   | Production Deployment ❌  | ❌ Blocked      | 0%         | **Sprint 3 #19-21**   |
| 8   | Documentation             | ⏳ Partial      | 50%        | Architecture diagrams |

---

## 🎮 How to Work with These Issues

### For @dev:

```bash
# Sprint 1 work
gh issue view 11 --web  # View issue in browser
gh issue develop 11     # Create feature branch
# Implement and test
gh pr create             # Open pull request
```

### For @qa:

```bash
# Sprint 2 testing
gh issue view 15 --web  # Frontend tests
gh issue view 16 --web  # Backend tests
# Create test plan and execute
```

### For @architect:

```bash
# Sprint 3 infrastructure
gh issue view 19 --web  # Production setup
gh issue view 20 --web  # CI/CD pipeline
# Make decisions and document
```

---

## 🔗 Issue Dependencies & Blocking

```
Sprint 1:
  #11 (Sign-up) → blocks #14, #22, #23

Sprint 2:
  #15, #16, #17 (Independent - run parallel)

Sprint 3:
  #19 (Prod setup) → blocks #20, #21
  #20 (CI/CD) → blocks #21 (Deploy)
  #18 (Map) → independent

Sprint 4:
  #22 (Search) depends on #18 (Map)
  #23 (Email) depends on #11 (Sign-up)
  #24, #25 (Independent)
```

---

## 📊 Success Criteria by Sprint

### Sprint 1 ✅

- [ ] All 4 issues completed
- [ ] Sign-up system fully functional
- [ ] 0 critical bugs
- [ ] All acceptance criteria met

### Sprint 2 ✅

- [ ] Frontend coverage > 80%
- [ ] Backend coverage > 80%
- [ ] All forms validate correctly
- [ ] 0 unresolved errors

### Sprint 3 ✅

- [ ] Backend deployed to production
- [ ] Frontend deployed to production
- [ ] CI/CD pipeline active
- [ ] All smoke tests pass
- [ ] Production URLs documented

### Sprint 4 ✅

- [ ] Lighthouse score > 90
- [ ] All security issues fixed
- [ ] Advanced search implemented
- [ ] Email notifications working
- [ ] Ready for user launch

---

## 📞 Quick Contact

Need help? Mention the appropriate agent:

- **@dev** - Code implementation issues
- **@qa** - Testing and quality issues
- **@architect** - Technical decisions and infrastructure
- **@ux-expert** - UI/UX and design issues
- **@sm** - Blocker removal and process help
- **@po** - Acceptance criteria and approval

---

## 🔄 Issue Workflow

1. **Assigned** → Agent claims issue
2. **In Progress** → Agent creates feature branch
3. **Review** → Submit PR for code review
4. **Testing** → QA verifies acceptance criteria
5. **Done** → Merged to main, deployed

---

**Last Updated:** November 3, 2025  
**Total Issues Ready:** 23  
**Ready to Start:** NOW 🚀
