# Dynamic Page and Component Plan Template

## 1. Product Overview

### Product name

`[PRODUCT NAME]`

### Product type

`[SaaS / Marketplace / Mobile App / Website / Dashboard / E-commerce / Internal Tool / Community / Other]`

### Product description

`[ONE OR TWO SENTENCES EXPLAINING WHAT THE PRODUCT DOES]`

### Primary objective

`[THE MAIN OUTCOME THE PRODUCT HELPS USERS ACHIEVE]`

### Target users

| User type       | Description     | Primary goal |
| --------------- | --------------- | ------------ |
| `[USER TYPE 1]` | `[DESCRIPTION]` | `[GOAL]`     |
| `[USER TYPE 2]` | `[DESCRIPTION]` | `[GOAL]`     |
| `[USER TYPE 3]` | `[DESCRIPTION]` | `[GOAL]`     |

### Supported platforms

* `[ ] Desktop web`
* `[ ] Mobile web`
* `[ ] Native mobile`
* `[ ] Tablet`
* `[ ] Public website`
* `[ ] Authenticated application`
* `[ ] Admin application`

### Core product loop

```text
[USER ENTRY POINT]
    ↓
[PRIMARY ACTION]
    ↓
[PROCESS OR WORKFLOW]
    ↓
[RESULT]
    ↓
[NEXT ACTION OR REPEAT LOOP]
```

---

# 2. Product Scope

## Core features

1. `[CORE FEATURE]`
2. `[CORE FEATURE]`
3. `[CORE FEATURE]`
4. `[CORE FEATURE]`

## Secondary features

1. `[SECONDARY FEATURE]`
2. `[SECONDARY FEATURE]`
3. `[SECONDARY FEATURE]`

## Out-of-scope features

* `[FEATURE NOT INCLUDED]`
* `[FEATURE NOT INCLUDED]`
* `[FEATURE DEFERRED TO LATER PHASE]`

## Key entities

Define the primary objects users interact with.

| Entity     | Description            | Example     |
| ---------- | ---------------------- | ----------- |
| `[ENTITY]` | `[WHAT IT REPRESENTS]` | `[EXAMPLE]` |
| `[ENTITY]` | `[WHAT IT REPRESENTS]` | `[EXAMPLE]` |
| `[ENTITY]` | `[WHAT IT REPRESENTS]` | `[EXAMPLE]` |

Examples include users, projects, products, orders, files, messages, reports, campaigns, tasks, teams, or invoices.

---

# 3. User Roles and Permissions

| Role     | Access level                   | Main permissions |
| -------- | ------------------------------ | ---------------- |
| `[ROLE]` | `[FULL / LIMITED / READ-ONLY]` | `[PERMISSIONS]`  |
| `[ROLE]` | `[FULL / LIMITED / READ-ONLY]` | `[PERMISSIONS]`  |
| `[ROLE]` | `[FULL / LIMITED / READ-ONLY]` | `[PERMISSIONS]`  |

## Permission-sensitive actions

* `[CREATE ENTITY]`
* `[EDIT ENTITY]`
* `[DELETE ENTITY]`
* `[APPROVE ENTITY]`
* `[MANAGE TEAM]`
* `[MANAGE BILLING]`
* `[VIEW ADMIN DATA]`

---

# 4. Information Architecture

## Primary navigation

| Navigation item | Route      | Purpose     | Visible to |
| --------------- | ---------- | ----------- | ---------- |
| `[ITEM]`        | `/[route]` | `[PURPOSE]` | `[ROLES]`  |
| `[ITEM]`        | `/[route]` | `[PURPOSE]` | `[ROLES]`  |
| `[ITEM]`        | `/[route]` | `[PURPOSE]` | `[ROLES]`  |

## Secondary navigation

* `[SUBNAV ITEM]`
* `[SUBNAV ITEM]`
* `[SUBNAV ITEM]`

## Global actions

* `[CREATE]`
* `[SEARCH]`
* `[IMPORT]`
* `[EXPORT]`
* `[NOTIFICATIONS]`
* `[HELP]`
* `[PROFILE MENU]`

## Suggested route structure

```text
/
├── [public-page]
├── auth
│   ├── login
│   ├── signup
│   └── forgot-password
├── app
│   ├── dashboard
│   ├── [primary-feature]
│   │   ├── new
│   │   └── [id]
│   ├── [secondary-feature]
│   └── settings
└── admin
    ├── users
    ├── activity
    └── configuration
```

---

# 5. Global Application Shell

## Header

### Components

* Product logo
* Breadcrumbs
* Page title
* Global search
* Primary create button
* Notifications
* Help
* User profile menu

### Header actions

* `[ACTION]`
* `[ACTION]`
* `[ACTION]`

## Sidebar or primary navigation

### Components

* Workspace or account switcher
* Navigation groups
* Collapsed state
* Active item indicator
* Upgrade or usage indicator
* User profile access

## Mobile navigation

Choose one:

* `[ ] Bottom navigation`
* `[ ] Slide-out drawer`
* `[ ] Compact top navigation`
* `[ ] Hybrid navigation`

## Global overlays

* Command menu
* Notification drawer
* Search overlay
* Create menu
* Confirmation dialog
* Unsaved changes dialog
* Help panel

---

# 6. Page Inventory

Use this table to define every required page before creating detailed specifications.

| ID  | Page     | Route      | Type                                            | Priority          | Primary user goal |
| --- | -------- | ---------- | ----------------------------------------------- | ----------------- | ----------------- |
| P01 | `[PAGE]` | `/[route]` | `[LIST / DETAIL / FORM / DASHBOARD / SETTINGS]` | `[MVP / P1 / P2]` | `[GOAL]`          |
| P02 | `[PAGE]` | `/[route]` | `[TYPE]`                                        | `[PRIORITY]`      | `[GOAL]`          |
| P03 | `[PAGE]` | `/[route]` | `[TYPE]`                                        | `[PRIORITY]`      | `[GOAL]`          |

## Common page categories

* Public marketing pages
* Authentication
* Onboarding
* Dashboard
* List or index pages
* Detail pages
* Create and edit forms
* Workflow or wizard pages
* Search and discovery
* Reports and analytics
* Activity and notifications
* Team administration
* Billing and subscription
* Integrations
* Settings
* Help and support
* Error and system pages

---

# 7. Individual Page Specification

Duplicate this section for every page.

---

## `[PAGE NAME]`

### Page ID

`[P01]`

### Route

`/[route]`

### Page type

`[Dashboard / List / Detail / Form / Wizard / Settings / Marketing / Other]`

### Priority

`[MVP / P1 / P2 / Future]`

### Purpose

`[WHY THIS PAGE EXISTS]`

### Primary user goal

`[WHAT THE USER SHOULD ACCOMPLISH]`

### Entry points

* `[NAVIGATION ITEM]`
* `[BUTTON ON ANOTHER PAGE]`
* `[DIRECT LINK]`
* `[NOTIFICATION]`

### Exit points

* `[NEXT PAGE]`
* `[DETAIL PAGE]`
* `[CONFIRMATION STATE]`
* `[RETURN PAGE]`

### Access rules

* Authentication required: `[YES / NO]`
* Required role: `[ROLE]`
* Required subscription: `[PLAN OR NONE]`
* Required entity state: `[STATE OR NONE]`

### Page layout

```text
[GLOBAL HEADER]
[PAGE HEADER]
[PRIMARY CONTENT AREA]
[SECONDARY PANEL OR SIDEBAR]
[STICKY ACTION AREA]
```

### Page header

#### Content

* Page title
* Description
* Breadcrumbs
* Status badge
* Metadata
* Contextual help

#### Primary action

`[PRIMARY BUTTON]`

#### Secondary actions

* `[BUTTON]`
* `[BUTTON]`
* `[OVERFLOW MENU]`

### Main sections

#### Section 1: `[SECTION NAME]`

Purpose: `[PURPOSE]`

Components:

* `[COMPONENT]`
* `[COMPONENT]`
* `[COMPONENT]`

Actions:

* `[ACTION]`
* `[ACTION]`

#### Section 2: `[SECTION NAME]`

Purpose: `[PURPOSE]`

Components:

* `[COMPONENT]`
* `[COMPONENT]`

Actions:

* `[ACTION]`
* `[ACTION]`

#### Section 3: `[SECTION NAME]`

Purpose: `[PURPOSE]`

Components:

* `[COMPONENT]`
* `[COMPONENT]`

### Data displayed

| Field     | Data type                         | Editable     | Required     | Source                  |
| --------- | --------------------------------- | ------------ | ------------ | ----------------------- |
| `[FIELD]` | `[TEXT / NUMBER / DATE / STATUS]` | `[YES / NO]` | `[YES / NO]` | `[USER / API / SYSTEM]` |
| `[FIELD]` | `[TYPE]`                          | `[YES / NO]` | `[YES / NO]` | `[SOURCE]`              |

### Clickable controls

| Control   | Type                              | Action     | Result     |
| --------- | --------------------------------- | ---------- | ---------- |
| `[LABEL]` | `[BUTTON / LINK / MENU / TOGGLE]` | `[ACTION]` | `[RESULT]` |
| `[LABEL]` | `[TYPE]`                          | `[ACTION]` | `[RESULT]` |

### Filters

* `[FILTER]`
* `[FILTER]`
* `[FILTER]`

### Sorting

* `[SORT OPTION]`
* `[SORT OPTION]`
* `[SORT OPTION]`

### Search behavior

* Search fields: `[FIELDS]`
* Search type: `[INSTANT / SUBMIT / SERVER-SIDE]`
* Empty query behavior: `[BEHAVIOR]`
* No-result behavior: `[BEHAVIOR]`

### Bulk actions

* `[BULK ACTION]`
* `[BULK ACTION]`
* `[BULK ACTION]`

### Pagination or loading

Choose one:

* `[ ] Numbered pagination`
* `[ ] Load more`
* `[ ] Infinite scroll`
* `[ ] Virtualized list`
* `[ ] No pagination`

### Responsive behavior

#### Desktop

`[DESKTOP LAYOUT]`

#### Tablet

`[TABLET LAYOUT]`

#### Mobile

`[MOBILE LAYOUT]`

### Accessibility requirements

* Keyboard accessible
* Visible focus states
* Proper labels
* Semantic heading order
* Screen-reader announcements
* Accessible error messages
* Sufficient contrast
* Touch targets at least 44×44 px where applicable

---

# 8. Component Specification

Duplicate this section for every major reusable component.

## `[COMPONENT NAME]`

### Component ID

`[C01]`

### Purpose

`[WHAT THE COMPONENT DOES]`

### Used on

* `[PAGE]`
* `[PAGE]`
* `[PAGE]`

### Component type

`[Navigation / Form / Data Display / Feedback / Overlay / Media / Action]`

### Anatomy

1. `[ELEMENT]`
2. `[ELEMENT]`
3. `[ELEMENT]`
4. `[ELEMENT]`

### Inputs or props

| Property | Type     | Required     | Description     |
| -------- | -------- | ------------ | --------------- |
| `[PROP]` | `[TYPE]` | `[YES / NO]` | `[DESCRIPTION]` |
| `[PROP]` | `[TYPE]` | `[YES / NO]` | `[DESCRIPTION]` |

### Variants

* `[DEFAULT]`
* `[COMPACT]`
* `[SELECTED]`
* `[DISABLED]`
* `[ERROR]`
* `[LOADING]`

### Interactions

| Trigger  | Behavior     |
| -------- | ------------ |
| Click    | `[BEHAVIOR]` |
| Hover    | `[BEHAVIOR]` |
| Focus    | `[BEHAVIOR]` |
| Keyboard | `[BEHAVIOR]` |

### States

* Default
* Hover
* Focused
* Active
* Selected
* Disabled
* Loading
* Success
* Warning
* Error
* Empty

### Responsive behavior

`[HOW THE COMPONENT CHANGES BY SCREEN SIZE]`

### Accessibility

`[ARIA LABELS, KEYBOARD BEHAVIOR, FOCUS MANAGEMENT, ANNOUNCEMENTS]`

---

# 9. Shared Component Library

## Navigation

* App header
* Sidebar
* Mobile navigation
* Breadcrumbs
* Tabs
* Pagination
* Stepper
* Command menu

## Actions

* Primary button
* Secondary button
* Tertiary button
* Icon button
* Split button
* Overflow menu
* Floating action button
* Destructive button

## Form controls

* Text input
* Textarea
* Number input
* Search field
* Select
* Multi-select
* Combobox
* Checkbox
* Radio group
* Toggle
* Date picker
* Time picker
* File upload
* Rich-text editor
* Tag input
* Slider

## Data display

* Card
* Table
* List
* Grid
* Badge
* Status indicator
* Avatar
* Thumbnail
* Metric card
* Timeline
* Activity feed
* Chart
* Progress bar
* Empty state

## Feedback

* Toast
* Inline alert
* Banner
* Validation message
* Loading skeleton
* Spinner
* Progress indicator
* Success confirmation
* Error state

## Overlays

* Modal
* Confirmation dialog
* Drawer
* Popover
* Tooltip
* Dropdown
* Bottom sheet

---

# 10. Button and Action Inventory

Use this section to prevent missing interactions.

| Button or action | Page/component | Permission | Confirmation required | Destination/result |
| ---------------- | -------------- | ---------- | --------------------- | ------------------ |
| `[CREATE]`       | `[PAGE]`       | `[ROLE]`   | No                    | `[RESULT]`         |
| `[DELETE]`       | `[PAGE]`       | `[ROLE]`   | Yes                   | `[RESULT]`         |
| `[EXPORT]`       | `[PAGE]`       | `[ROLE]`   | No                    | `[RESULT]`         |

## Standard actions

* Create
* View
* Edit
* Save
* Save draft
* Save and continue
* Duplicate
* Archive
* Restore
* Delete
* Cancel
* Back
* Next
* Approve
* Reject
* Retry
* Pause
* Resume
* Import
* Export
* Share
* Download
* Upload
* Filter
* Sort
* Search
* Clear
* Reset
* Select all
* Deselect all

## Destructive actions

For each destructive action define:

* Confirmation message
* Consequence
* Recovery method
* Undo availability
* Required permissions
* Audit log behavior

---

# 11. Form Plan

## `[FORM NAME]`

### Purpose

`[WHAT THE FORM CREATES OR UPDATES]`

### Sections

1. `[SECTION]`
2. `[SECTION]`
3. `[SECTION]`

### Fields

| Field     | Type     | Required     | Validation | Default     |
| --------- | -------- | ------------ | ---------- | ----------- |
| `[FIELD]` | `[TYPE]` | `[YES / NO]` | `[RULE]`   | `[DEFAULT]` |
| `[FIELD]` | `[TYPE]` | `[YES / NO]` | `[RULE]`   | `[DEFAULT]` |

### Form actions

* Save
* Save draft
* Save and add another
* Cancel
* Reset
* Preview

### Validation behavior

* Inline field validation
* Submit-level error summary
* Server-error handling
* Duplicate detection
* Unsaved-changes warning
* Autosave behavior

### Success behavior

`[REDIRECT / TOAST / MODAL / REMAIN ON PAGE]`

### Failure behavior

`[RETRY / PRESERVE INPUT / SHOW ERROR DETAILS]`

---

# 12. Workflow and Wizard Plan

## `[WORKFLOW NAME]`

### Goal

`[FINAL OUTCOME]`

### Steps

| Step | Name     | Purpose     | Required data | Primary action |
| ---- | -------- | ----------- | ------------- | -------------- |
| 1    | `[STEP]` | `[PURPOSE]` | `[DATA]`      | `[ACTION]`     |
| 2    | `[STEP]` | `[PURPOSE]` | `[DATA]`      | `[ACTION]`     |
| 3    | `[STEP]` | `[PURPOSE]` | `[DATA]`      | `[ACTION]`     |

### Navigation behavior

* Back allowed: `[YES / NO]`
* Steps skippable: `[YES / NO]`
* Autosave: `[YES / NO]`
* Resume later: `[YES / NO]`
* Exit warning: `[YES / NO]`

### Completion state

* Success summary
* Created entity link
* Recommended next action
* Secondary next actions

---

# 13. State Matrix

Define the major states for every page and component.

| State             | Trigger                   | UI behavior                | Available actions    |
| ----------------- | ------------------------- | -------------------------- | -------------------- |
| Loading           | Data requested            | Skeleton or spinner        | Cancel if applicable |
| Empty             | No data exists            | Guidance and primary CTA   | Create or import     |
| No results        | Filters return zero items | Clear explanation          | Clear filters        |
| Error             | Request fails             | Error message              | Retry                |
| Partial error     | Some data fails           | Preserve usable data       | Retry failed portion |
| Offline           | Connection unavailable    | Offline banner             | Retry                |
| Permission denied | User lacks access         | Restricted state           | Request access       |
| Archived          | Entity inactive           | Read-only or warning state | Restore              |
| Processing        | Background job active     | Progress state             | Pause or cancel      |
| Success           | Action completes          | Confirmation               | Continue             |

---

# 14. Empty-State Plan

| Page     | Empty-state title | Explanation | Primary CTA | Secondary CTA |
| -------- | ----------------- | ----------- | ----------- | ------------- |
| `[PAGE]` | `[TITLE]`         | `[TEXT]`    | `[ACTION]`  | `[ACTION]`    |
| `[PAGE]` | `[TITLE]`         | `[TEXT]`    | `[ACTION]`  | `[ACTION]`    |

Each empty state should explain:

1. Why the page is empty.
2. What the user can do next.
3. What value the next action provides.

---

# 15. Error-State Plan

| Error type  | User message | Recovery action | Technical details shown |
| ----------- | ------------ | --------------- | ----------------------- |
| Network     | `[MESSAGE]`  | Retry           | No                      |
| Validation  | `[MESSAGE]`  | Correct fields  | Field-specific          |
| Permission  | `[MESSAGE]`  | Request access  | No                      |
| Integration | `[MESSAGE]`  | Reconnect       | Optional                |
| Processing  | `[MESSAGE]`  | Retry job       | Job ID                  |
| Unknown     | `[MESSAGE]`  | Contact support | Reference ID            |

---

# 16. Notification Plan

## Notification channels

* In-app
* Email
* Push
* SMS
* Webhook

## Notification events

| Event     | Audience | Channel     | Action  |
| --------- | -------- | ----------- | ------- |
| `[EVENT]` | `[ROLE]` | `[CHANNEL]` | `[CTA]` |
| `[EVENT]` | `[ROLE]` | `[CHANNEL]` | `[CTA]` |

## Notification controls

* Mark as read
* Mark all as read
* Open related entity
* Dismiss
* Change preferences

---

# 17. Search and Filtering Plan

## Global search

Searchable entities:

* `[ENTITY]`
* `[ENTITY]`
* `[ENTITY]`

Result groups:

* `[GROUP]`
* `[GROUP]`
* `[GROUP]`

Actions:

* Open result
* View all
* Filter by type
* Clear query

## Saved views

* Create saved view
* Rename
* Duplicate
* Share
* Set default
* Delete

---

# 18. Data and Integration Plan

## Data sources

| Data     | Source                          | Refresh method                     | Failure behavior |
| -------- | ------------------------------- | ---------------------------------- | ---------------- |
| `[DATA]` | `[DATABASE / API / USER INPUT]` | `[REAL-TIME / MANUAL / SCHEDULED]` | `[BEHAVIOR]`     |

## Integrations

| Integration | Purpose     | Setup page               | Status states              |
| ----------- | ----------- | ------------------------ | -------------------------- |
| `[SERVICE]` | `[PURPOSE]` | `/settings/integrations` | Connected, error, disabled |

## Background jobs

* Data import
* Data export
* File processing
* Report generation
* AI processing
* Email delivery
* Synchronization

For every job define:

* Queued state
* Active state
* Progress visibility
* Pause behavior
* Cancel behavior
* Retry behavior
* Completion notification
* Failure recovery

---

# 19. Responsive Design Plan

## Breakpoints

| Breakpoint    | Target        |
| ------------- | ------------- |
| `< 640px`     | Mobile        |
| `640–1023px`  | Tablet        |
| `1024–1439px` | Desktop       |
| `1440px+`     | Large desktop |

## Responsive rules

### Navigation

* Desktop: `[FULL SIDEBAR OR HEADER]`
* Tablet: `[COLLAPSED OR DRAWER]`
* Mobile: `[BOTTOM NAV OR DRAWER]`

### Tables

* Desktop: full columns
* Tablet: reduced columns
* Mobile: stacked rows or cards

### Forms

* Desktop: multi-column where useful
* Mobile: single column
* Sticky actions on small screens

### Modals

* Desktop: centered dialog
* Mobile: full-screen dialog or bottom sheet

---

# 20. Design-System Direction

## Visual style

`[MINIMAL / EDITORIAL / PLAYFUL / ENTERPRISE / LUXURY / TECHNICAL]`

## Brand attributes

* `[ATTRIBUTE]`
* `[ATTRIBUTE]`
* `[ATTRIBUTE]`

## Color roles

| Role      | Usage                          |
| --------- | ------------------------------ |
| Primary   | Main actions                   |
| Secondary | Supporting actions             |
| Neutral   | Surfaces and text              |
| Success   | Completed states               |
| Warning   | Attention states               |
| Error     | Destructive and failure states |
| Info      | Informational states           |

## Typography

* Display
* Page title
* Section heading
* Body
* Label
* Caption
* Code or numeric data

## Spacing

Use a consistent spacing scale such as:

`4, 8, 12, 16, 24, 32, 48, 64`

## Shape and elevation

* Border radius: `[VALUE]`
* Card elevation: `[VALUE]`
* Modal elevation: `[VALUE]`
* Border style: `[VALUE]`

---

# 21. Analytics and Tracking Plan

| Event                  | Trigger            | Properties        |
| ---------------------- | ------------------ | ----------------- |
| `page_viewed`          | Page opens         | Page name, role   |
| `[ACTION]_clicked`     | User clicks action | Entity, location  |
| `[ENTITY]_created`     | Create succeeds    | Entity ID, source |
| `[WORKFLOW]_completed` | Workflow finishes  | Duration, result  |
| `error_displayed`      | Error appears      | Error type, page  |

## Core product metrics

* Activation rate
* Workflow completion rate
* Time to first value
* Conversion rate
* Retention
* Feature adoption
* Error rate
* Abandonment rate

---

# 22. MVP Prioritization

## MVP pages

1. `[PAGE]`
2. `[PAGE]`
3. `[PAGE]`
4. `[PAGE]`

## Post-MVP pages

1. `[PAGE]`
2. `[PAGE]`
3. `[PAGE]`

## MVP components

* `[COMPONENT]`
* `[COMPONENT]`
* `[COMPONENT]`

## MVP workflow

```text
[ENTRY]
  ↓
[ACTION]
  ↓
[PROCESS]
  ↓
[RESULT]
```

## Priority criteria

Evaluate each page and feature by:

* User value
* Frequency of use
* Business value
* Technical dependency
* Implementation complexity
* Risk
* Required for core workflow

---

# 23. Page Dependency Matrix

| Page     | Depends on       | Required before      | Shared components |
| -------- | ---------------- | -------------------- | ----------------- |
| `[PAGE]` | `[DATA OR PAGE]` | `[PAGE OR WORKFLOW]` | `[COMPONENTS]`    |
| `[PAGE]` | `[DATA OR PAGE]` | `[PAGE OR WORKFLOW]` | `[COMPONENTS]`    |

---

# 24. Design and Build Checklist

## Page completeness

* `[ ]` Every page has a clear purpose
* `[ ]` Every page has a primary action
* `[ ]` Every button has a defined result
* `[ ]` Every page has loading, empty, and error states
* `[ ]` Every destructive action has confirmation
* `[ ]` Every form has validation behavior
* `[ ]` Every workflow has a completion state
* `[ ]` Role restrictions are documented
* `[ ]` Mobile behavior is defined
* `[ ]` Accessibility requirements are included

## Component completeness

* `[ ]` Reusable components are identified
* `[ ]` Component states are documented
* `[ ]` Component variants are defined
* `[ ]` Keyboard behavior is defined
* `[ ]` Responsive behavior is defined
* `[ ]` Naming is consistent

## Development readiness

* `[ ]` Routes are finalized
* `[ ]` Data requirements are defined
* `[ ]` API dependencies are identified
* `[ ]` Analytics events are listed
* `[ ]` Background jobs are documented
* `[ ]` Permission rules are documented
* `[ ]` MVP scope is separated from future scope

---

# 25. AI Design-Generation Prompt Template

Use this condensed section to convert the completed plan into a prompt for Google Stitch or another UI generator.

```text
Design a responsive [PRODUCT TYPE] named [PRODUCT NAME].

Purpose:
[PRODUCT DESCRIPTION]

Users:
[PRIMARY USER TYPES]

Core workflow:
[ENTRY] → [ACTION] → [PROCESS] → [RESULT]

Visual direction:
[DESIGN STYLE], [COLOR DIRECTION], [TYPOGRAPHY], [SPACING], [COMPONENT DENSITY], [BORDER AND SHADOW STYLE].

Global shell:
[NAVIGATION], [HEADER], [SEARCH], [CREATE ACTION], [NOTIFICATIONS], [PROFILE MENU].

Generate these screens:
1. [PAGE]: [PURPOSE, SECTIONS, PRIMARY ACTIONS]
2. [PAGE]: [PURPOSE, SECTIONS, PRIMARY ACTIONS]
3. [PAGE]: [PURPOSE, SECTIONS, PRIMARY ACTIONS]
4. [PAGE]: [PURPOSE, SECTIONS, PRIMARY ACTIONS]

Reusable components:
[COMPONENT LIST]

Include:
Loading, empty, no-results, success, warning, error, disabled, permission-denied, processing, confirmation, and unsaved-change states.

Responsive behavior:
[DESKTOP BEHAVIOR]
[TABLET BEHAVIOR]
[MOBILE BEHAVIOR]

All visible controls must appear interactive. Use realistic content and maintain one consistent design system across every screen.
```

---

# 26. Fast-Start Planning Input

Complete this shorter section first, then expand the full template.

```text
Product:
[NAME]

Product type:
[TYPE]

Users:
[USER TYPES]

Primary problem:
[PROBLEM]

Primary outcome:
[OUTCOME]

Core entities:
[ENTITIES]

Core workflow:
[WORKFLOW]

Main navigation:
[NAVIGATION ITEMS]

Required pages:
[PAGES]

Primary actions:
[ACTIONS]

User roles:
[ROLES]

Visual style:
[STYLE]

Platforms:
[PLATFORMS]

MVP boundary:
[WHAT MUST BE INCLUDED]
```
