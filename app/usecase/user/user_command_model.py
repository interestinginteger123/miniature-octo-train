from pydantic import BaseModel, Field

class UserCreateModel(BaseModel):
    """UserCreateModel represents a write model to create a user."""

class UserUpdateModel(BaseModel):
    """UserUpdateModel represents a write model to update the number shelves in a user."""
