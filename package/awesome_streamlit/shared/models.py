"""Models of app"""
from typing import List, NamedTuple, Optional

_IMAGE_DICT = {" ": "-", "#": ""}


class Tag(NamedTuple):
    """Model of a Tag"""

    name: str

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)


class Author(NamedTuple):
    """Model of an Author"""

    name: str
    url: str

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Resource:
    """Model of a Resource"""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        name: str,
        url: str,
        is_awesome: bool,
        tags: Optional[List[Tag]] = None,
        author: Optional[Author] = None,
    ):
        self.name = name
        self.url = url
        self.is_awesome = is_awesome
        if tags:
            self.tags = tags
        else:
            self.tags = []
        self.author = author

    def to_markdown_bullet(self) -> str:
        """A markdown bullet string

        Returns:
            [str] -- The Resource as a Markdown bullet string
        """
        result = f"- [{self.name}]({self.url})"
        if self.author:
            result += f" by [{self.author.name}]({self.author.url})"
        if self.tags:
            result += " (#" + ", #".join(sorted([tag.name for tag in self.tags])) + ")"

        return result

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Resource(name={self.name})"

    @property
    def screenshot_file(self) -> str:
        """The file name of an associated image of the resource

        Returns:
            str -- The file name of an associated image
        """
        file = f"{self.name.lower()}.png"
        for original, new in _IMAGE_DICT.items():
            file = file.replace(original, new)
        return file
