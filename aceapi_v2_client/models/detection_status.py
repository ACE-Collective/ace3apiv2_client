from enum import StrEnum


class DetectionStatus(StrEnum):
    ACTIVE = "active"
    ALL = "all"
    EXPIRED = "expired"

    def __str__(self) -> str:
        return str(self.value)
