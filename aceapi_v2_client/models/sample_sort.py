from enum import StrEnum


class SampleSort(StrEnum):
    CAPTURE_COUNT = "capture_count"
    FIRST_CAPTURED = "first_captured"
    LABEL = "label"
    LAST_CAPTURED = "last_captured"
    RULE = "rule"
    SHA256 = "sha256"

    def __str__(self) -> str:
        return str(self.value)
