---
name: python-analyzer

description: |
    Analyze Python code using Python-specific best practices, coding standards, and common conventions.
---

# Python Analyzer

## Standards

While analyzing Python code, consider following:

- The Zen of Python
- Pythonic coding conventions
- PEP 8 (Style Guide)
- PEP 257 (Docstrings)
- Type Hints

## Analyze

Review the code for:

- Naming conventions
- Import organization
- Function and class design
- Code readability
- Maintainability
- Proper use of docstrings
- Type hints
- Exception handling
- Logging
- Context managers (use of `with`)
- List, dictionary, and generator comprehensions
- Async programming (when applicable)
- Project structure (when multiple files are provided)

## Python Version

- Identify the Python version used by the project.
- Verify whether it is currently supported.
- Recommend upgrading to the latest stable Python version if it is not supported.
- Highlight any deprecated syntax or features used.

## Global Interpreter Lock (GIL)

- Determine whether the application is CPU-bound or I/O-bound.
- Check whether the Global Interpreter Lock (GIL) could impact performance.
- Suggest alternatives such as multiprocessing, asynchronous programming, or other suitable approaches when applicable.
- Do not recommend changes unless they provide a measurable benefit.

## Dependencies

- Analyze the project's dependencies, imported modules, and virtual environment configuration.
- Verify that the project is using an appropriate Python virtual environment.
- Generate a complete `requirements.txt` file based on the project's dependencies.
- Before installing, updating, removing, or modifying any dependencies, always ask for the user's permission.
- Identify and report any missing, unused, duplicate, outdated, or unnecessary packages, along with recommendations for cleanup.

## Common Python Issues

Identify issues such as:

- Missing docstrings
- Missing type hints
- Unused imports
- Circular imports
- Excessive nesting
- Duplicate code
- Long functions
- Large classes
- Hardcoded values
- Resource and Credential leaks
