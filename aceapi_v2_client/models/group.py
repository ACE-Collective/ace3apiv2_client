from enum import StrEnum


class Group(StrEnum):
    DAY = "day"
    MONTH = "month"

    def __str__(self) -> str:
        return str(self.value)
