from enum import StrEnum


class ExportFormat(StrEnum):
    CSV = "csv"

    def __str__(self) -> str:
        return str(self.value)
