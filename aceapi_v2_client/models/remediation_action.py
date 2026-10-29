from enum import StrEnum


class RemediationAction(StrEnum):
    REMOVE = "remove"
    RESTORE = "restore"

    def __str__(self) -> str:
        return str(self.value)
