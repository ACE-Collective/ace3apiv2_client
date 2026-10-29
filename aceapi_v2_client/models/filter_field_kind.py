from enum import StrEnum


class FilterFieldKind(StrEnum):
    BOOL = "bool"
    DATE_RANGE = "date_range"
    MULTI = "multi"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
