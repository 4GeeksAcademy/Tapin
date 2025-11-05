# Agent Issue Template

Use this template when creating issues for AI agents to work through. Copy and fill in the bracketed sections for each task.

---

## Issue Template

```markdown
## Objective

[Clear, one-sentence goal for this task]

## Context

[Why is this work important? How does it fit into the sprint?]

## Acceptance Criteria

- [ ] [Specific, testable criterion 1]
- [ ] [Specific, testable criterion 2]
- [ ] [Specific, testable criterion 3]

## Dependencies

- Depends on: [Link other issues or mention @other-agent]
- Blocks: [What work waits on this]

## Resources

- [Link to relevant docs/code]
- [Link to design specs if needed]

## Success Looks Like

[Describe what completion looks like]

## Questions?

Tag @other-agent if you need their input
```

---

## How to Use

1. **Create issue** in GitHub with this template
2. **Assign to** the appropriate agent (@analyst, @dev, @pm, @po, @architect, @qa, @ux-expert, @sm)
3. **Tag related** issues or agents who need visibility
4. **Agent works** through the acceptance criteria
5. **Agent updates** comments with progress
6. **Agent links** PR when ready for review

---

## Example Issue

```markdown
## Objective

Research vector databases and recommend best option for Tapin

## Context

Phase 2 AI infrastructure depends on this decision. Cost and performance
impact platform for 2+ years. Decision blocks @dev infrastructure setup.

## Acceptance Criteria

- [ ] Comparison matrix: Pinecone vs Weaviate vs pgvector
- [ ] Cost projections for 3 years (1K, 10K, 50K users)
- [ ] Risk assessment with mitigation for primary choice
- [ ] Final recommendation with fallback option

## Dependencies

- Depends on: None (can start immediately)
- Blocks: @dev infrastructure setup, @architect design decisions

## Resources

- [AI-ARCHITECTURE-STRATEGY.md](/Documents/AI-ARCHITECTURE-STRATEGY.md)
- [AI-PRODUCT-ROADMAP.md](/Documents/AI-PRODUCT-ROADMAP.md)
- Vendor documentation: Pinecone, Weaviate, pgvector

## Success Looks Like

Team can make confident decision to proceed with chosen vector DB.
Clear cost/performance/risk tradeoffs documented.

## Questions?

@architect - any technical constraints I should know about?
```

---

## Tips

- **Be specific:** Vague criteria = rework
- **Link context:** Reference docs, other issues, PRs
- **Tag agents:** Use @agent-name when you need their input mid-issue
- **Update regularly:** Post progress in comments as you work
- **Close when done:** Mark acceptance criteria ✅ as you complete them

---

**For all agents:** Reference the project documentation:

- BMAD-ORCHESTRATION-PLAN.md - Sprint structure and roles
- AI-PRODUCT-ROADMAP.md - All 47 user stories
- EXEC-SUMMARY.md - Business context
- AI-ARCHITECTURE-STRATEGY.md - Technical strategy
