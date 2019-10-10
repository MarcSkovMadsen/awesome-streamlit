"""Models of app"""
from typing import List, NamedTuple, Optional


class Tag(NamedTuple):
    """Model of a Tag"""

    name: str

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Resource(NamedTuple):
    """Model of a Resource"""

    name: str
    url: str
    app_url: Optional[str] = None
    tags: List[Tag] = []

    def to_markdown_bullet(self) -> str:
        """A markdown bullet string

        Returns:
            [str] -- The Resource as a Markdown bullet string
        """
        result = f"- [{self.name}]({self.url})"
        if self.app_url:
            result += f" [app]({self.app_url})"

        return result
