from enum import StrEnum


class DetectionPointRowOverrideType0(StrEnum):
    FP = "fp"
    TP = "tp"

    def __str__(self) -> str:
        return str(self.value)
