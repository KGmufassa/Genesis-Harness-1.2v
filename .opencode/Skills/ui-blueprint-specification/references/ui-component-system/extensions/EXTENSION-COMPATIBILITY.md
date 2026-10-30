# Extension Compatibility

Use this table before loading individual extension files.

| Extension | Marketing website | SaaS dashboard | Ecommerce storefront | Mobile utility |
| --- | --- | --- | --- | --- |
| `analytics` | conditional | yes | yes | conditional |
| `role-based-access` | no | yes | yes | yes |
| `onboarding` | yes | yes | yes | yes |
| `billing` | no | yes | yes | no |
| `collaboration` | no | yes | conditional | no |
| `messaging` | no | yes | conditional | yes |
| `file-management` | no | yes | conditional | yes |

Compatibility meanings:

- `yes`: compatible when upstream product/workflow evidence justifies it
- `conditional`: compatible only when the product explicitly includes that capability
- `no`: do not apply unless recorded as an explicit project override/deviation

Do not add an extension just because it is compatible. Add it only when Stage 1 workflows, Stage 4 journeys, roles, or feature behavior require it.

