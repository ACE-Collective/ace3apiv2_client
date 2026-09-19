from enum import StrEnum


class AlertSearchResultOutTierType0(StrEnum):
    EXACT = "exact"
    GOOD = "good"
    STRONG = "strong"
    WEAK = "weak"

    def __str__(self) -> str:
        return str(self.value)
