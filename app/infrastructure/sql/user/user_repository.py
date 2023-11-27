from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.domain.user import User, UserRepository
from app.usecase.user import UserCommandUseCaseUnitOfWork

from .user_dto import userDTO


class userRepositoryImpl(UserRepository):
    """UserRepositoryImpl implements CRUD operations related user entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> Optional[User]:
        try:
            user_dto = self.session.query(userDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return user_dto.to_entity()

    def create(self, user: User):
        user_dto = userDTO.from_entity(user)
        try:
            self.session.add(user_dto)
        except:
            raise

class UserCommandUseCaseUnitOfWorkImpl(UserCommandUseCaseUnitOfWork):
    def __init__(
        self,
        session: Session,
        user_repository: UserRepository,
    ):
        self.session: Session = session
        self.user_repository: UserRepository = user_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
