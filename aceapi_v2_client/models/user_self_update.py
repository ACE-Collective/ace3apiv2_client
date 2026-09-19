from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSelfUpdate")


@_attrs_define
class UserSelfUpdate:
    """The fields a user may change on their OWN account from the preferences page. Username,
    email, password and enablement stay with the admin endpoints (and the change-password
    page), so this is deliberately not UserUpdate with the id removed.

        Attributes:
            display_name (None | str | Unset):
            timezone (None | str | Unset):
            queue (None | str | Unset):
    """

    display_name: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    queue: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        queue: None | str | Unset
        if isinstance(self.queue, Unset):
            queue = UNSET
        else:
            queue = self.queue

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if queue is not UNSET:
            field_dict["queue"] = queue

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_queue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queue = _parse_queue(d.pop("queue", UNSET))

        user_self_update = cls(
            display_name=display_name,
            timezone=timezone,
            queue=queue,
        )

        return user_self_update
