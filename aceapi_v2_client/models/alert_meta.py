from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertMeta")


@_attrs_define
class AlertMeta:
    """The parts of an alert that change while an analyst has it open, for the alert page's poll.

    Everything here is database state, so it is read without loading the alert from disk.

        Attributes:
            is_locked (bool):
            status (str):
            version (str):
            disposition (None | str | Unset):
            disposition_user_id (int | None | Unset):
            disposition_user_name (None | str | Unset):
            owner_id (int | None | Unset):
            owner_name (None | str | Unset):
            owner_time (None | str | Unset): ISO 8601, UTC, with a Z suffix
    """

    is_locked: bool
    status: str
    version: str
    disposition: None | str | Unset = UNSET
    disposition_user_id: int | None | Unset = UNSET
    disposition_user_name: None | str | Unset = UNSET
    owner_id: int | None | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    owner_time: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_locked = self.is_locked

        status = self.status

        version = self.version

        disposition: None | str | Unset
        if isinstance(self.disposition, Unset):
            disposition = UNSET
        else:
            disposition = self.disposition

        disposition_user_id: int | None | Unset
        if isinstance(self.disposition_user_id, Unset):
            disposition_user_id = UNSET
        else:
            disposition_user_id = self.disposition_user_id

        disposition_user_name: None | str | Unset
        if isinstance(self.disposition_user_name, Unset):
            disposition_user_name = UNSET
        else:
            disposition_user_name = self.disposition_user_name

        owner_id: int | None | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        owner_time: None | str | Unset
        if isinstance(self.owner_time, Unset):
            owner_time = UNSET
        else:
            owner_time = self.owner_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_locked": is_locked,
                "status": status,
                "version": version,
            }
        )
        if disposition is not UNSET:
            field_dict["disposition"] = disposition
        if disposition_user_id is not UNSET:
            field_dict["disposition_user_id"] = disposition_user_id
        if disposition_user_name is not UNSET:
            field_dict["disposition_user_name"] = disposition_user_name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if owner_time is not UNSET:
            field_dict["owner_time"] = owner_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        is_locked = d.pop("is_locked")

        status = d.pop("status")

        version = d.pop("version")

        def _parse_disposition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disposition = _parse_disposition(d.pop("disposition", UNSET))

        def _parse_disposition_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        disposition_user_id = _parse_disposition_user_id(
            d.pop("disposition_user_id", UNSET)
        )

        def _parse_disposition_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disposition_user_name = _parse_disposition_user_name(
            d.pop("disposition_user_name", UNSET)
        )

        def _parse_owner_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("owner_name", UNSET))

        def _parse_owner_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_time = _parse_owner_time(d.pop("owner_time", UNSET))

        alert_meta = cls(
            is_locked=is_locked,
            status=status,
            version=version,
            disposition=disposition,
            disposition_user_id=disposition_user_id,
            disposition_user_name=disposition_user_name,
            owner_id=owner_id,
            owner_name=owner_name,
            owner_time=owner_time,
        )

        alert_meta.additional_properties = d
        return alert_meta

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
