from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RunTarget")


@_attrs_define
class RunTarget:
    """
    Attributes:
        hostname (str): as registered
        host (str): the short host name, lower case
        username (None | str | Unset): as registered
        fqdn (None | str | Unset):
        user (None | str | Unset): the bare user name, lower case
    """

    hostname: str
    host: str
    username: None | str | Unset = UNSET
    fqdn: None | str | Unset = UNSET
    user: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        host = self.host

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        fqdn: None | str | Unset
        if isinstance(self.fqdn, Unset):
            fqdn = UNSET
        else:
            fqdn = self.fqdn

        user: None | str | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
                "host": host,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if fqdn is not UNSET:
            field_dict["fqdn"] = fqdn
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hostname = d.pop("hostname")

        host = d.pop("host")

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_fqdn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fqdn = _parse_fqdn(d.pop("fqdn", UNSET))

        def _parse_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        run_target = cls(
            hostname=hostname,
            host=host,
            username=username,
            fqdn=fqdn,
            user=user,
        )

        run_target.additional_properties = d
        return run_target

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
