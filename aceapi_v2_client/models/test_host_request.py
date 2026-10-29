from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestHostRequest")


@_attrs_define
class TestHostRequest:
    """A test host as an svs:admin adds or replaces it. Names are matched case-insensitively.

    Attributes:
        hostname (str): the short or fully qualified host name; a fully qualified one also sets fqdn
        fqdn (None | str | Unset): the fully qualified name, when the host has one. A target named by a fully qualified
            name matches only this one
        usernames (list[str] | Unset): the users runs may use on the host, as user, DOMAIN\\user or user@domain; empty
            means any user
        ips (list[str] | Unset): the host's addresses
        platform (None | str | Unset): one of windows, linux, macos, when known: a test that doesn't support it can't
            target the host
        notes (None | str | Unset):
    """

    hostname: str
    fqdn: None | str | Unset = UNSET
    usernames: list[str] | Unset = UNSET
    ips: list[str] | Unset = UNSET
    platform: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        fqdn: None | str | Unset
        if isinstance(self.fqdn, Unset):
            fqdn = UNSET
        else:
            fqdn = self.fqdn

        usernames: list[str] | Unset = UNSET
        if not isinstance(self.usernames, Unset):
            usernames = self.usernames

        ips: list[str] | Unset = UNSET
        if not isinstance(self.ips, Unset):
            ips = self.ips

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
            }
        )
        if fqdn is not UNSET:
            field_dict["fqdn"] = fqdn
        if usernames is not UNSET:
            field_dict["usernames"] = usernames
        if ips is not UNSET:
            field_dict["ips"] = ips
        if platform is not UNSET:
            field_dict["platform"] = platform
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hostname = d.pop("hostname")

        def _parse_fqdn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fqdn = _parse_fqdn(d.pop("fqdn", UNSET))

        usernames = cast(list[str], d.pop("usernames", UNSET))

        ips = cast(list[str], d.pop("ips", UNSET))

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

        test_host_request = cls(
            hostname=hostname,
            fqdn=fqdn,
            usernames=usernames,
            ips=ips,
            platform=platform,
            notes=notes,
        )

        test_host_request.additional_properties = d
        return test_host_request

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
