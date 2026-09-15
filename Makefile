.PHONY: install run test

install:
	poetry install

run:
	poetry run uvicorn astro_bookings.app:app --host 127.0.0.1 --port 8000 --reload

test:
	poetry run pytest
