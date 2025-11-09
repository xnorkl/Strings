from mcp_agent.core.fastagent import FastAgent
from mcp_agent.core.request_params import RequestParams
from pydantic import BaseModel
from typing import List


fast = FastAgent("Documentation Generator System")


class DocumentationResult(BaseModel):
    """Structured documentation output."""
    title: str
    content: str
    sections: List[str]
    quality_score: float


@fast.agent(
    name="content_generator",
    instruction="Generate high-quality technical documentation with examples",
    servers=["filesystem"],
    use_history=False,
)
@fast.agent(
    name="quality_evaluator",
    instruction="""
    Evaluate content quality on:
    - Technical accuracy
    - Clarity and readability
    - Completeness
    - Code example quality

    Rate as: EXCELLENT, GOOD, FAIR, or POOR
    Provide specific, actionable feedback for improvement.
    """,
    request_params=RequestParams(temperature=0.2),  # Lower temp for consistent evaluation
)
@fast.evaluator_optimizer(
    name="documentation_system",
    generator="content_generator",
    evaluator="quality_evaluator",
    min_rating="EXCELLENT",
    max_refinements=3,
)
async def main() -> None:
    async with fast.run() as agent:
        docs = await agent.documentation_system.send(
            "Create documentation for a Python API endpoint"
        )
        print(docs)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())