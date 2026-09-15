# Add Developer Makefile

## Role

Act as a senior Python software engineer.

## Task

Add a small `Makefile` with a test command for the project.

Do not change application behavior.

## Context

* The project is a Python API.
* The project uses Poetry for dependency management.
* The API uses FastAPI and Uvicorn.
* Tests use pytest.
* Developers may work on Ubuntu, WSL, or Git Bash.
* Dependency installation and application startup should remain explicit Poetry commands.
* The Makefile should provide only a short, memorable test command.

## Requirements

Add this target when supported by the current project:

```bash
make test
```

Expected behavior:

* `make test` runs the complete pytest test suite from the project environment.

Use `.PHONY` targets.

Do not duplicate configuration already present in `pyproject.toml`.

Do not introduce new dependencies.

Do not add `make install` or `make run`; developers should use Poetry directly for those workflows.

## Steps to Follow

1. **Inspect the Project**

   * Identify the Poetry configuration.
   * Identify how the current tests are executed.

2. **Create the Makefile**

   * Add only the supported test target.
   * Keep commands simple and explicit.

3. **Verify**

   * Run `make test`.
   * Verify the existing tests pass.
   * Verify project setup documentation still uses `poetry install`.

4. **Commit**

   * Commit the changes using an appropriate Conventional Commit message.

## Output Checklist

* [ ] A `Makefile` exists at the project root.
* [ ] The Makefile only defines `make test`.
* [ ] `make test` runs pytest from the project environment.
* [ ] Dependency installation remains documented as `poetry install`.
* [ ] Existing tests pass.
* [ ] No unnecessary dependencies are added.
* [ ] Changes are committed using a Conventional Commit message.

## Git

- Create a branch named `chore/dev-makefile` from the current default branch.
- Commit the implementation using a Conventional Commit message.
