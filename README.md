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
- [AWS API Gateway](https://aws.amazon.com/api-gateway/)
- [AWS S3 bucket](https://aws.amazon.com/s3/)
- [GitHub Actions](https://github.com/features/actions)
- [Pytest](https://docs.pytest.org/en/stable/)

## Project Structure

```bash
.
├── README.md
├── .github
│    └── workflows
│        ├── api.yml
│        └── ui.yml
└── services
    ├── src
    │   ├── api
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-311.pyc
    │   │   │   └── tasks.cpython-311.pyc
    │   │   └── tasks.py
    │   ├── config.py
    │   ├── coverage.xml
    │   ├── create_dynamodb_locally.py
    │   ├── docker
    │   │   └── dynamodb
    │   ├── docker-compose.yml
    │   ├── __init__.py
    │   ├── main.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-311.pyc
    │   │   │   └── tasks.cpython-311.pyc
    │   │   └── tasks.py
    │   ├── package.json
    │   ├── poetry.lock
    │   ├── __pycache__
    │   │   ├── config.cpython-311.pyc
    │   │   ├── __init__.cpython-311.pyc
    │   │   ├── main.cpython-311.pyc
    │   │   ├── models.cpython-311.pyc
    │   │   ├── schemas.cpython-311.pyc
    │   │   ├── store.cpython-311.pyc
    │   │   └── tests.cpython-311-pytest-7.4.3.pyc
    │   ├── pyproject.toml
    │   ├── README.md
    │   ├── requirements.txt
    │   ├── resources
    │   │   ├── cognito.yml
    │   │   └── dynamodb.yml
    │   ├── schemas
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-311.pyc
    │   │   │   └── tasks.cpython-311.pyc
    │   │   └── tasks.py
    │   ├── serverless.yml
    │   ├── store.py
    │   └── tests
    │       ├── conftest.py
    │       ├── __init__.py
    │       ├── __pycache__
    │       │   ├── conftest.cpython-311-pytest-7.4.3.pyc
    │       │   ├── __init__.cpython-311.pyc
    │       │   └── test_tasks.cpython-311-pytest-7.4.3.pyc
    │       └── test_tasks.py
    └── src_ui
        ├── index.html
        ├── node_modules
        │   ├── @babel ...
        │   ├── csstype
        │   │   ├── index.d.ts
        │   │   ├── index.js.flow
        │   │   ├── LICENSE
        │   │   ├── package.json
        │   │   └── README.md
        │   ├── @esbuild
        │   │   └── linux-x64
        │   │       ├── bin
        │   │       │   └── esbuild
        │   │       ├── package.json
        │   │       └── README.md
        │   ├── ...
        ├── src
        │   ├── App.vue
        │   ├── assets
        │   │   └── vue.svg
        │   ├── components
        │   │   └── HelloWorld.vue
        │   ├── main.js
        │   └── style.css
        └── vite.config.js
```
