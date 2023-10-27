# Tasks API

## Run tests

```bash
poetry run pytest tests.py
```

## Code Quality

```bash
poetry run black .
poetry run isort . --profile black
poetry run flake8 .
```

## Generate requirements.txt from poetry.lock

```bash
poetry export --with dev --without-hashes --format=requirements.txt > requirements.txt
```
