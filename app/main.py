import logging
from logging import config
from typing import Iterator, List

from fastapi import FastAPI, HTTPException, Depends, Form
from sqlalchemy.orm.session import Session

from app.domain.user import (
    UserAlreadyExistsError,
    UsersNotFoundError,
    UserRepository
)

from app.infrastructure.sql.user import (
    UserCommandUseCaseUnitOfWorkImpl,
    UserQueryServiceImpl,
    userRepositoryImpl,
)

from app.infrastructure.sql.database import SessionLocal, create_tables

from app.presentation.schema.user.user_error_message import (
    ErrorMessageUsersNotFound,
)

from app.usecase.user import (
    UserCommandUseCase,
    UserCommandUseCaseImpl,
    UserCommandUseCaseUnitOfWork,
    UserCreateModel,
    UserQueryService,
    UserQueryUserCase,
    UserQueryUserCaseImpl,
    UserReadModel,
    UserUpdateModel,
)

app = FastAPI()
config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

create_tables()

def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        return session
    finally:
        session.close()


def user_query_usecase(session: Session = get_session()) -> UserQueryUserCase:
    user_query_service: UserQueryService = UserQueryServiceImpl(session)
    return UserQueryUserCaseImpl(user_query_service)


def user_command_usecase(session: Session = get_session()) -> UserCommandUseCase:
    user_repository: UserRepository = userRepositoryImpl(session)
    uow: UserCommandUseCaseUnitOfWork = UserCommandUseCaseUnitOfWorkImpl(
        session, user_repository=user_repository
    )
    return UserCommandUseCaseImpl(uow)

def create_user(
    data: UserCreateModel,
    user_command_usecase: UserCommandUseCase = user_command_usecase(),
):
    try:
        user = user_command_usecase.create_user(data)
    except UserAlreadyExistsError as e:
        print(e.message)
    return user


@app.post("/user")
async def create_user_endpoint(
    data: UserCreateModel = Depends(), session: Session = Depends(get_session)
):
    try:
        user = user_command_usecase(session).create_user(data)
        return {"message": "User created successfully", "user": user}
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=e.message)


@app.get("/user")
async def find_users_endpoint(
    session: Session = Depends(get_session)
):
    try:
        find_all = user_query_usecase(session).fetch_users()
        return {"message": "Found all Users", "Users": find_all}
    except UsersNotFoundError as e:
        raise HTTPException(status_code=400, detail=ErrorMessageUsersNotFound)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)