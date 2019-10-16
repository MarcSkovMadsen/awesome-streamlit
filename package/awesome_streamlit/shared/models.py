"""Models of app"""
from typing import List, NamedTuple, Optional


class Tag(NamedTuple):
    """Model of a Tag"""

    name: str

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Author(NamedTuple):
    """Model of an Author"""

    name: str
    url: str

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Resource(NamedTuple):
    """Model of a Resource"""

    name: str
    url: str
    is_awesome: bool
    tags: List[Tag] = []
    author: Optional[Author] = None

    def to_markdown_bullet(self) -> str:
        """A markdown bullet string

        Returns:
            [str] -- The Resource as a Markdown bullet string
        """
        result = f"- [{self.name}]({self.url})"

        return result

    def __str__(self):
        return self.name
