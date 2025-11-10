# Scripts Usage

This directory contains utility scripts that support the fast-agent system, including security checks and deployment tools.

## Available Scripts

- `security_check.py`: Custom security script that performs additional DAST/SAST checks during pre-commit

## Running Scripts

Execute scripts using uv:

```bash
# Run security checks
uv run python -m scripts.security_check

# Or directly
python -m scripts.security_check
```

## GitHub CLI Integration

Use GitHub CLI for script management:

```bash
# Create a new script
gh gist create -d "Utility script" -f script_name.py

# View script history
gh api repos/owner/repo/contents/scripts/script_name.py --jq '.sha'

# Clone scripts from other repositories
gh repo clone username/repo -- --depth 1 --filter=blob:none --sparse
gh sparse-checkout set scripts/
```

## CodeRabbit Integration

CodeRabbit can help improve scripts:

1. Ask for security reviews: "Review this script for security vulnerabilities"
2. Optimize performance: "Improve the performance of this script"
3. Add error handling: "Add comprehensive error handling to this script"
4. Generate documentation: "Create detailed docstrings for all functions in this script"