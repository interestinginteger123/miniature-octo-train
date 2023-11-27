import pytest

from app.domain.user import user


class Testuser:
    def test_constructor_should_create_instance(self):
        user = user(
            id="user01",
        )

        assert user.id == "user01"

    def test_user_entity_should_be_identified_by_id(self):
        user_1 = user(
            id="user01",
        )

        user_2 = user(
            id="user01",
        )

        user_3 = user(
            id="user03",
        )

        assert user_1 == user_2
        assert user_1 != user_3   