from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.user import UserNotFoundError, UserNotFoundError

from .user_query_model import UserReadModel
from .user_query_service import UserQueryService


class UserQueryUserCase(ABC):
    """UserQueryUserCase defines a query usecase interface related user entity."""

    @abstractmethod
    def fetch_user_by_id(self, id: str) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def fetch_users(self) -> List[UserReadModel]:
        raise NotImplementedError


class UserQueryUserCaseImpl(UserQueryUserCase):
    """UserQueryUserCaseImpl implements a query usecases related user entity."""

    def __init__(self, user_query_service: UserQueryService):
        self.user_query_service: UserQueryService = user_query_service

    def fetch_user_by_id(self, id: str) -> Optional[UserReadModel]:
        try:
            user = self.user_query_service.find_by_id(id)
            if user is None:
                raise UserNotFoundError
        except:
            raise

        return user

    def fetch_users(self) -> List[UserReadModel]:
        try:
            users = self.user_query_service.find_all()
        except:
            raise

        return users
