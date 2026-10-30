---
name: dynamic-wireframe-mapper
description: |
  Dynamically analyzes a provided document (PRD, UI/UX design draft, or user flow)
  and generates a component dependency wireframe graph showing how components,
  states, and systems interact.
compatibility: opencode
---
  This skill adapts its output based on the document type and extracts:
  - Component relationships
  - Trigger flows
  - Data flow
  - UI → Backend interactions

  Use when:
  - Visualizing system behavior from documentation
  - Mapping UI interactions before development
  - Understanding dependencies between components
  - Creating wireframe-style system diagrams

outputs:
-  format: markdown
-  destination: /docs/frontend/references/wireframes.md
---

# Component Dependency Mapper (Dynamic)

You are responsible for analyzing a document and generating a **wireframe interaction graph**.

---

# Execution Rules (MANDATORY)

- ALWAYS ingest the provided document first  
- Dynamically determine document type if not provided  
- Adapt graph structure based on document type  
- ONLY include relationships supported by the document  
- DO NOT invent components without evidence  
- Maintain clean, readable ASCII structure  
- Ensure graph reflects real system flow  
- Output must be saved to `/docs/wireframes`  

---

# Step 1 — Ingest Document

Load `document_path`.

If `document_type` is not provided:

Detect based on content:

- PRD → features, requirements, user roles  
- UI Design → components, layouts, pages  
- User Flow → steps, navigation, transitions  

---

# Step 2 — Extract Core Elements

## If PRD:
- Features
- User actions
- System responses
- Data dependencies

## If UI Design:
- Components
- Layout hierarchy
- Interaction triggers
- Visual states

## If User Flow:
- Steps
- Decision points
- Transitions
- Entry/exit states

---

# Step 3 — Build Dependency Model

Create relationships:

```plaintext
User Action → UI Component → Event → State → API → Backend → Response → UI
```
Map:

- Trigger chains
- Component dependencies
- Data movement
- Conditional logic

# Step 4 — Select Graph Type

Based on `output_mode`:

## component-flow

Focus on:

- UI components
- Interaction triggers

## data-flow

Focus on:

- State
- API calls
- Backend interaction
- full-system (default)

Combine both

# Step 5 — Generate Wireframe Graph

## Use ASCII diagram format:

Rules:

- Top = user entry
- Middle = UI + logic
- Bottom = backend/data
- Use arrows (↓, →)
- Use decision branches where needed
- Graph Templates (Dynamic)
- PRD-Based Graph
- User → Feature → UI → Action → API → Backend → Data → Response → UI
- UI Design Graph
- User → Component → Event → State → UI Update
- User Flow Graph
- Start → Step → Decision → Path A / Path B → Outcome

# Step 6 — Add Conditional Logic

If decisions exist:
```
        ┌──────────────┐
        │ Condition ?  │
        └──────┬───────┘
          Yes  │   No
              ▼
```

# Step 7 — Final Output
## COMPONENT DEPENDENCY GRAPH
```
[Generated wireframe graph]
```
---

## Summary
 
- Document type detected:
- Components identified:
- Key triggers:
- Data flow points:
 
##  Notes
- Any inferred relationships (if necessary)
- Missing clarity in source document
- 
## Behavior Summary
- Fully dynamic based on document type
- Converts documentation → system visualization
- Produces wireframe-style ASCII graphs
- Supports PRD, UI, and user flows
- Aligns UI + backend interactions
