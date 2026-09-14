# Rocket Management API Specification

## Problem Description
- As an AstroBookings operator, I want to **create rocket records** so that launches can be planned against available passenger capacity.
- As an AstroBookings operator, I want to **provide each rocket's mission range** so that the system can distinguish suborbital, orbital, moon, and mars-capable vehicles.
- As an API consumer, I want to **see the rocket request and response schema in generated API documentation** so that I can integrate with the endpoint correctly.

## Solution Overview
- The API provides a rocket management endpoint that accepts rocket details and returns the accepted rocket representation.
- A rocket request includes `name`, `range`, and `capacity`.
- The `range` value is limited to `suborbital`, `orbital`, `moon`, or `mars`.
- The `capacity` value accepts whole passenger counts from 1 through 10.
- Requests that do not satisfy the rocket schema are rejected with a validation error response.
- The API schema exposes the rocket endpoint and model constraints through the generated OpenAPI documentation.

## Acceptance Criteria
- [ ] When an API consumer submits a rocket with a non-empty `name`, an allowed `range`, and a `capacity` from 1 to 10, the API shall accept the request.
- [ ] When a rocket request is accepted, the API shall return a response containing the rocket `name`, `range`, and `capacity`.
- [ ] When an API consumer submits `range` as `suborbital`, `orbital`, `moon`, or `mars`, the API shall treat the range as valid.
- [ ] When an API consumer submits a `range` outside `suborbital`, `orbital`, `moon`, or `mars`, the API shall reject the request with a validation error.
- [ ] When an API consumer submits `capacity` less than 1, the API shall reject the request with a validation error.
- [ ] When an API consumer submits `capacity` greater than 10, the API shall reject the request with a validation error.
- [ ] When an API consumer omits `name`, `range`, or `capacity`, the API shall reject the request with a validation error.
- [ ] When an API consumer submits `capacity` as a non-whole-number value, the API shall reject the request with a validation error.
- [ ] When the generated API schema is viewed, the API shall show the rocket endpoint and the validation constraints for `range` and `capacity`.
