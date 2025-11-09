import asyncio
from pathlib import Path
from typing import Literal, TypedDict
from pydantic import BaseModel
from mcp_agent.core.fastagent import FastAgent
from mcp_agent.core.prompt import Prompt
from mcp_agent.core.request_params import RequestParams

# Create the application instance
fast = FastAgent("Production Agent System")

# Define structured response models
class AnalysisResult(BaseModel):
    """Type-safe analysis output."""
    summary: str
    confidence: float
    recommendations: list[str]
    metadata: dict[str, str | int | float]


# Define agent with comprehensive type hints
@fast.agent(
    name="analyzer",
    instruction=Path("./prompts/analyzer.md"),
    servers=["filesystem"],
    model="anthropic.claude-sonnet-4-0",
    request_params=RequestParams(
        maxTokens=4096,
        temperature=0.7,
        use_history=True,
        max_iterations=20,
    ),
)
async def main() -> None:
    """Run the agent system."""
    async with fast.run() as agent:
        # Type-safe structured output
        result, message = await agent.analyzer.structured(
            [Prompt.user("Analyze the dataset")],
            AnalysisResult
        )

        if result is not None:
            print(f"Confidence: {result.confidence:.2%}")
            for rec in result.recommendations:
                print(f"- {rec}")


if __name__ == "__main__":
    asyncio.run(main())