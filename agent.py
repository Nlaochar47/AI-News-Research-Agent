import json
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools

load_dotenv()
print("OpenAI key found:", os.getenv("OPENAI_API_KEY") is not None)
print("Tavily key found:", os.getenv("TAVILY_API_KEY") is not None)

class AINewsReport(BaseModel):
    new_features: List[str]
    new_companies: List[str]
    notable_developments: List[str]
    sources: List[str]

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[TavilyTools(time_range="month", topic="news")],
    output_schema=AINewsReport,
    add_datetime_to_context=True,
    instructions=[
        "You are an AI industry analyst producing a structured report on recent AI developments.",
        "Step 1: Search the web for current information before writing anything. Never answer from memory alone.",
        "Step 2: For every search result, check its publish or last-updated date against today's date (provided in context).",
        "Step 3: If a source is older than 30 days from today, do not use it. Search again with a different query if needed to find a recent one.",
        "Step 4: For 'new_features', report specific new capabilities or product features released by AI companies or models — name the company/product for each one.",
        "Step 5: For 'new_companies', report specific AI companies or products that are new, newly funded, or newly notable — not companies that have been well-known for years.",
        "Step 6: For 'notable_developments', report anything else genuinely interesting or significant in AI right now — research breakthroughs, notable use cases, major announcements. Be specific, not generic.",
        "Step 7: For 'sources', list only the URLs of the sources that passed the 30-day recency check in Step 3.",
        "If you cannot find a verified, recent source for a claim, state that clearly instead of guessing or using an old source.",
    ],
    markdown=False,
)

response = agent.run("Research recent AI industry news: new AI features and capabilities, new AI companies, and other notable AI developments.")

report = response.content

with open("ai_news_report.json", "w") as f:
    json.dump(report.model_dump(), f, indent=2)

print(json.dumps(report.model_dump(), indent=2))