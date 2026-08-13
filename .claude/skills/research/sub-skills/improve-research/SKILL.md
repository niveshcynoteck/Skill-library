---
name: improve-research

description:  Use this subskill when the user wants to review, improve, or update existing research.
---
# Improve Research

## Workflow

1. Review the complete research before making any suggestions.
2. Check the research against the rules and requirements defined in the main `research` skill.
3. If the user has not clearly stated what they want to improve, ask which sections or aspects they want to focus on.
4. If the requirements are unclear, ask the user for clarification before making changes.
5. Identify weaknesses, missing information, outdated information, unclear explanations, structural issues, and other areas that could be improved.
6. Suggest the required improvements to the user and ask for confirmation before applying them.

## Research Review

Check whether:

- All important aspects of the topic have been covered.
- Each section is properly researched.
- Important information is supported by reliable sources.
- Sources are still valid and relevant.
- Numbers, statistics, dates, and facts are accurate.
- There are any outdated or incorrect claims.
- The explanations are clear and complete.
- The language is simple, correct, and easy to understand.
- The structure is logical and easy to follow.
- The research follows the rules defined in the main `research` skill.
- No important information or requirement has been missed.

## Visual Review

Review all existing visual representations and check:

- Whether the visual correctly represents the information.
- Whether the data shown in the visual is accurate.
- Whether the chosen visualization type is appropriate.
- Whether the visual is placed in the correct section.
- Whether labels, values, legends, and titles are correct and readable.
- Whether a missing visualization could make the research easier to understand.

If a visual needs improvement, suggest the changes and use the `image-maker` skill after user confirmation.

## Saving Changes

Ask the user whether the improved research should:

- Replace the existing research.
- Be saved as a separate version.

If the user chooses a new version:

- Preserve the original research.
- Save the improved research as a new version.

If the user chooses to modify the existing research:

- Confirm the choice with the user.
- Update the existing research files accordingly.

Do not overwrite the original research without the user's confirmation.
