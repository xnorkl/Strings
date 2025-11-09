import pytest
from mcp_agent.core.fastagent import FastAgent
from mcp_agent.core.prompt import Prompt
from pathlib import Path
from typing import Any


@pytest.mark.asyncio
async def test_agent_structured_output() -> None:
    """Test agent produces valid structured output."""
    fast = FastAgent("Test App")

    @fast.agent(
        name="test_agent",
        model="playback",  # Use playback model for testing
    )
    async def _() -> None:
        pass

    async with fast.run() as agent:
        # Test structured output
        # Note: This is a simplified test - real testing would require a mock or playback model
        pass  # Placeholder for actual test logic


@pytest.mark.asyncio
async def test_workflow_pipeline() -> None:
    """Test complete workflow execution."""
    fast = FastAgent("Test Workflow")

    @fast.agent(name="step1", instruction="Process input")
    @fast.agent(name="step2", instruction="Transform data")
    @fast.chain(name="pipeline", sequence=["step1", "step2"])
    async def _() -> None:
        pass

    async with fast.run() as agent:
        result = await agent.pipeline.send("test input")
        assert isinstance(result, str)
        assert len(result) > 0