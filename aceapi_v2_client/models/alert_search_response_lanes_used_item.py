from enum import StrEnum


class AlertSearchResponseLanesUsedItem(StrEnum):
    LEXICAL = "lexical"
    SEMANTIC = "semantic"

    def __str__(self) -> str:
        return str(self.value)
