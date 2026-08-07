---
name: image-maker

description: |
    Use this skill whenever the user wants to create a visual representation of information such as statistical data, tables, workflows, architectures, processes, comparisons, or other structured content.
---

# Image Maker
## Rules 
- Gain a full understanding of the given content before generating the visualization. 
- Choose the most suitable visualization format based on the content. 
- Keep the visualization simple, clear, and easy to understand. 
- If the visualization becomes too complex, break it down into multiple smaller, logically grouped sections within the same diagram to improve clarity and make it easier to understand.
- Highlight the most important information. 
- Do not add data or facts by yourself. 
- Use meaningful labels, legends and titles. 
- The text part of the visualization should be clear and readable.
- Ensure the visualization accurately represents the given information.

- Depending on the content, choose the best format for the visualization. That can be :
	- Mermaid diagram
	- Bar chart 
	- Pie chart 
	- Line chart
	- Sequence diagram 
	- Architecture diagram

**Important:**
- Ensure all text within generated visuals is clearly visible, well-spaced, and distinct. Prevent text overlap, crowding, or placement that makes labels difficult to read.

- Select the visualization that makes the information easiest to understand. Multiple visualizations may be generated if they improve clarity.

## Validation

After generating the visualization:

- Verify that the generated image correctly represents the provided data and information.
- Check that all text, labels, legends, and titles are clearly visible and readable.
- Verify that there is no text overlap, clipping, crowding, or missing information.
- Check that the diagram structure and relationships are logically correct.
- If any issue is found, regenerate or revise the visualization before presenting it to the user.
- Do not present a visualization that is unclear, unreadable, or incorrectly represents the provided information.

## Guidelines for Output format Selection
- Recommend the best output format (e.g., SVG, PNG, HTML, Markdown, PDF) based on the content and use case.
- Briefly justify the recommendation.
Obtain the user's confirmation before generating the output. 
- If the user prefers a different format, honor their choice.

