from typing import cast

from pydantic import BaseModel, Field

from app.domain.user import user


class UserReadModel(BaseModel):
    """UserReadModel represents data structure as a read model."""
    id: str = Field(example="user1")
    created_at: int = Field(example=1136214245000)
    updated_at: int = Field(example=1136214245000)

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(user: user) -> "UserReadModel":
        return UserReadModel(
            id=user.id,
            created_at=cast(int, user.created_at),
            updated_at=cast(int, user.updated_at)
        )
