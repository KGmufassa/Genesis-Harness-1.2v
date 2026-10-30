```
                         ┌──────────────────────────────┐
                         │          LANDING PAGE         │
                         │  [Logo] [Nav] [Login][Signup] │
                         │                              │
                         │   [Headline]                 │
                         │   [Subheading]               │
                         │   [CTA: Get Started]         │
                         └──────────────┬───────────────┘
                                        │ Click CTA
                                        ▼
                         ┌──────────────────────────────┐
                         │        AUTH MODAL / PAGE      │
                         │  [Email Input]                │
                         │  [Password Input]             │
                         │  [Login Button]               │
                         │  [Signup Link]                │
                         └──────────────┬───────────────┘
                                        │ Submit Form
                                        ▼
                         ┌──────────────────────────────┐
                         │     AUTH STATE HANDLER        │
                         │ (Validate → API Request)      │
                         └──────────────┬───────────────┘
                              Success   │    Error
                                       ▼
                    ┌──────────────────────────────┐
                    │        DASHBOARD PAGE         │
                    │ [Sidebar] [Top Nav]          │
                    │                              │
                    │  ┌──────────────┐            │
                    │  │ Metric Card  │            │
                    │  └──────────────┘            │
                    │                              │
                    │  [Main Content Area]         │
                    └──────────────┬───────────────┘
                                   │
                  ┌────────────────┼────────────────┐
                  ▼                                 ▼
      ┌──────────────────────┐         ┌──────────────────────┐
      │   CREATE ACTION BTN  │         │   NAVIGATION CLICK   │
      │   [New Item +]       │         │   [Menu / Route]     │
      └──────────┬───────────┘         └──────────┬───────────┘
                 │                                │
                 ▼                                ▼
      ┌──────────────────────┐         ┌──────────────────────┐
      │   FORM MODAL / PAGE  │         │   NEW PAGE LOAD      │
      │ [Input Fields]       │         │ [Different View]     │
      │ [Submit Button]      │         └──────────┬───────────┘
      └──────────┬───────────┘                    │
                 │ Submit                          │
                 ▼                                 ▼
      ┌──────────────────────┐         ┌──────────────────────┐
      │   LOCAL STATE UPDATE │         │   DATA FETCH         │
      │ (Form → State)       │         │ (API Call)           │
      └──────────┬───────────┘         └──────────┬───────────┘
                 │                                │
                 ▼                                ▼
      ┌──────────────────────┐         ┌──────────────────────┐
      │   API REQUEST        │         │   API RESPONSE       │
      │ (POST /items)        │         │ (Data Returned)      │
      └──────────┬───────────┘         └──────────┬───────────┘
                 │                                │
                 └──────────────┬─────────────────┘
                                ▼
                     ┌──────────────────────────────┐
                     │   GLOBAL STATE UPDATE         │
                     │ (Store / Cache Updated)       │
                     └──────────────┬───────────────┘
                                    │
                                    ▼
                     ┌──────────────────────────────┐
                     │      UI RE-RENDER            │
                     │ (Updated Dashboard View)     │
                     └──────────────────────────────┘
```
