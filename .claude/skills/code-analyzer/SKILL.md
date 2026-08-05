---
name: code-analyzer

description: |
    Use this skill whenever the user wants to analyze existing source code. This skill identifies the programming language and delegates the analysis to the appropriate language-specific analyzer.
---

# Code Analyzer

## Workflow

1. Detect the programming language of the provided code.
2. Verify that the language is supported.
3. Load the corresponding language analyzer.
4. Perform the analysis using the language-specific rules.
5. If code execution is required, execute it in an isolated sandbox using a temporary working directory to avoid modifying the original project.
6. Use the `image-maker` skill whenever visual representations improve the analysis.
7. Present the findings in a structured report.
8. Save the report in Markdown format as `analysis_report_of_[project_name].md`.

## Supported Languages

Only analyze languages that have an analyzer under the `languages/` directory.

If the language is not supported:

- Inform the user that the language is currently unsupported.
- Do not attempt to analyze it.

## General Analysis Rules

Regardless of the programming language:

- Understand the purpose of the code before analyzing it.
- Evaluate readability and maintainability.
- Identify code smells and potential issues.
- Review the overall architecture when multiple files are provided.
- Highlight possible performance concerns.
- Highlight possible security concerns.
- Distinguish confirmed issues from recommendations.
- Clearly explain the reasoning behind every observation.
- Write the analysis in clear, simple English so that it can be understood by both technical and non-technical readers.
- Use examples whenever they improve understanding.
- Do not assume missing code or project context.

## General File Handling Rules

- Skip data files (e.g., CSV, TSV, Excel), binary files, media files, archives, and other non-visual assets unless they are explicitly required for the analysis of the code.

## Execution Environment

If execution is required:

- Create a temporary working directory separate from the original project.
- Execute the code only within this isolated environment.
- Ensure the original source code and project files remain unchanged.
- Clean up all temporary files after the analysis is complete.


## Dependency Analysis

Analyze the project's dependencies and environment.

- Identify required, missing, unused, duplicate, outdated, or unnecessary dependencies.
- Recommend appropriate dependency updates or cleanup.
- Install missing dependencies only after obtaining the user's permission.
- Include all dependency findings and recommendations in the final report.

## Testing Analysis

Analyze the project's testing strategy.

Review:

- Existing test scripts.
- Test quality and maintainability.
- Test coverage.
- Untested modules and functions.
- Missing edge-case tests.
- Test organization.

Provide in the report:

- Test analysis.
- Coverage assessment.
- Suggestions for improving test quality.
- Recommendations for increasing code coverage.
- Additional test cases that should be implemented.

Additionally,
- Generate an HTML code coverage report for browser-based viewing.
- Include the location or link to the generated HTML report in the Markdown analysis report.

## Performance Analysis

Analyze the application's performance characteristics.

Review:

- Execution time.
- Memory usage.
- Inefficient algorithms.
- Resource utilization.
- Scalability concerns.

Recommend optimizations where appropriate, including:

- Better algorithms or data structures.
- Caching strategies.
- Lazy evaluation.
- Multithreading.
- Multiprocessing.
- Asynchronous programming (when applicable).

Only recommend optimizations when they provide a measurable benefit.

## Image Inclusion 

Use the `image-maker` skill whenever a visual representation improves the understanding of the analysis.

Examples include:

- Code flow
- Project architecture
- Class diagrams
- Function call hierarchy
- Performance statistics
- Any other structured information that is easier to understand visually

Choose only the diagrams that add value. Do not generate unnecessary visuals.

## Response Guidelines

Organize the report using relevant sections such as:

- Overview
- Architecture
- Code Flow
- Findings
- Code Quality
- Dependency Analysis
- Testing Analysis
- Performance Analysis
- Security
- Suggestions
- Conclusion
