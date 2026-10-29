from enum import StrEnum


class VerdictRequestVerdict(StrEnum):
    FP = "fp"
    TP = "tp"

    def __str__(self) -> str:
        return str(self.value)
