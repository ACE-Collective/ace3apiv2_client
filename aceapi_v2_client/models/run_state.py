from enum import StrEnum


class RunState(StrEnum):
    CANCELED = "canceled"
    CLOSED = "closed"
    CREATED = "created"
    ENDED = "ended"
    ERROR = "error"
    REVIEWED = "reviewed"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
