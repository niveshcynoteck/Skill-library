---
name: code-analyzer

description: |
    Use this skill whenever the user wants to analyze existing source code. This skill identifies the programming language and delegates the analysis to the appropriate language-specific analyzer.
---

# Code Analyzer

## Workflow

1. Detect the programming language of the provided code.
2. Verify that the language is supported.
3. Load the corresponding language-specific analyzer.
4. Perform the analysis using the language-specific rules.
5. If code execution is required, execute it in an isolated sandbox using a temporary working directory to avoid modifying the original project.
6. Invoke the `testing` skill to perform a testing analysis of the project.
7. Use the `image-maker` skill whenever visual representations improve the understanding of the analysis.
8. Present and save the findings in a structured report.

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

- Do not analyze data files (e.g., CSV, TSV, Excel), binary files, media files, archives, or other non-code assets by default. Ask the user for permission before including them in the analysis, unless they are explicitly required to understand the code.

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

## Testing Skill Integration

Use the `testing` skill whenever test files, test directories, or testing configurations are present in the project.

The `testing` skill is responsible for:

- Analyzing the project's testing strategy.
- Evaluating test quality and maintainability.
- Performing code coverage analysis.
- Identifying missing tests.
- Recommending additional test cases.
- Generating testing-related visualizations.
- Generating HTML coverage reports (when supported).

Pass the project's test files and testing-related information to the `testing` skill.

Provide the analysis directory path to the `testing` skill and instruct it to save all generated reports and artifacts within:

analysis_report_[project_name]/testing/

After the testing skill completes its work:

- Include a summary of the testing findings in the main analysis report.
- Include a link to the testing report.
- Include a link to the HTML coverage report (if generated).
- Include links to any testing-related visual assets.

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

Actively identify opportunities to explain concepts visually. Generate diagrams that improve understanding.

## Report Organization

Save the analysis inside:

analysis_report_[project_name]/

The directory should contain:

- `analysis_report_of_[project_name].md`
- `testing/`
- `assets/`

The main Markdown report should:

- Summarize the complete analysis.
- Link to the Testing Analysis report generated by the `testing` skill.
- Link to all generated visual assets.
- Link to any additional generated reports.

## Response Guidelines

Organize the report using relevant sections such as:

- Overview
- Architecture
- Code Flow
- Findings
- Code Quality
- Dependency Analysis
- Performance Analysis
- Security
- Testing Analysis (link to the testing report)
- Suggestions
- Conclusion
