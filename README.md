# AI News Research Agent

An AI agent that searches for recent AI industry news and puts together a 
structured report, with real sources so the findings can actually be checked.

## The problem

Asking an AI model directly about "recent AI news" runs into two issues: it 
often pulls from outdated training data instead of what's actually happening 
now, and it just returns a wall of text that's hard to reuse or verify. I 
wanted something that searched the live web, stayed genuinely recent, and 
gave me a clean, structured result I could trust.

## What I did

1. Built an agent in Python using Agno, connected to OpenAI's API and a 
   Tavily web search tool.
2. Defined a strict output format with Pydantic (new features, new companies, 
   notable developments, sources) so the result comes back as clean, 
   structured data instead of a paragraph.
3. Ran into a real problem early on: the agent kept including sources from 
   years ago, even though I'd asked it to stay current. Fixed this by 
   filtering the search itself to the last month and giving the agent the 
   actual current date to check sources against, instead of just asking it 
   nicely to "be recent."
4. Fact-checked a few of the agent's claims myself against the actual source 
   articles to confirm the pipeline was working, not just returning 
   plausible-sounding text.

## Tools

Python, OpenAI API, Agno, Tavily

## Example output

```json
{
  "new_features": [
    "Oracle's Moonshot AI Kimi K3 launched with expanded Model Import options and NL2SQL features."
  ],
  "notable_developments": [
    "OpenAI unveiled GPT-6 Astra, showcasing major advances in coding, cybersecurity, and research capabilities."
  ],
  "sources": [
    "https://www.foxbusiness.com/technology/openai-unveils-gpt-6-astra-major-advances-ai-capabilities"
  ]
}
```

## Verification

I checked several of the report's claims against their listed sources, 
including the GPT-6 Astra release, and they held up.

## What's in this repo

- `agent.py`: the full agent script
- `ai_news_report.json`: a real sample output

## Running it

You'll need your own OpenAI and Tavily API keys, set in a `.env` file 
(not included here):
