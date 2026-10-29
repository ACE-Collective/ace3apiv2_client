from enum import StrEnum


class ExpectationRequestState(StrEnum):
    EXPECTED = "expected"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
