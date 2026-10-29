from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.run_state import RunState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_event_details_type_0 import RunEventDetailsType0


T = TypeVar("T", bound="RunEvent")


@_attrs_define
class RunEvent:
    """One row of a run's event log.

    Attributes:
        id (int): the event's id; a run's events are in id order
        run_id (str): the run's uuid
        kind (str): what happened: registered, transition, launcher_call, ... (docs/SVS_API.md, *Run events*)
        actor (str): who did it: the caller's name, or svs for a timer
        created_at (datetime.datetime):
        updated_at (datetime.datetime): the feed's changed_since key
        from_state (None | RunState | Unset):
        to_state (None | RunState | Unset):
        actor_user (None | str | Unset): the actor's username, when the actor is a user
        details (None | RunEventDetailsType0 | Unset): what the event carries; its shape depends on kind
    """

    id: int
    run_id: str
    kind: str
    actor: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    from_state: None | RunState | Unset = UNSET
    to_state: None | RunState | Unset = UNSET
    actor_user: None | str | Unset = UNSET
    details: None | RunEventDetailsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.run_event_details_type_0 import RunEventDetailsType0

        id = self.id

        run_id = self.run_id

        kind = self.kind

        actor = self.actor

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        from_state: None | str | Unset
        if isinstance(self.from_state, Unset):
            from_state = UNSET
        elif isinstance(self.from_state, RunState):
            from_state = self.from_state.value
        else:
            from_state = self.from_state

        to_state: None | str | Unset
        if isinstance(self.to_state, Unset):
            to_state = UNSET
        elif isinstance(self.to_state, RunState):
            to_state = self.to_state.value
        else:
            to_state = self.to_state

        actor_user: None | str | Unset
        if isinstance(self.actor_user, Unset):
            actor_user = UNSET
        else:
            actor_user = self.actor_user

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, RunEventDetailsType0):
            details = self.details.to_dict()
        else:
            details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "run_id": run_id,
                "kind": kind,
                "actor": actor,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if from_state is not UNSET:
            field_dict["from_state"] = from_state
        if to_state is not UNSET:
            field_dict["to_state"] = to_state
        if actor_user is not UNSET:
            field_dict["actor_user"] = actor_user
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.run_event_details_type_0 import RunEventDetailsType0

        d = dict(src_dict)
        id = d.pop("id")

        run_id = d.pop("run_id")

        kind = d.pop("kind")

        actor = d.pop("actor")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_from_state(data: object) -> None | RunState | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_state_type_0 = RunState(data)

                return from_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunState | Unset, data)

        from_state = _parse_from_state(d.pop("from_state", UNSET))

        def _parse_to_state(data: object) -> None | RunState | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_state_type_0 = RunState(data)

                return to_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunState | Unset, data)

        to_state = _parse_to_state(d.pop("to_state", UNSET))

        def _parse_actor_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actor_user = _parse_actor_user(d.pop("actor_user", UNSET))

        def _parse_details(data: object) -> None | RunEventDetailsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = RunEventDetailsType0.from_dict(data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunEventDetailsType0 | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        run_event = cls(
            id=id,
            run_id=run_id,
            kind=kind,
            actor=actor,
            created_at=created_at,
            updated_at=updated_at,
            from_state=from_state,
            to_state=to_state,
            actor_user=actor_user,
            details=details,
        )

        run_event.additional_properties = d
        return run_event

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
