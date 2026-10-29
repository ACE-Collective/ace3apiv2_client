from enum import StrEnum


class ValidationResultRowLabelSourceType0(StrEnum):
    EXPLICIT = "explicit"
    INHERITED_MULTI = "inherited_multi"
    INHERITED_SINGLE = "inherited_single"

    def __str__(self) -> str:
        return str(self.value)
