# Add Developer Makefile

## Role

Act as a senior Python software engineer.

## Task

Add a small `Makefile` with common development commands for the project.

Do not change application behavior.

## Context

* The project is a Python API.
* The project uses Poetry for dependency management.
* The API uses FastAPI and Uvicorn.
* Tests use pytest.
* Developers may work on Ubuntu, WSL, or Git Bash.
* The Makefile should provide short, memorable development commands.

## Requirements

Add these targets when supported by the current project:

```bash
make install
make run
make test
```

Expected behavior:

* `make install` installs or synchronizes project dependencies with Poetry.
* `make run` starts the FastAPI application through Uvicorn.
* `make test` runs the complete pytest test suite.

Use `.PHONY` targets.

Do not duplicate configuration already present in `pyproject.toml`.

Do not introduce new dependencies.

Do not add targets for tools that are not configured in the project.

## Steps to Follow

1. **Inspect the Project**

   * Identify the Poetry configuration.
   * Identify the FastAPI application import path.
   * Identify how the current tests are executed.

2. **Create the Makefile**

   * Add only useful development targets.
   * Keep commands simple and explicit.

3. **Verify**

   * Run `make test`.
   * Verify the existing tests pass.
   * Verify `make run` starts the API correctly.

4. **Commit**

   * Commit the changes using an appropriate Conventional Commit message.

## Output Checklist

* [ ] A `Makefile` exists at the project root.
* [ ] `make install` uses the existing Poetry configuration.
* [ ] `make run` starts the FastAPI API.
* [ ] `make test` runs pytest.
* [ ] Existing tests pass.
* [ ] No unnecessary dependencies are added.
* [ ] Changes are committed using a Conventional Commit message.

## Git

- Create a branch named `chore/dev-makefile` from the current default branch.
- Commit the implementation using a Conventional Commit message.