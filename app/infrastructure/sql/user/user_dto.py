from datetime import datetime
from typing import Union

from sqlalchemy import Column, Integer, String

from app.domain.user import User
from app.infrastructure.sql.database import Base
from app.usecase.user import UserReadModel


def unixtimestamp() -> int:
    return int(datetime.now().timestamp() * 1000)


class userDTO(Base):
    """userDTO is a data transfer object associated with a user entity."""

    __tablename__ = "user"
    id: Union[str, Column] = Column(String, primary_key=True, autoincrement=False)
    created_at: Union[int, Column] = Column(Integer, index=True, nullable=False)
    updated_at: Union[int, Column] = Column(Integer, index=True, nullable=False)

    def to_entity(self) -> User:
        return User(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def to_read_model(self) -> UserReadModel:
        return UserReadModel(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(user: User) -> "userDTO":
        now = unixtimestamp()
        return userDTO(
            id=user.id,
            created_at=now,
            updated_at=now,
        )
