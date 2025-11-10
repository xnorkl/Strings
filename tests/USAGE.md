# Testing Usage

This directory contains tests for the fast-agent system to ensure code quality and reliability.

## Available Tests

- `test_agents.py`: Tests for agent system functionality and structured output

## Running Tests

Execute tests using uv:

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_agents.py

# Run with verbose output
uv run pytest -v

# Run async tests specifically
uv run pytest -k "asyncio"
```

## Writing New Tests

To create a new test:

1. Add to existing test file or create new one with `test_*.py` naming
2. Use pytest with async support for agent tests
3. Follow existing patterns for structured output testing
4. Ensure tests cover edge cases and error conditions

## Example: Agent Test

```python
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
        # Load test conversation
        from mcp_agent.mcp.prompts import load_prompt_multipart
        
        # Test structured output
        result, _ = await agent.test_agent.structured(
            [Prompt.user("Generate analysis")],
            AnalysisResult,
        )

        assert result is not None
        assert 0.0 <= result.confidence <= 1.0
        assert len(result.recommendations) > 0
```

## GitHub CLI Integration

Use GitHub CLI for testing workflows:

```bash
# Create a test PR
gh pr create --title "test: Add new agent functionality tests" --body "Adds tests for new agent features"

# Check test status on PRs
gh pr list --label test
gh pr view --json title,state,checks

# Run tests across PRs
gh api repos/owner/repo/actions/runs --jq '.workflow_runs[] | .id, .conclusion'
```

## CodeRabbit Integration

CodeRabbit can help with testing:

1. Generate tests: "Create comprehensive tests for this agent class"
2. Improve test coverage: "Add tests for edge cases in this function"
3. Review test quality: "Review these tests for completeness and effectiveness"
4. Generate mock data: "Create realistic test data for this agent"
5. Suggest test improvements: "Suggest better assertions for this test"