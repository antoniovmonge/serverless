# Tasks API

## Poetry

```bash
export PATH="$HOME/.local/bin:$PATH"
```

## Install with poetry

```bash
poetry add --group dev moto
```

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
