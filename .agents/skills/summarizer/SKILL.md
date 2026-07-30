---
name: summarizer
description: Use this skill whenever the user asks to summarize any content, including text, documents, files, articles, reports, emails, meeting notes, or other written material.
---
- Read and understand the entire content before summarizing.
- Preserve the original meaning and important context.
- Do not add assumptions, opinions, or information that is not present in the source.
- Keep the summary clear, concise, and well-structured.
- Present the summary in bullet points.
- Group related points under appropriate headings whenever applicable.
- Use tables when comparing information or presenting structured data.
- Highlight important numbers, dates, names, and decisions whenever relevant.
- If action items, decisions, risks, or next steps are present, include them as separate sections.
- Adjust the level of detail based on the user's request (brief, standard, or detailed).
- End the response with a **TL;DR** section containing a 2–3 sentence summary.
- Save the final response as a Markdown (`.md`) file.

Response Format:

# Summary
A concise title describing the summarized content.

## Overview
Provide a brief introduction to what the content is about.

## Key Points
Summarize the main information in bullet points.

## Action Items
(Only if applicable.) List any tasks, recommendations, or next steps.

## TL;DR
Provide a 2–3 sentence summary capturing the essence of the content.

Skip any section that is not applicable to the user's request.