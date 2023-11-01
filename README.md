# Serverless APP with FastAPI, Vue and DynamoDB

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This is a simple app created to get familiar with Serverless Framework using FastAPI, Vue and DynamoDB.

The application is at a very early stage. It will be updated and developed in the next days.

## Development

This app aims to follow Test Driven Development (TDD) principles. The tests are written using Pytest.

## Stack

- [Serverless Framework](https://www.serverless.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Vue](https://vuejs.org/)
- [DynamoDB](https://aws.amazon.com/dynamodb/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Cognito](https://aws.amazon.com/cognito/)
- [GitHub Actions](https://github.com/features/actions)
- [Pytest](https://docs.pytest.org/en/stable/)

## Folder Structure

```bash
.
├── .github
│   └── workflows
│       └── api.yml
├── .gitignore
└── services
    └── src
        ├── api
        │   ├── __init__.py
        │   └── tasks.py
        ├── models
        │   ├── __init__.py
        │   └── tasks.py
        ├── resources
        │   ├── cognito.yml
        │   └── dynamodb.yml
        ├── schemas
        │   ├── __init__.py
        │   └── tasks.py
        ├── tests
        │   ├── __init__.py
        │   ├── conftest.py
        │   └── test_tasks.py
        ├── __init__.py
        ├── .env.development
        ├── .flake8
        ├── config.py
        ├── create_dynamodb_locally.py
        ├── docker-compose.yml
        ├── main.py
        ├── package.json
        ├── poetry.lock
        ├── pyproject.toml
        ├── serverless.yml
        └── store.py
```
