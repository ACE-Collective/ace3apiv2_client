from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaintenanceWindow")


@_attrs_define
class MaintenanceWindow:
    """A test host's maintenance window (docs/SVS_RUNS.md, *Maintenance windows*).

    Attributes:
        id (str): the window's uuid; svs_maintenance in ACE's logs
        host (str): the test host, by its short name
        reason (str):
        opened_by (str): who opened it: the key's or user's name
        opened_at (datetime.datetime):
        ends_at (datetime.datetime): when it was opened to end
        open_ (bool): it hasn't ended
        fqdn (None | str | Unset):
        ended_at (datetime.datetime | None | Unset): when it ended: early, or at ends_at
        ended_by (None | str | Unset): who ended it; svs when it expired
        end_reason (None | str | Unset): ended or expired
    """

    id: str
    host: str
    reason: str
    opened_by: str
    opened_at: datetime.datetime
    ends_at: datetime.datetime
    open_: bool
    fqdn: None | str | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    ended_by: None | str | Unset = UNSET
    end_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        host = self.host

        reason = self.reason

        opened_by = self.opened_by

        opened_at = self.opened_at.isoformat()

        ends_at = self.ends_at.isoformat()

        open_ = self.open_

        fqdn: None | str | Unset
        if isinstance(self.fqdn, Unset):
            fqdn = UNSET
        else:
            fqdn = self.fqdn

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        ended_by: None | str | Unset
        if isinstance(self.ended_by, Unset):
            ended_by = UNSET
        else:
            ended_by = self.ended_by

        end_reason: None | str | Unset
        if isinstance(self.end_reason, Unset):
            end_reason = UNSET
        else:
            end_reason = self.end_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "host": host,
                "reason": reason,
                "opened_by": opened_by,
                "opened_at": opened_at,
                "ends_at": ends_at,
                "open": open_,
            }
        )
        if fqdn is not UNSET:
            field_dict["fqdn"] = fqdn
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if ended_by is not UNSET:
            field_dict["ended_by"] = ended_by
        if end_reason is not UNSET:
            field_dict["end_reason"] = end_reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        host = d.pop("host")

        reason = d.pop("reason")

        opened_by = d.pop("opened_by")

        opened_at = datetime.datetime.fromisoformat(d.pop("opened_at"))

        ends_at = datetime.datetime.fromisoformat(d.pop("ends_at"))

        open_ = d.pop("open")

        def _parse_fqdn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fqdn = _parse_fqdn(d.pop("fqdn", UNSET))

        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        def _parse_ended_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ended_by = _parse_ended_by(d.pop("ended_by", UNSET))

        def _parse_end_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_reason = _parse_end_reason(d.pop("end_reason", UNSET))

        maintenance_window = cls(
            id=id,
            host=host,
            reason=reason,
            opened_by=opened_by,
            opened_at=opened_at,
            ends_at=ends_at,
            open_=open_,
            fqdn=fqdn,
            ended_at=ended_at,
            ended_by=ended_by,
            end_reason=end_reason,
        )

        maintenance_window.additional_properties = d
        return maintenance_window

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
