# Root API Endpoint

## Role

Act as a senior Python backend developer.

## Task

Add a root endpoint (`GET /`) to the AstroBookings FastAPI application.

Do not add unrelated functionality or modify existing API behavior.

## Context

* The application uses FastAPI, Uvicorn, and Pydantic.
* A health status endpoint already exists.
* The root endpoint should provide a minimal welcome response identifying the API.
* The endpoint should be available at `/`.
* FastAPI should include the endpoint in the generated OpenAPI documentation.

### Expected Response

```json
{
  "message": "Welcome to AstroBookings API"
}
```

## Code Guidelines

* Follow the existing project structure and conventions.
* Use Python type annotations.
* Keep the implementation minimal.
* Do not duplicate application or router setup.
* Do not introduce new dependencies.
* Preserve all existing endpoints and behavior.

## Steps to follow

1. **Inspect the Application**

   * Identify where the FastAPI application and existing routes are defined.

2. **Implement the Endpoint**

   * Add a `GET /` endpoint returning the expected response.

3. **Verify**

   * Run the existing test suite.
   * Verify that `/` returns HTTP `200`.
   * Verify that the endpoint appears in the generated OpenAPI schema.

4. **Commit**

   * Commit the changes using an appropriate Conventional Commit message.

## Output Checklist

* [ ] `GET /` is available.
* [ ] The endpoint returns HTTP `200`.
* [ ] The response is:

```json
{
  "message": "Welcome to AstroBookings API"
}
```

* [ ] Existing endpoints continue to work.
* [ ] The endpoint appears in FastAPI's generated API documentation.
* [ ] Changes are committed using a Conventional Commit message.
