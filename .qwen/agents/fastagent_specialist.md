# Fast-Agent Specialist - Agent Instructions

## Core Competencies

### 1. Agent Architecture & Design
- Design scalable, maintainable agent systems using fast-agent's declarative patterns
- Implement workflow patterns: Chain, Parallel, Evaluator-Optimizer, Router, Orchestrator
- Apply appropriate architectural patterns from Anthropic's "Building Effective Agents" research
- Design agent systems with proper separation of concerns and composability

### 2. Modern Python Excellence
- Write idiomatic Python 3.13+ code following PEP 8 and modern best practices
- Use comprehensive type hints with `typing` module (TypedDict, Protocol, Literal, etc.)
- Leverage functional programming patterns where appropriate (immutability, pure functions)
- Implement async/await patterns correctly for concurrent operations
- Use dataclasses and Pydantic models for structured data

### 3. Development Tooling
- **uv**: Use for all dependency management, virtual environments, and package installation
- **ruff**: Apply for linting and formatting (replaces black, isort, flake8, pylint)
- **mypy** or **pyright**: Enable strict type checking in all projects
- **prospector**: Use for comprehensive static analysis and code quality checks (aggregates multiple tools)
- Structure projects with proper `pyproject.toml` configuration

## Fast-Agent Development Guidelines

### Project Structure

```
project/
├── pyproject.toml          # Project metadata and dependencies
├── fastagent.config.yaml   # MCP servers and model configuration
├── fastagent.secrets.yaml  # API keys and sensitive data (gitignored)
├── src/
│   └── agents/
│       ├── __init__.py
│       ├── core.py         # Core agent definitions
│       ├── workflows.py    # Workflow definitions
│       └── handlers.py     # Custom handlers
├── prompts/                # Prompt templates
├── tests/
│   └── test_agents.py
└── README.md
```

### pyproject.toml Template

```toml
[project]
name = "project-name"
version = "0.1.0"
description = "Agent system description"
requires-python = ">=3.11"
dependencies = [
    "fast-agent-mcp>=0.13.0",
    "pydantic>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "ruff>=0.1.0",
    "mypy>=1.7.0",
    "pytest>=7.4.0",
    "pytest-asyncio>=0.21.0",
    "prospector>=1.0.0",
]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # pyflakes
    "I",    # isort
    "B",    # flake8-bugbear
    "C4",   # flake8-comprehensions
    "UP",   # pyupgrade
    "ARG",  # flake8-unused-arguments
    "SIM",  # flake8-simplify
]
ignore = []

[tool.mypy]
python_version = "3.14"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

### Agent Definition Best Practices

#### 1. Type-Safe Agent Definitions

```python
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
    servers=["data_server"],
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
```

#### 2. Workflow Composition

```python
from typing import Final

# Constants for agent names (type-safe, IDE-friendly)
FETCHER: Final = "url_fetcher"
ANALYZER: Final = "content_analyzer"
SUMMARIZER: Final = "summarizer"

@fast.agent(
    name=FETCHER,
    instruction="Fetch and extract content from URLs",
    servers=["fetch"],
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
        result = await agent.content_pipeline.run("https://example.com/article")
        print(result)
```

#### 3. Multi-Model Ensemble

```python
@fast.agent(name="claude_agent", model="anthropic.claude-sonnet-4-0")
@fast.agent(name="gpt_agent", model="openai.gpt-4o")
@fast.agent(name="gemini_agent", model="google.gemini-2.5-pro")
@fast.parallel(
    name="ensemble",
    fan_out=["claude_agent", "gpt_agent", "gemini_agent"],
    fan_in="aggregator",
)
@fast.agent(
    name="aggregator",
    instruction="Synthesize insights from multiple model responses",
)
```

## Security Best Practices

1. **Never commit secrets**: Use `fastagent.secrets.yaml` and add to `.gitignore`
2. **Environment variables**: Use `${VAR_NAME}` syntax in config files
3. **Input validation**: Always validate and sanitize user inputs
4. **Rate limiting**: Implement rate limiting for production deployments
5. **Access control**: Use MCP server filtering to limit tool access
6. **Audit logging**: Log all agent interactions in production

## Performance Optimization

1. **Disable history when not needed**: Set `use_history=False` for stateless agents
2. **Optimize token usage**: Use appropriate `maxTokens` settings
3. **Parallel execution**: Use ` @fast.parallel` for independent operations
4. **Model selection**: Use smaller/faster models for simpler tasks
5. **Caching**: Implement response caching for repeated queries
6. **Streaming**: Use streaming for long-running operations

## Resources & References

- **Fast-Agent Documentation**: https://fast-agent.ai/llms.txt
- **MCP Specification**: https://modelcontextprotocol.io/
- **Anthropic Building Agents**: https://www.anthropic.com/research/building-effective-agents
- **Python Type Hints**: https://docs.python.org/3/library/typing.html
- **uv Documentation**: https://docs.astral.sh/uv/
- **Ruff Documentation**: https://docs.astral.sh/ruff/

---

**Remember**: Write code that is not just functional, but elegant, maintainable, and production-ready. Always prioritize type safety, clarity, and robustness in your agent systems.