---
name: research

description: |
    Use this skill whenever the user wants to research a topic in a structured and comprehensive way. This skill is intended to provide well-organized, fact-based, and easy-to-read research reports on various topics.
---

## Research Planning

Before starting the research, create a research plan by identifying the key areas that should be covered.

- Present the proposed research plan to the user as 5–7 concise research topics or questions.
- Organize the topics in a logical order.
- Tailor the plan to the user's request instead of using a fixed template.
- Ask the user to review the proposed plan.
- Allow the user to add, remove, or modify topics.
- Revise the plan based on the user's feedback.
- Continue refining the plan until the user explicitly confirms that they are satisfied with it.
- Do **not** begin the research until the user has approved the research plan.
- Once the plan is approved, proceed with the research.


## Rules 
- Prefer official documentation and official websites whenever available. 
- Verify important information using multiple reliable sources. 
- Do not make up facts or claim anything by your own. 
- Clearly distinguish facts from opinions. 
- Use examples whenever required as they improve understanding. 
- Keep the response well-structured and easy to read. 
- Write in simple English. Prioritize clarity over complexity and explain technical terms when they are necessary.
- Use headings, bullet points, tables, and diagrams (where appropriate) to improve clarity. 
- Include references for important claims. 
- If information cannot be verified, explicitly mention it.

## Tip: Visual Representations

Whenever the research contains information that can be better understood visually (e.g., statistical data, comparisons, workflows, architectures, timelines, processes, or structured data), use the `image-maker` skill.

- Provide the `image-maker` skill with the relevant data and context.
- Allow the `image-maker` skill to recommend the most suitable visualization format.
- Embed the generated visual representation whenever it belongs and improves clarity and understanding.

## Reference Validation

Before presenting the final response:

- Collect every reference or URL used during the research.
- Follow the procedure described in `scripts/validate_links.sh`.
- Use the generated validation report to verify every reference.
- Remove or replace broken or invalid references whenever possible.
- Clearly indicate if a reference could not be validated.
- It is mandatory to validate all links before using them as references in the research.

Save all validated links in a CSV file in the following format as `validated_links.csv`:

| Name | Information | URL | Valid |
|------|-------------|-----|-------|
| Website or document name | Short description of the information obtained from the source | Source URL | TRUE/FALSE |

Use this report to ensure that all references included in the final response are valid and relevant.


## Response Guidelines
- Organize the content into sections with meaningful headings. 
- Highlight the important information and facts.
- Add sections/subsections whenever they improve the explanation.

### For comparison requests 
- Compare items side by side using tables whenever possible. 
- Compare only relevant characteristics instead of every possible feature. 
- Highlight similarities, differences, advantages, disadvantages, and trade-offs. 
- End with a short conclusion explaining when each option is most suitable. 

### For technical topics Consider including topics such as: 
- Architecture 
- Working principle 
- Workflow 
- Features 
- Advantages 
- Limitations 
- Best practices 
- Real-world examples 
- Common mistakes 
- Bibliography

### For non-technical topics Consider including topics such as: |
- Background 
- History 
- Key concepts
- Benefits 
- Challenges 
- Examples 
- Current trends
- References

 **IMPORTANT:** Adapt the report structure to the topic. Do not force every predefined section; include, remove, merge, or introduce sections as appropriate to ensure the research is clear, relevant, and comprehensive.

## Saving the Research 
After generating the response, ask the user whether they want to save it. 
If the user says **Yes**, follow the procedure described in: 
`scripts/save_response.sh` 
The script should: 
- Create an appropriately named folder for the research. 
- Decide the folder and file structure based on the generated response. 
- Create one Markdown file for each major section. 
- Preserve the same hierarchy and headings as the response.