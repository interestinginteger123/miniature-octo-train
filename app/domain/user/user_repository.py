from abc import ABC, abstractmethod
from typing import Optional

from app.domain.user import User


class UserRepository(ABC):
    """UserRepository defines a repository interface for user entity."""

    @abstractmethod
    def create(self, user: User) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[User]:
        raise NotImplementedError