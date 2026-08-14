---
name: research

description: |
    TRIGGER — invoke whenever the user wants a structured, fact-based writeup on a topic rather than a quick answer: "research X", "look into X", "do a deep dive on X", "compare X vs Y", "what are the pros/cons/tradeoffs of X", "give me a report/overview/landscape of X", "investigate X and summarize findings", or any request implying multiple sources should be checked and organized before answering. Also invoke when the user hands over existing research and wants it reviewed, critiqued, or improved: "review this research", "what's wrong with this report", "improve this writeup", "analyze this doc and fix it up".
    SKIP when: the user asks a quick factual question answerable in 1-2 sentences ("what version of X", "does X support Y"); the topic is about THIS codebase/repo.

---

## Research Planning

Before starting the research, create a research plan by identifying the key areas that should be covered.

- Present the proposed research plan to the user as 5–7 concise research topics or questions.
- Organize the topics in a logical order.
- Tailor the plan to the user's request instead of using a fixed template.
- Ask the user to review the proposed plan, and explicitly invite them to contribute their own angles, sources, or priorities — not just react to the proposed list.
- Revise the plan based on the user's feedback.
- Continue refining the plan until the user explicitly confirms that they are satisfied with it.
- Do **not** begin the research until the user has approved the research plan.
- Once the plan is approved, proceed with the research.


## Subskill Delegation

Use the appropriate subskill when the user's request matches its purpose.

### Improve Research

Use the `improve-research` subskill when:

- The user provides existing research and asks to review, improve, update, refine, or correct it.
- The user asks to find weaknesses, missing information, outdated information, or errors in existing research.
- The user asks to improve the structure, sources, language, facts, or visual representations of existing research.
- Do not use the `improve-research` subskill when the user is asking for completely new research.


## Rules 

- Prefer official documentation and official websites whenever available.
- Verify important information using multiple reliable sources.
- Do not make up facts or claim anything by your own.
- Clearly distinguish facts from opinions.
- Research each subtopic thoroughly and provide enough detail to give a complete understanding of it.
- Use examples whenever required as they improve understanding.
- Keep the response well-structured, clear, and easy to read.
- Write in simple, natural English. The response should be easy to understand and should not read like an academic thesis.
- Prioritize clarity and practical understanding over overly formal or complex language.
- Explain technical terms when they are necessary.
- Use headings, bullet points, tables, and diagrams (where appropriate) to improve clarity.
- Include references for important claims.
- If information cannot be verified, explicitly mention it.


## Tip: Visual Representations for Better Understanding

Whenever the research contains information that can be better understood visually (e.g., statistical data, comparisons, workflows, architectures, timelines, processes, or structured data), use the image-maker skill.

Consider visuals not only for numerical data, but also for comparisons, trends, relationships, processes, workflows, architectures, timelines, and other complex or non-numeric information.

- Provide the image-maker skill with the relevant data and context.
- Allow the image-maker skill to recommend the most suitable visualization format.
- Embed the generated visual representation whenever it belongs and improves clarity and understanding.

**IMPORTANT:** Take a visual-first approach when preparing the research. Identify information that can be understood more clearly through diagrams, charts, flowcharts, timelines, or other visualizations. Recommend the appropriate visuals using the image-maker skill and obtain the user's confirmation before generating them.


## Reference Validation

Before presenting the final response:

- Collect every reference or URL used during the research.
- Follow the procedure described in `scripts/validate_links.sh`.
- Use the generated validation report to verify every reference.
- Remove or replace broken or invalid references whenever possible.
- Clearly indicate if a reference could not be validated.
- It is mandatory to validate all links before using them as references in the research.

Save all validated links in a CSV file in the following format as `<research_topic>/validated_links.csv`:

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