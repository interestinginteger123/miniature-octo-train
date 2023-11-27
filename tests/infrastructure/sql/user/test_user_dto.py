import pytest
from app.domain import user

from app.domain.user import user
from app.infrastructure.sql.user import userDTO


class TestuserDTO:
    def test_to_read_model_should_create_entity_instance(self):
        user_dto = userDTO(
            id="user_01",
            created_at=1614007224642,
            updated_at=1614007224642,
        )

        user = user_dto.to_read_model()

        assert user.id == "user_01"
        assert user.shelves == 3

    def test_to_entity_should_create_entity_instance(self):
        user_dto = userDTO(
            id="user_01",
            created_at=1614007224642,
            updated_at=1614007224642,
        )

        user = user_dto.to_entity()

        assert user.id == "user_01"

    def test_from_entity_should_create_dto_instance(self):
        user = user(
            id="user_01",
            created_at=1614007224642,
            updated_at=1614007224642
        )

        user_dto = userDTO.from_entity(user)

        assert user_dto.id == "user_01"
