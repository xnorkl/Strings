# Prompt Templates Usage

This directory contains prompt templates used by the fast-agent system. Prompt templates define the behavior and capabilities of AI agents in the system.

## Available Prompt Templates

- `analyzer.md`: Template for data analysis agents that extract actionable insights

## Creating New Prompt Templates

To create a new prompt template:

1. Create a new `.md` file in this directory
2. Follow the structure of existing prompts with these sections:
   - **Your Capabilities**: Define the agent's abilities
   - **Context**: Provide relevant context information
   - **Instructions**: Specific steps for the agent to follow
   - **Output Format**: Define expected response format

## GitHub CLI Integration

Use GitHub CLI to manage prompt templates:

```bash
# Create a new prompt template
gh gist create -d "New prompt template" -f new_prompt.md

# Clone a repository containing prompt templates
gh repo clone username/prompt-library
```

## CodeRabbit Integration

CodeRabbit can assist in developing high-quality prompts:

1. Ask for prompt improvements: "Review this prompt for clarity and effectiveness"
2. Generate variations: "Create alternative versions of this prompt"
3. Optimize for specific models: "Adjust this prompt for better Claude performance"