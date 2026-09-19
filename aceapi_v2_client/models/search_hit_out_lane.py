from enum import StrEnum


class SearchHitOutLane(StrEnum):
    LEXICAL = "lexical"
    SEMANTIC = "semantic"

    def __str__(self) -> str:
        return str(self.value)
