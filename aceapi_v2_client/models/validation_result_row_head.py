from enum import StrEnum


class ValidationResultRowHead(StrEnum):
    ERROR = "error"
    MATCH = "match"
    MISS = "miss"

    def __str__(self) -> str:
        return str(self.value)
