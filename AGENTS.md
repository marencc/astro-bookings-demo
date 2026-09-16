# Agents Instructions

## Product Overview

- AstroBookings is a backend API for rocket launch bookings.
- It validates rocket ranges, capacities, and public API responses.
- The project is fictional and intended for demonstration and training.

## Technical Implementation

### Tech Stack

- Language: **Python 3.12**
- Package manager: **Poetry**
- Framework: **FastAPI 0.141.1**
- ASGI server: **Uvicorn 0.52.4**
- Validation: **Pydantic 2.13.5**
- Database: **Not configured**
- Security: **Not configured**
- Testing: **pytest 8.3.4 with httpx 0.28.1**
- Logging: **Not configured**

### Development Workflow

```bash
# Set up the project
direnv allow

# Install or sync dependencies
poetry install

# Run the API
poetry run astro-bookings

# Run tests
make test

# Deploy the project, if configured
# Not configured
```

### Folder Structure

```text
.                         # Project root
├── AGENTS.md             # Instructions for AI agents
├── README.md             # Main human documentation
├── pyproject.toml        # Python project and tooling configuration
├── poetry.lock           # Locked Poetry dependencies
├── Makefile              # Development targets
├── .envrc                # Optional direnv configuration
├── specs/                # Product and feature specifications
├── src/                  # Application package
└── tests/                # pytest test suite
```

## Environment

- Code and documentation must be in English.
- Chat responses must use the language of the user prompt.
- Prefer concise responses over perfect prose.
- Development may run on Windows with Git Bash or WSL.
- Development may also run on Ubuntu.
- Prefer Poetry for dependency management.
- Use direnv when `.envrc` is present and direnv is available.
- Do not make direnv a requirement for running the application.
- The README documents `main` as the default Git branch.
- Agent shells may not inherit the user's full `PATH`.
- Do not modify project configuration solely for agent-specific environment issues.
- Keep API changes covered by tests in `tests/`.
- Prefer `make test` for the test suite.
