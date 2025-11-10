---
name: fast-agent-specialist
description: Agentic engineering specialist using fast-agent.
color: Automatic Color
---

# Fast-Agent + SPARC Reference Implementation

Reference implementation showing AI agent systems with fast-agent and SPARC methodology. Provides working examples of agent patterns, workflows, and MCP integrations.

## Summary

Demonstrates SPARC-driven development (Specification → Pseudocode → Architecture → Refinement → Completion) with fast-agent orchestration. Includes agent patterns, type-safe models, and terminal-based workflows.

## Architecture

**Core Components:**
- FastAgent Framework: Manages agents, workflows, and MCP servers
- MCP Integration: Protocol servers for filesystem, web search, etc.
- Type-Safe Models: Pydantic models for structured I/O
- Configuration: YAML-based with environment variables

**Agent Patterns:**
- Basic agents with specific instructions
- Workflows: chain, parallel, router patterns
- Evaluator-optimizer for quality assurance
- SPARC phase-specific agents

**Structure:**
```
project/
├── pyproject.toml
├── fastagent.config.yaml
├── src/agents/
│   ├── core.py
│   ├── workflows.py
│   └── evaluator_optimizer.py
├── prompts/
└── tests/
```

## Dependencies

- fast-agent-mcp, Pydantic, uv, ruff, mypy, pytest, prospector, opengrep, pre-commit

## Usage

**Installation:**
```bash
git clone <repository-url>
cd <repository-name>
uv sync
source .venv/bin/activate
```

**Configuration:**
```env
# .env
ANTHROPIC_API_KEY=your-key
OPENAI_API_KEY=your-key
```

**Running:**
```bash
uv run python -m src.agents.core
uv run python -m src.agents.workflows
uv run python -m src.agents.evaluator_optimizer
```

**Development:**
```bash
uv run ruff format .
uv run ruff check . --fix
uv run mypy src/
uv run pytest
```

## SPARC Methodology

Maps phases to agent workflows:
- **Specification**: Requirements clarification
- **Pseudocode**: Logic design
- **Architecture**: Component design
- **Refinement**: Implementation
- **Completion**: Quality assurance

Each phase has dedicated configurations and prompts in `prompts/`.

## Security

Automated checks with OpenGrep (SAST), Prospector, and pre-commit hooks.

Detects:
- Hardcoded secrets
- Insecure configurations
- Weak cryptography
- Injection vulnerabilities

```bash
pre-commit run --all-files
uv run prospector
```

**Best Practices:**
- Never commit secrets
- Use `.env` for keys
- Validate inputs
- Use MCP server filtering

## Deployment

**Docker:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY src/ ./src/
COPY prompts/ ./prompts/
COPY fastagent.config.yaml ./
CMD ["uv", "run", "python", "-m", "agents.main", "--server", "--port", "8080"]
```

```bash
docker build -t fast-agent-system .
docker run -p 8080:8080 -e ANTHROPIC_API_KEY=key fast-agent-system
```

## Contributing

1. Follow type safety practices
2. Write tests for new functionality
3. Use meaningful names
4. Document complex logic
5. Format with ruff
6. Pass security checks

## Resources

- [fast-agent](https://fast-agent.ai/)
- [MCP](https://modelcontextprotocol.io/)
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [uv](https://docs.astral.sh/uv/)
