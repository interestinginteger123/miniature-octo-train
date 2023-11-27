from pydantic import BaseModel, Field

from app.domain.user import (
    UserNotFoundError,
    UserNotCreatedError
)


class ErrorMessageUsersNotFound(BaseModel):
    detail: str = Field(example=UserNotFoundError.message)


class ErrorMessageUnableToCreateuser(BaseModel):
    detail: str = Field(example=UserNotCreatedError.message)
