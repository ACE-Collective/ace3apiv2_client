from enum import StrEnum


class SampleRowLabelType0(StrEnum):
    CONFLICTED = "conflicted"
    FP = "fp"
    TP = "tp"

    def __str__(self) -> str:
        return str(self.value)
