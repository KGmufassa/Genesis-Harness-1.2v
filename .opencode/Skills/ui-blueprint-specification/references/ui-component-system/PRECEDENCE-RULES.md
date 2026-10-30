# Template Precedence Rules

Apply UI architecture guidance in this order:

1. project-specific requirements
2. explicit project overrides
3. selected extensions
4. primary template
5. base template

If two rules conflict, preserve the higher-priority rule and record a `template_deviation` or `override`.

Do not silently replace Stage 1 product scope, Stage 3 architecture, or Stage 4 journey decisions with template defaults.

