from enum import StrEnum


class ObservationSource(StrEnum):
    ALL_HUNTS = "all_hunts"
    EXPECTED = "expected"
    OVERRIDE = "override"

    def __str__(self) -> str:
        return str(self.value)
