from enum import StrEnum


class AlertSearchResultOutLanesItem(StrEnum):
    LEXICAL = "lexical"
    SEMANTIC = "semantic"

    def __str__(self) -> str:
        return str(self.value)
