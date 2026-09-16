# Create Agents Instructions

## Role

Act as a senior Python software engineer.

## Task

Create a concise set of instructions for AI agents working on this project.

## Context

Infer the project structure and tooling only from files that actually exist.

Do not invent technologies, commands, services, or workflows.

### Instructions Template

Create a short file with no more than 100 sentences.

Keep sentences concise, preferably under 100 characters.

Save the result as `AGENTS.md`.

Follow this template:

````markdown
# Agents Instructions

## Product Overview

- {What the product does in 2-3 short sentences.}

## Technical Implementation

### Tech Stack

- Language: **{language and version}**
- Package manager: **{package manager and version, if available}**
- Framework: **{framework and version}**
- ASGI server: **{server and version}**
- Validation: **{validation library and version}**
- Database: **{database or Not configured}**
- Security: **{security strategy or Not configured}**
- Testing: **{testing framework or Not configured}**
- Logging: **{logging approach or Not configured}**

### Development Workflow

```bash
# Set up the project

# Install or sync dependencies

# Run the API

# Run tests

# Deploy the project, if configured
```

### Folder Structure

```text
.                         # Project root
├── AGENTS.md             # Instructions for AI agents
├── README.md             # Main human documentation
├── pyproject.toml        # Python project configuration, if present
├── .envrc                # direnv configuration, if present
├── {other_files}         # Other relevant files
└── {other_folders}/      # Other relevant folders
```

## Environment

- Code and documentation must be in English.
- Chat responses must use the language of the user prompt.
- Prefer concise responses over perfect prose.
- Development may run on Windows with Git Bash or WSL.
- Development may also run on Ubuntu.
- Prefer the project's configured package manager, such as Poetry.
- Use direnv when `.envrc` is present and direnv is available.
- Do not make direnv a requirement for running the application.
- The default Git branch is `master`.
- Agent shells may not inherit the user's full `PATH`.
- Do not modify project configuration solely for agent-specific environment issues.
````

## Steps to Follow

1. **Inspect the Project**

   * Read the main configuration and documentation files.
   * Inspect the source, tests, and relevant project directories.
   * Identify actual technologies and commands in use.
   * Inspect the Makefile, if present, and use only the targets it actually defines.

2. **Summarize the Product**

   * Describe the product in 2-3 short sentences.
   * Base the description on the existing project files.

3. **Describe the Technical Implementation**

   * Include versions when they can be determined reliably.
   * Mark missing components as `Not configured`.

4. **Document the Development Workflow**

  * Use the project's configured package manager for setup and dependency management.
  * Prefer `make test` when that target exists.
  * Otherwise, use the project's configured testing command.

5. **Document the Folder Structure**

   * Show only important files and directories.
   * Keep the tree compact and useful to an AI coding agent.

6. **Write the Instructions**

   * Follow the template.
   * Do not add speculative architecture or recommendations.

## Output Checklist

* [ ] A markdown file named `AGENTS.md` is created.
* [ ] Only technologies present in the project are listed.
* [ ] Development commands reflect the real project configuration.
* [ ] The file contains no more than 100 sentences.

