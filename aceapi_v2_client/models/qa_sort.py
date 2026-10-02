from enum import StrEnum


class QASort(StrEnum):
    LAST_MATCH = "last_match"
    MATCH_COUNT = "match_count"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
