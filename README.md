
# AstroBookings 

A **backend API** for offering bookings for rocket launches.
- Launches are scheduled for specific rockets, with pricing and minimum passenger thresholds.
- Rockets have limited seats; launch requests are validated against rocket capacity.
- Launch status lifecycle: scheduled → confirmed → successful, or cancellation/suspension paths.
- A customer is identified by their email address and has a name and phone number.
- One customer can book multiple seats on a launch but cannot exceed the available seats.
- Customers are billed upon booking, and payments are processed through a mock gateway.

> [!WARNING]
> AstroBookings is a fictional space travel company.
> The system is designed for demonstration and training purposes. 
> Not for production use; no security or database is required at the initial stage.

---
[Repository at GitHub](https://github.com/marencc/astro-bookings-demo)
**Author**: [Maren Calleja](https://github.com/marencc/)
**Original proprosal from** [Alberto Basalo](https://albertobasalo.dev)
**From IT Trainning** [Repository at GitHub](https://github.com/AlbertoBasaloLabs/astro-bookings-demo)
- Default branch: `main`

## Development

This project uses [Poetry](https://python-poetry.org/) for dependency and package
management.

```bash
poetry install
poetry run astro-bookings
poetry run pytest
poetry run ruff check .
```

The API runs at `http://127.0.0.1:8000` by default.

- Health status: `GET /health`
- Swagger UI: `GET /docs`
- ReDoc: `GET /redoc`
- OpenAPI schema: `GET /openapi.json`

This repository includes a `.envrc` for optional direnv integration:

```bash
direnv allow
```
