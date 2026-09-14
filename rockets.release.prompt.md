# Release

## Role

Act as a Python software release manager.

## Task

Verify the rockets feature, ensure it is tested, documented, and versioned, and prepare and execute the release of the current AstroBookings version.

## Context

- The current feature branch is `feat/rockets`.
- The implementation must satisfy `specs/rockets.spec.md`.
- The backend uses FastAPI, Uvicorn, and Pydantic.
- Prefer the project's existing Poetry and direnv workflow, but check whether those tools are available before invoking them.

## Release Guidelines

- Preserve unrelated user changes and do not use destructive Git commands.
- Follow the repository's current versioning policy when one exists.
- Otherwise use semantic versioning and select the smallest valid version increment justified by the change.
- Store the project version in `pyproject.toml` or in the existing canonical Python version file used by the repository.
- Use `pytest` for tests.
- Use FastAPI's `TestClient` or an `httpx` ASGI client for endpoint-level tests, following the versions already installed in the project.
- Test observable behavior from the specification rather than internal implementation details.

## Environment Checks

1. Inspect `pyproject.toml`, `poetry.lock`, `.envrc`, the current virtual environment, and the existing test configuration.
2. Check tool availability before use:
   - `command -v poetry`
   - `command -v direnv`
3. If Poetry is available and the project uses it, run project commands through `poetry run`.
4. If Poetry is unavailable, use the active project environment and report commands that could not be executed; do not install Poetry globally without explicit permission.
5. Do not require direnv for tests or release execution.

## Steps to Follow

1. **Verify the Implementation**
   - Read every acceptance criterion in `specs/rockets.spec.md`.
   - Write end-to-end or API-level tests covering those criteria.
   - Include validation of allowed rocket ranges and capacity boundaries.
   - Verify invalid request behavior and response schemas.
   - Verify that the OpenAPI schema includes the rockets endpoint and its Pydantic-derived schemas when required by the specification.
   - Run the full relevant test suite and resolve failures caused by this feature.

2. **Update Version and Documentation**
   - Update the canonical version in `pyproject.toml` or the repository's existing version source according to semantic versioning.
   - Add a dated entry to `CHANGELOG.md`, categorized consistently with the existing changelog.
   - Update `README.md` only where the new endpoint, local startup command, API documentation URL, or workflow must be described.
   - Keep commands consistent with the actual project layout, for example the appropriate equivalent of `poetry run uvicorn <module>:<app> --reload`.

3. **Review the Release State**
   - Confirm the test suite passes.
   - Confirm the working tree contains only intended release changes.
   - Review the final diff and version number.

4. **Commit, Tag, and Merge**
   - Commit release changes with: `chore: prepare release v{version}`.
   - Create an annotated Git tag named `v{version}` with message: `Release v{version}`.
   - Merge `feat/rockets` into `main` using the repository's established merge strategy.
   - Do not force-push, delete branches, or publish remotely unless explicitly requested.

## Output Checklist

- [ ] All acceptance-criteria tests pass.
- [ ] The relevant full test suite passes.
- [ ] The canonical project version was updated.
- [ ] `CHANGELOG.md` was updated.
- [ ] `README.md` was updated when applicable.
- [ ] Release changes were committed as `chore: prepare release v{version}`.
- [ ] Annotated tag `v{version}` was created with message `Release v{version}`.
- [ ] `feat/rockets` was merged into `main`.
- [ ] No remote publication or destructive Git action occurred without explicit authorization.