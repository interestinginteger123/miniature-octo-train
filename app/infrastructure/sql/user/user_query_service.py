from typing import List, Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.usecase.user import UserQueryService, UserReadModel

from .user_dto import userDTO


class UserQueryServiceImpl(UserQueryService):
    """UserQueryServiceImpl implements READ operations related user entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> Optional[UserReadModel]:
        try:
            user_dto = self.session.query(userDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return user_dto.to_read_model()

    def find_all(self) -> List[UserReadModel]:
        try:
            user_dtos = (
                self.session.query(userDTO)
                .order_by(userDTO.updated_at)
                .limit(100)
                .all()
            )
        except:
            raise

        if len(user_dtos) == 0:
            return []

        return list(map(lambda user_dto: user_dto.to_read_model(), user_dtos))
