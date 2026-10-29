from enum import StrEnum


class DetectionPointRowVerdictType0(StrEnum):
    FP = "fp"
    TP = "tp"

    def __str__(self) -> str:
        return str(self.value)
