# Strings - A generic agentic engineering framework

This project demonstrates building AI agent systems using fast-agent and the SPARC methodology. It provides working examples of agent patterns, workflows, and MCP integrations that can be adapted for your own projects.

## Summary

The project showcases how to build scalable, maintainable AI agents using the fast-agent framework. It includes various architectural patterns such as chain workflows, evaluator-optimizer systems, and parallel processing. The implementation emphasizes type safety through Pydantic models, follows modern Python best practices, and integrates seamlessly with MCP servers.

## Architecture

### Core Components

1. **FastAgent Framework**: The central orchestrator that manages agents, workflows, and MCP servers
2. **MCP Integration**: Model Context Protocol servers for enhanced functionality (filesystem, web search, etc.)
3. **Type-Safe Models**: Pydantic models for structured data input/output
4. **Configuration Management**: YAML-based configuration with environment variable support

### Agent Patterns Implemented

- **Basic Agents**: Single-purpose agents with specific instructions
- **Workflows**: Chain, parallel, and router patterns for complex orchestrations
- **Evaluator-Optimizer**: Iterative refinement pattern for quality assurance
- **Router Systems**: Task routing to appropriate specialist agents

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
│       ├── evaluator_optimizer.py # Evaluator-optimizer pattern
│       └── settings.py     # Application settings with validation
├── prompts/                # Prompt templates
│   └── analyzer.md         # Example prompt template
├── scripts/                # Utility scripts
│   └── security_check.py   # Security validation script
├── tests/                  # Test files
│   └── test_agents.py      # Agent system tests
├── README.md
└── USAGE.md files          # Detailed usage in respective directories
```

## Dependencies & Tools

- **fast-agent-mcp**: Core agent framework with MCP support
- **Pydantic**: Data validation and settings management
- **uv**: Modern Python packaging and dependency management
- **ruff**: Fast Python linter and formatter
- **mypy**: Static type checking
- **pytest**: Testing framework with async support
- **prospector**: Static code analysis aggregating multiple tools
- **opengrep**: SAST engine to find security issues in code
- **pre-commit**: Git hooks framework to run checks on commit
- **GitHub CLI (gh)**: Command-line tool for GitHub operations and PR management
- **CodeRabbit**: AI-powered code review and development assistance platform

## Usage

This framework is designed to apply the SPARC methodology (Self-critique, Planning, Action, Reflection) to agent development for both new and existing projects:

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies with uv:
   ```bash
   uv sync
   ```

3. Activate the virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

### Configuration

1. Create a `.env` file to store your API keys:
   ```env
   ANTHROPIC_API_KEY=your-anthropic-api-key
   OPENAI_API_KEY=your-openai-api-key
   ```

2. Review or modify the `fastagent.config.yaml` to match your MCP server requirements

### Running Agents

1. **Core Agent Example:**
   ```bash
   uv run python -m src.agents.core
   ```

2. **Workflow Example:**
   ```bash
   uv run python -m src.agents.workflows
   ```

3. **Evaluator-Optimizer Example:**
   ```bash
   uv run python -m src.agents.evaluator_optimizer
   ```

### Applying to New Projects

To apply this framework to a new project:

1. Copy the project structure as a template
2. Modify `fastagent.config.yaml` to match your server requirements
3. Create new agents in `src/agents/` following the patterns
4. Define new prompt templates in `prompts/`
5. Add appropriate tests in `tests/`

### Applying to Existing Projects

To integrate this framework into an existing project:

1. Add the fast-agent dependencies to your existing project
2. Gradually introduce agent patterns starting with simple tasks
3. Use the evaluator-optimizer pattern to improve existing functionality
4. Leverage MCP servers to extend capabilities of your existing system

Detailed usage examples for each directory are available in corresponding USAGE.md files:
- [prompts/USAGE.md](./prompts/USAGE.md) - Prompt templates usage
- [scripts/USAGE.md](./scripts/USAGE.md) - Script utilities usage
- [src/agents/USAGE.md](./src/agents/USAGE.md) - Agent development usage
- [tests/USAGE.md](./tests/USAGE.md) - Testing usage

## Security Best Practices

- Never commit secrets to version control
- Use `fastagent.secrets.yaml` and add to `.gitignore`
- Validate all inputs before processing
- Use environment variables for configuration
- Implement access controls through MCP server filtering

## Deployment

For production deployment, use the provided Dockerfile template:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy application
COPY src/ ./src/
COPY prompts/ ./prompts/
COPY fastagent.config.yaml ./

# Run agent
CMD ["uv", "run", "python", "-m", "agents.main", "--server", "--port", "8080"]
```

Build and run:
```bash
docker build -t fast-agent-system .
docker run -p 8080:8080 -e ANTHROPIC_API_KEY=your-key fast-agent-system
```

## Contributing

1. Follow the type safety practices outlined in the codebase
2. Write comprehensive tests for new functionality
3. Use meaningful variable and function names
4. Document complex logic with clear comments
5. Maintain consistent code formatting using ruff
6. Ensure all security checks pass before submitting pull requests

For detailed development workflows with GitHub CLI and CodeRabbit, see the USAGE.md files in each directory.

## Resources

- [fast-agent Documentation](https://fast-agent.ai/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Anthropic Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Modern Python Development Practices](https://docs.python.org/3/)
- [uv Documentation](https://docs.astral.sh/uv/)
