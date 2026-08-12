# Definitions

## Non-Agentic AI
Non-agentic AI refers to systems that require a direct instruction for **every** task and act as passive, responsive tools. Common shapes include a single prompt-and-response LLM call, a classifier, or a rule-based automation script — input goes in, output comes out, and the surrounding application code decides what happens next. These systems do not set their own sub-goals or take independent action in the world.

## Agentic AI
According to MIT Sloan, agentic AI refers to **"autonomous or semi-autonomous systems that perceive, reason, and act in digital environments to achieve goals on behalf of human principals."** IBM similarly describes it as AI that can **"accomplish a specific goal with limited supervision,"** using AI agents — models that mimic human decision-making to solve problems in real time.

Unlike a chatbot that only generates text for a human to act on, agentic AI:
- Plans multi-step sequences of actions
- Calls real tools (APIs, files, browsers, code execution)
- Observes the results of its actions
- Adjusts its plan and loops until the goal is achieved

Wikipedia frames the key distinction as **autonomy and multi-step execution**: traditional tools like Siri or Alexa "lacked the general-purpose reasoning ability of later agents run by LLMs," while modern agentic AI chains multiple actions toward complex objectives instead of executing a single predetermined workflow.

**Important nuance:** Multiple sources emphasize that "agenticness is a spectrum, not a yes/no" — systems fall along a continuum rather than a strict binary (see [05-autonomy-spectrum.md](05-autonomy-spectrum.md)).
