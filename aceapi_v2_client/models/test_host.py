from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestHost")


@_attrs_define
class TestHost:
    """
    Attributes:
        id (int):
        hostname (str): the short name, lower case
        usernames (list[str]): bare user names, lower case; empty means any user
        ips (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        fqdn (None | str | Unset):
        platform (None | str | Unset):
        notes (None | str | Unset):
        created_by (None | str | Unset): who added it (username)
    """

    id: int
    hostname: str
    usernames: list[str]
    ips: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    fqdn: None | str | Unset = UNSET
    platform: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    created_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        hostname = self.hostname

        usernames = self.usernames

        ips = self.ips

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        fqdn: None | str | Unset
        if isinstance(self.fqdn, Unset):
            fqdn = UNSET
        else:
            fqdn = self.fqdn

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "hostname": hostname,
                "usernames": usernames,
                "ips": ips,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if fqdn is not UNSET:
            field_dict["fqdn"] = fqdn
        if platform is not UNSET:
            field_dict["platform"] = platform
        if notes is not UNSET:
            field_dict["notes"] = notes
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        hostname = d.pop("hostname")

        usernames = cast(list[str], d.pop("usernames"))

        ips = cast(list[str], d.pop("ips"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_fqdn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fqdn = _parse_fqdn(d.pop("fqdn", UNSET))

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        test_host = cls(
            id=id,
            hostname=hostname,
            usernames=usernames,
            ips=ips,
            created_at=created_at,
            updated_at=updated_at,
            fqdn=fqdn,
            platform=platform,
            notes=notes,
            created_by=created_by,
        )

        test_host.additional_properties = d
        return test_host

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
