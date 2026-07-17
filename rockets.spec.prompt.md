# Spec

## Role

Act as a software analyst.

## Task

Generate a specification for the functionality described below.

Do not write implementation code or tests; write only the specification.

## Context

- AstroBookings needs an API endpoint for managing rockets.
- Each rocket has:
  - `name`
  - `range`: `suborbital`, `orbital`, `moon`, or `mars`
  - `capacity`: from 1 to 10 passengers
- The target backend stack is:
  - Python
  - FastAPI
  - Uvicorn
  - Pydantic models for data validation and schema generation
- FastAPI will use the Pydantic schemas and Python type annotations to generate the OpenAPI documentation, Swagger UI, and ReDoc.

Do not invent authentication, persistence, identifiers, or additional operations that are not supported by the available context. State any necessary assumptions explicitly, and ask for additional context only when a missing decision materially affects the specification.

### Specification Template

Follow this template for the file `specs/rockets.spec.md`:

````markdown
# Rocket Management API Specification

## Problem Description
- As {role}, I want to **{goal}** so that {reason}.

## Solution Overview
- {Describe the simplest behavioral solution without implementation details.}

## Acceptance Criteria
- [ ] {Acceptance criterion in EARS format.}
````

## Steps to Follow

1. **Define the Problem**
   - Describe the problem with no more than three user stories.
2. **Outline the Solution**
   - Describe the simplest application behavior and required API interactions.
   - Keep the specification technology-independent except for the stated API and validation constraints.
3. **Set Acceptance Criteria**
   - Write no more than nine acceptance criteria.
   - Use EARS format.
   - Cover valid requests, allowed `range` values, capacity boundaries, invalid input, response behavior, and generated API schema visibility when applicable.

## Output Checklist

- [ ] A Markdown file exists at `specs/rockets.spec.md`.
- [ ] The specification contains:
  - Problem Description
  - Solution Overview
  - Acceptance Criteria
- [ ] No implementation code or tests are included.