# Code

## Role

Act as a senior Python backend developer.

## Task

Implement the functionality described in the provided specification.

Write only the minimum functional code required. Do not write tests or documentation during this stage.

## Context

- The specification is located at `specs/rockets.spec.md`.
- Ask for the specification only if that file is genuinely unavailable.
- The implementation must use:
  - FastAPI for the HTTP API
  - Uvicorn as the ASGI server
  - Pydantic models for request and response validation and schema generation
- FastAPI must expose its generated OpenAPI schema and interactive API documentation through its standard endpoints unless the existing project explicitly configures them differently.

## Python Guidelines

- Follow the Python version and project layout already declared in `pyproject.toml`; otherwise target Python 3.11 or newer.
- Use complete type annotations for public functions, methods, and data structures.
- Avoid `Any` unless it is required at a clearly identified external boundary.
- Use Pydantic `BaseModel` classes for API request and response schemas.
- Represent the rocket range with an enum rather than unrestricted strings.
- Express field constraints in the Pydantic models, including capacity from 1 through 10.
- Use Pydantic v2 conventions when the installed project version is v2; otherwise remain compatible with the version already used by the project.
- Use FastAPI routers, dependency injection, HTTP status codes, and `HTTPException` where they improve clarity without adding unnecessary abstraction.
- Prefer small, cohesive modules and avoid premature layering.
- Avoid mutable default arguments and hidden global state where practical.
- Do not add a database, authentication, or unrelated infrastructure unless required by the specification.
- Do not embed Uvicorn startup logic inside application modules unless the existing project follows that convention; the application must be importable by Uvicorn.

## Environment and Dependency Management

Prefer Poetry and direnv, but do not assume either command is installed.

1. Inspect the repository for `pyproject.toml`, `poetry.lock`, `.python-version`, `.envrc`, and existing dependency-management conventions.
2. Check availability before invoking tools:
   - `command -v poetry`
   - `command -v direnv`
3. If the project already uses Poetry, preserve that workflow and add FastAPI, Uvicorn, and Pydantic through Poetry when needed.
4. If no dependency manager exists and Poetry is available, create the smallest Poetry-compatible project configuration required by the implementation.
5. If Poetry is unavailable, do not install it globally or replace the project's existing environment without explicit permission. Implement the code using the existing environment and report any command that could not be executed.
6. Treat direnv as optional convenience tooling. Use an existing `.envrc` when present; do not make application execution depend on direnv.
7. Never commit virtual environments, secrets, caches, or generated local environment files.

## Steps to Follow

1. **Understand the Specification**
   - Read `specs/rockets.spec.md` and identify every acceptance criterion.
2. **Inspect the Existing Project**
   - Determine the current Python layout, dependency manager, application entry point, and coding conventions.
3. **Break Down the Work**
   - Divide the implementation into the smallest required components.
4. **Prepare a Plan**
   - State the implementation steps without low-level coding details.
5. **Prepare Git**
   - Inspect the current branch and working tree.
   - Preserve all existing user changes; never discard or overwrite them.
   - Commit pre-existing changes separately only when it is safe and clearly intended.
   - Create and switch to a branch named `feat/rockets` if it does not already exist.
6. **Implement the Feature**
   - Write the minimum code necessary to satisfy the specification.
   - Ensure the FastAPI application can be imported and served by Uvicorn.
7. **Perform a Basic Verification**
   - Import the application or start it briefly when the environment permits.
   - Do not create the formal test suite in this stage.

## Output Checklist

- [ ] The implementation is on branch `feat/rockets`.
- [ ] FastAPI, Uvicorn, and Pydantic are used as required.
- [ ] Request and response data are validated with typed Pydantic models.
- [ ] The FastAPI application is importable by Uvicorn.
- [ ] Only the code and dependency files required by the plan were modified or created.
- [ ] Existing unrelated user changes were preserved.