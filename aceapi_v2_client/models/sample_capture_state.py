from enum import StrEnum


class SampleCaptureState(StrEnum):
    MISSING = "missing"
    PENDING = "pending"
    STORED = "stored"

    def __str__(self) -> str:
        return str(self.value)
