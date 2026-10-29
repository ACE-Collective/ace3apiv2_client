from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.host_holder import HostHolder


T = TypeVar("T", bound="RunValidationTarget")


@_attrs_define
class RunValidationTarget:
    """
    Attributes:
        hostname (str): as sent
        accepted (bool): the target is a test host and a user it lists
        username (None | str | Unset): as sent
        reason (None | str | Unset): why the target would be refused
        test_host (None | str | Unset): the test host it names, by its short name
        platform (None | str | Unset): that test host's platform
        held_by (list[HostHolder] | Unset): the runs holding that test host
    """

    hostname: str
    accepted: bool
    username: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    test_host: None | str | Unset = UNSET
    platform: None | str | Unset = UNSET
    held_by: list[HostHolder] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        accepted = self.accepted

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        test_host: None | str | Unset
        if isinstance(self.test_host, Unset):
            test_host = UNSET
        else:
            test_host = self.test_host

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        held_by: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.held_by, Unset):
            held_by = []
            for held_by_item_data in self.held_by:
                held_by_item = held_by_item_data.to_dict()
                held_by.append(held_by_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
                "accepted": accepted,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if reason is not UNSET:
            field_dict["reason"] = reason
        if test_host is not UNSET:
            field_dict["test_host"] = test_host
        if platform is not UNSET:
            field_dict["platform"] = platform
        if held_by is not UNSET:
            field_dict["held_by"] = held_by

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.host_holder import HostHolder

        d = dict(src_dict)
        hostname = d.pop("hostname")

        accepted = d.pop("accepted")

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_test_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        test_host = _parse_test_host(d.pop("test_host", UNSET))

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        _held_by = d.pop("held_by", UNSET)
        held_by: list[HostHolder] | Unset = UNSET
        if _held_by is not UNSET:
            held_by = []
            for held_by_item_data in _held_by:
                held_by_item = HostHolder.from_dict(held_by_item_data)

                held_by.append(held_by_item)

        run_validation_target = cls(
            hostname=hostname,
            accepted=accepted,
            username=username,
            reason=reason,
            test_host=test_host,
            platform=platform,
            held_by=held_by,
        )

        run_validation_target.additional_properties = d
        return run_validation_target

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
