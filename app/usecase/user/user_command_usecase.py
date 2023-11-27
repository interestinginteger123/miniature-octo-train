import uuid

from abc import ABC, abstractmethod
from typing import Optional, cast

from app.domain.user import (
    User,
    UserRepository,
    UserNotFoundError,
    UserAlreadyExistsError
)

from .user_command_model import UserCreateModel, UserUpdateModel
from .user_query_model import UserReadModel


class UserCommandUseCaseUnitOfWork(ABC):
    """UserCommandUseCaseUnitOfWork defines an interface based on Unit of Work pattern."""

    user_repository: UserRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class UserCommandUseCase(ABC):
    """UserCommandUseCase defines a command usecase interface related Book entity."""

    @abstractmethod
    def create_user(self, data: UserCreateModel) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, id: str, data: UserUpdateModel) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_user_by_id(self, id: str):
        raise NotImplementedError


class UserCommandUseCaseImpl(UserCommandUseCase):
    """UserCommandUseCaseImpl implements a command usecases related user entity."""

    def __init__(
        self,
        uow: UserCommandUseCaseUnitOfWork,
    ):
        self.uow: UserCommandUseCaseUnitOfWork = uow

    def create_user(self, data: UserCreateModel) -> Optional[UserReadModel]:
        try:
            _uuid = str(uuid.uuid4())
            user = User(id=_uuid)
            self.uow.user_repository.create(user)
            self.uow.commit()

            created_user = self.uow.user_repository.find_by_id(_uuid)
        except:
            self.uow.rollback()
            raise

        return UserReadModel.from_entity(cast(user, created_user))

    def update_user(self, id: str, data: UserUpdateModel) -> Optional[UserReadModel]:
        try:
            existing_user = self.uow.user_repository.find_by_id(id)
            if existing_user is None:
                raise UserNotFoundError

            user = user(
                id=id
            )

            self.uow.user_repository.update(user)

            updated_user = self.uow.user_repository.find_by_id(user.id)

            self.uow.commit()
        except:
            self.uow.rollback()
            raise

        return UserReadModel.from_entity(cast(user, updated_user))

    def delete_user_by_id(self, id: str):
        try:
            existing_user = self.uow.user_repository.find_by_id(id)
            if existing_user is None:
                raise UserNotFoundError

            self.uow.user_repository.delete_by_id(id)

            self.uow.commit()
        except:
            self.uow.rollback()
            raise
