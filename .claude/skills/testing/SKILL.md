---
name: testing

description: |
    Use this skill whenever a project's testing strategy needs to be analyzed. Review existing tests, identify missing tests, evaluate code coverage, and recommend improvements.
---

# Testing Analysis

## Workflow

1. Analyze the project's testing strategy.
2. Generate the testing analysis.
3. Generate supporting testing artifacts.
4. Use the `image-maker` skill whenever visual representations improve the understanding of the testing analysis.
5. Save the generated reports.

## Testing Analysis

Analyze the project's testing strategy.

Review:

- Existing test scripts.
- Test quality and maintainability.
- Test coverage.
- Untested modules and functions.
- Missing edge-case tests.
- Test organization.

If no tests exist:

- Recommend what should be tested.
- Suggest suitable test cases.
- Identify critical components that should be covered first.

Provide in the report:

- Test analysis.
- Coverage assessment.
- Suggestions for improving test quality.
- Recommendations for increasing code coverage.
- Additional test cases that should be implemented.

Additionally:

- Generate an HTML code coverage report for browser-based viewing whenever supported.
- Include the location or link to the generated HTML coverage report in the Markdown testing report.

## Visual Representation

Use the `image-maker` skill whenever a visual representation can improve the clarity and understanding of the testing analysis.

Examples include:

- Code coverage summary
- Coverage by module
- Coverage heatmaps
- Covered vs. uncovered code
- Test execution flow
- Test architecture
- Test statistics

Use visual representations when they provide meaningful insights and make the testing results easier to understand. Do not generate unnecessary visuals.


## Saving the Report

If this skill is invoked by another skill, save the testing report and all generated artifacts in the directory provided by the calling skill.

Otherwise, ask the user where they would like to save the generated reports.

The generated files should include:

- `testing_report.md`
- `coverage.html` (when supported)
- Any generated visual assets