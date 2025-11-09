from typing import Final
from mcp_agent.core.fastagent import FastAgent
from mcp_agent.core.request_params import RequestParams

fast = FastAgent("Workflow Example System")

# Constants for agent names (type-safe, IDE-friendly)
FETCHER: Final = "url_fetcher"
ANALYZER: Final = "content_analyzer"
SUMMARIZER: Final = "summarizer"

@fast.agent(
    name=FETCHER,
    instruction="Fetch and extract content from URLs",
    servers=["filesystem"],
    request_params=RequestParams(use_history=False),
)
@fast.agent(
    name=ANALYZER,
    instruction="Analyze content for key themes and entities",
    request_params=RequestParams(temperature=0.3),
)
@fast.agent(
    name=SUMMARIZER,
    instruction="Create concise summaries optimized for social media",
    request_params=RequestParams(maxTokens=512),
)
@fast.chain(
    name="content_pipeline",
    sequence=[FETCHER, ANALYZER, SUMMARIZER],
    cumulative=True,
)
async def main() -> None:
    async with fast.run() as agent:
        result = await agent.content_pipeline.send("https://example.com/article")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())