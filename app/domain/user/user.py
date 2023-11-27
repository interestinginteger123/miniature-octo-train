from typing import Optional


class User:
    """user represents a Unique ID entity."""

    def __init__(
        self,
        id: str,
        created_at: Optional[int] = None,
        updated_at: Optional[int] = None
    ):
        self.id: str = id
        self.created_at: Optional[int] = created_at
        self.updated_at: Optional[int] = updated_at
    
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, User):
            return self.id == o.id

        return False