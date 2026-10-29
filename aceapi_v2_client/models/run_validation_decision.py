from enum import StrEnum


class RunValidationDecision(StrEnum):
    ACCEPTED = "accepted"
    HOST_BUSY = "host_busy"
    INVALID = "invalid"
    REFUSED = "refused"

    def __str__(self) -> str:
        return str(self.value)
