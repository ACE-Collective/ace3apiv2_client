from enum import StrEnum


class QAStatus(StrEnum):
    MISSING = "missing"
    NOT_QA = "not_qa"
    QA = "qa"

    def __str__(self) -> str:
        return str(self.value)
