import boto3
import jwt
import pytest
from moto import mock_dynamodb
from starlette.testclient import TestClient

from src.api.tasks import get_task_store
from src.main import app
from src.store import TaskStore


@pytest.fixture
def task_store(dynamodb_table):
    return TaskStore(dynamodb_table)


@pytest.fixture
def client(task_store):
    app.dependency_overrides[get_task_store] = lambda: task_store
    return TestClient(app)


@pytest.fixture
def user_email():
    return "bob@builder.com"


@pytest.fixture
def id_token(user_email):
    return jwt.encode({"cognito:username": user_email}, "secret")


@pytest.fixture
def dynamodb_table():
    with mock_dynamodb():
        client = boto3.client("dynamodb")
        table_name = "test-table"
        client.create_table(
            AttributeDefinitions=[
                {"AttributeName": "PK", "AttributeType": "S"},
                {"AttributeName": "SK", "AttributeType": "S"},
                {"AttributeName": "GS1PK", "AttributeType": "S"},
                {"AttributeName": "GS1SK", "AttributeType": "S"},
            ],
            TableName=table_name,
            KeySchema=[
                {"AttributeName": "PK", "KeyType": "HASH"},
                {"AttributeName": "SK", "KeyType": "RANGE"},
            ],
            BillingMode="PAY_PER_REQUEST",
            GlobalSecondaryIndexes=[
                {
                    "IndexName": "GS1",
                    "KeySchema": [
                        {"AttributeName": "GS1PK", "KeyType": "HASH"},
                        {"AttributeName": "GS1SK", "KeyType": "RANGE"},
                    ],
                    "Projection": {
                        "ProjectionType": "ALL",
                    },
                },
            ],
        )
        yield table_name
