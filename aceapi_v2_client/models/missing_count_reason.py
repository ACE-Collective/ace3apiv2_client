from enum import StrEnum


class MissingCountReason(StrEnum):
    FILE = "file"
    MATCH_RECORD = "match_record"
    STORAGE = "storage"

    def __str__(self) -> str:
        return str(self.value)
