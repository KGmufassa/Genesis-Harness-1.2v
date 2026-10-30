---
pattern_id: notifications
pattern_type: interaction
aliases: [toasts, alerts, banners]
use_when: [async feedback, status changes, system events]
avoid_when: [critical blocking decisions without modal or inline context]
requires: [severity, dismissal behavior, screen reader announcement]
---

# Interaction Pattern — notifications

Define notification channel, trigger event, audience, CTA, read/dismiss controls, preference controls, and related-entity navigation.
