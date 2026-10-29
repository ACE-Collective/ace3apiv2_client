from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RunTargetRequest")


@_attrs_define
class RunTargetRequest:
    """
    Attributes:
        hostname (str): a test host, by its short or fully qualified name
        username (None | str | Unset): the user the test runs as (user, DOMAIN\\user or user@domain); required when the
            test host lists its users
    """

    hostname: str
    username: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hostname = d.pop("hostname")

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        run_target_request = cls(
            hostname=hostname,
            username=username,
        )

        run_target_request.additional_properties = d
        return run_target_request

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
