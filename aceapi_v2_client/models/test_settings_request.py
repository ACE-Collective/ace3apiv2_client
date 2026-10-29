from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestSettingsRequest")


@_attrs_define
class TestSettingsRequest:
    """A test's settings, as svs:run_manage sets them.

    Attributes:
        observation_minutes (int | None | Unset): the observation window of the test's runs registered from now on, used
            as it is (no slack, no floor), from 1 minute up to svs.runs.observation_window.ceiling_hours; null for the
            computed window
        holds_host (bool | Unset): the test leaves something behind on its hosts, so each run of it registered from now
            on holds them until its attribution window ends, not its observation window (docs/SVS_RUNS.md, *One run per test
            host*) Default: False.
    """

    observation_minutes: int | None | Unset = UNSET
    holds_host: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observation_minutes: int | None | Unset
        if isinstance(self.observation_minutes, Unset):
            observation_minutes = UNSET
        else:
            observation_minutes = self.observation_minutes

        holds_host = self.holds_host

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if observation_minutes is not UNSET:
            field_dict["observation_minutes"] = observation_minutes
        if holds_host is not UNSET:
            field_dict["holds_host"] = holds_host

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_observation_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        observation_minutes = _parse_observation_minutes(
            d.pop("observation_minutes", UNSET)
        )

        holds_host = d.pop("holds_host", UNSET)

        test_settings_request = cls(
            observation_minutes=observation_minutes,
            holds_host=holds_host,
        )

        test_settings_request.additional_properties = d
        return test_settings_request

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
