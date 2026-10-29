from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostHolder")


@_attrs_define
class HostHolder:
    """A run or a maintenance window holding a test host (docs/SVS_RUNS.md, *One run per test host*,
    *Maintenance windows*).

        Attributes:
            host (str): the test host, by its short name
            state (str): the run's state, or maintenance
            run_id (None | str | Unset): the run holding it; null for a maintenance window
            until (datetime.datetime | None | Unset): when its claim on the host ends; null while a run hasn't started
            maintenance_id (None | str | Unset): the maintenance window holding it
    """

    host: str
    state: str
    run_id: None | str | Unset = UNSET
    until: datetime.datetime | None | Unset = UNSET
    maintenance_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        state = self.state

        run_id: None | str | Unset
        if isinstance(self.run_id, Unset):
            run_id = UNSET
        else:
            run_id = self.run_id

        until: None | str | Unset
        if isinstance(self.until, Unset):
            until = UNSET
        elif isinstance(self.until, datetime.datetime):
            until = self.until.isoformat()
        else:
            until = self.until

        maintenance_id: None | str | Unset
        if isinstance(self.maintenance_id, Unset):
            maintenance_id = UNSET
        else:
            maintenance_id = self.maintenance_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "state": state,
            }
        )
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if until is not UNSET:
            field_dict["until"] = until
        if maintenance_id is not UNSET:
            field_dict["maintenance_id"] = maintenance_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        host = d.pop("host")

        state = d.pop("state")

        def _parse_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_id = _parse_run_id(d.pop("run_id", UNSET))

        def _parse_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                until_type_0 = datetime.datetime.fromisoformat(data)

                return until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        until = _parse_until(d.pop("until", UNSET))

        def _parse_maintenance_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        maintenance_id = _parse_maintenance_id(d.pop("maintenance_id", UNSET))

        host_holder = cls(
            host=host,
            state=state,
            run_id=run_id,
            until=until,
            maintenance_id=maintenance_id,
        )

        host_holder.additional_properties = d
        return host_holder

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
