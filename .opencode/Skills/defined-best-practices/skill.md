---
name: researching-tech-stack-best-practices
description: Reads stack-definition.md, extracts each technology in the stack, researches best practices using an MCP server (e.g., Context7), and generates structured best-practice documentation per technology.
compatibility: opencode
---

# Researching Tech Stack Best Practices

## Purpose

This skill:

1. Reads `Tech-Stack-Decision-Plan.md`
2. Extracts each declared technology
3. Researches best practices for each technology using an MCP server (e.g., Context7)
4. Outputs one structured best-practices file per technology
5. Generates a cross-stack overview document

If 5 technologies are detected → 5 output files are generated.

---

# Hard Requirements

- The file `Tech-Stack-Decision-Plan.md` must exist.
- If not found → stop and report error.
- Do not guess technologies.
- Do not infer technologies not explicitly listed.
- Do not merge best practices between technologies.

---

# Step 1 — Ingest Stack File

Locate:

`Build Plan/Active Plans/1-4 Stage Planning/Stage-1/markdown
/Tech-Stack-Decision-Plan.md`

Read file fully.

Extract:

- Frontend framework
- Backend framework
- Database
- ORM
- Auth provider
- State management
- Hosting
- DevOps tools
- Testing frameworks
- Other explicitly listed libraries

Normalize naming:

Example:
- NextJS → Next.js
- Postgres → PostgreSQL
- Node → Node.js

Remove duplicates.

---

# Step 2 — Confirm Technology List

Output detected technologies:

Detected Stack:

1. Technology A
2. Technology B
3. Technology C

If ambiguity exists:
Ask one clarification question.

Proceed only after confirmation.

---

# Step 3 — MCP Research Loop

For EACH technology:

Call MCP research tool with structured research request:

Research:

- Official documentation best practices
- Production architecture patterns
- Folder structure recommendations
- Security guidelines
- Performance optimization strategies
- Scaling strategies
- Deployment best practices
- Testing strategies
- Common pitfalls
- Versioning guidance

Each technology must be researched independently.

If MCP fails for one technology:
Continue others.
Report failure clearly.

---

# Step 4 — Output Structure Per Technology

For each tech create:

./system/stack-best-practices/[tech-name].md

Format:

# [Technology Name] — Best Practices

## 1. Recommended Architecture Patterns
## 2. Project Structure
## 3. Security Best Practices
## 4. Performance Optimization
## 5. Scalability Considerations
## 6. Deployment Guidance
## 7. Testing Strategy
## 8. Common Pitfalls
## 9. Ecosystem Tools
## 10. Version Management

All sections must contain researched content.
If not applicable → state "Not Applicable".

---

# Step 5 — Generate Stack Overview

Create:

/system/stack-best-practices/overview.md

Include:

# Stack Overview

## Stack Summary
## Integration Considerations
## Cross-Technology Compatibility Risks
## Architectural Recommendations
## Suggested Environment Structure
## CI/CD Considerations
## Observability & Logging Recommendations

This overview analyzes the stack as a system.

---

# Validation Before Completion

Ensure:

- Number of output files equals number of detected technologies.
- No duplicated content across tech files.
- All sections populated.
- Overview file created.
- Clear failure notices if any MCP research failed.

---

# Prohibited Actions

NEVER:

- Combine multiple technologies in one file.
- Fabricate best practices.
- Assume hosting or deployment environment.
- Skip security or performance sections.
- Skip overview generation.

ALWAYS:

- Keep outputs modular.
- Maintain consistent formatting.
- Preserve deterministic structure.
- Keep documentation production-ready.
