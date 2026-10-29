from enum import StrEnum


class LabelRequestVerdict(StrEnum):
    FP = "fp"
    TP = "tp"

    def __str__(self) -> str:
        return str(self.value)
