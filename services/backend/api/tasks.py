"""
This module contains the API endpoints for managing tasks.
"""

import uuid
from typing import Union

import jwt
from fastapi import APIRouter, Depends, Header
from starlette import status

from backend.config import Config
from backend.models.tasks import Task
from backend.schemas.tasks import APITask, APITaskList, CloseTask, CreateTask
from backend.store import TaskStore

config = Config()


def get_task_store() -> TaskStore:
    """
    Returns an instance of TaskStore.
    """
    return TaskStore(config.TABLE_NAME, dynamodb_url=config.DYNAMODB_URL)


def get_user_email(authorization: Union[str, None] = Header(default=None)) -> str:
    """
    Decodes the JWT token and returns the user email.
    """
    return jwt.decode(authorization, options={"verify_signature": False})[
        "cognito:username"
    ]


router = APIRouter()


@router.get("/health-check/")
def health_check():
    """
    Endpoint for checking the health of the API.
    """
    return {"message": "OK"}


@router.get("/open-tasks", response_model=APITaskList)
def open_tasks(
    user_email: str = Depends(get_user_email),
    task_store: TaskStore = Depends(get_task_store),
):
    """
    Endpoint for getting a list of open tasks for a user.
    """
    return APITaskList(results=task_store.list_open(owner=user_email))


@router.post(
    "/create-task",
    response_model=APITask,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    parameters: CreateTask,
    user_email: str = Depends(get_user_email),
    task_store: TaskStore = Depends(get_task_store),
):
    """
    Endpoint for creating a new task.
    """
    task = Task.create(id_=uuid.uuid4(), title=parameters.title, owner=user_email)
    task_store.add(task)

    return task


@router.post("/close-task", response_model=APITask)
def close_task(
    parameters: CloseTask,
    user_email: str = Depends(get_user_email),
    task_store: TaskStore = Depends(get_task_store),
):
    """
    Endpoint for closing a task.
    """
    task = task_store.get_by_id(task_id=parameters.id, owner=user_email)
    task.close()
    task_store.add(task)

    return task


@router.get("/closed-tasks", response_model=APITaskList)
def closed_tasks(
    user_email: str = Depends(get_user_email),
    task_store: TaskStore = Depends(get_task_store),
):
    """
    Endpoint for getting a list of closed tasks for a user.
    """
    return APITaskList(results=task_store.list_closed(owner=user_email))
