from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestSettings")


@_attrs_define
class TestSettings:
    """
    Attributes:
        test_guid (str):
        updated_at (datetime.datetime):
        observation_minutes (int | None | Unset): null: the computed window
        holds_host (bool | Unset):  Default: False.
        set_by (None | str | Unset): who set them (username)
    """

    test_guid: str
    updated_at: datetime.datetime
    observation_minutes: int | None | Unset = UNSET
    holds_host: bool | Unset = False
    set_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_guid = self.test_guid

        updated_at = self.updated_at.isoformat()

        observation_minutes: int | None | Unset
        if isinstance(self.observation_minutes, Unset):
            observation_minutes = UNSET
        else:
            observation_minutes = self.observation_minutes

        holds_host = self.holds_host

        set_by: None | str | Unset
        if isinstance(self.set_by, Unset):
            set_by = UNSET
        else:
            set_by = self.set_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_guid": test_guid,
                "updated_at": updated_at,
            }
        )
        if observation_minutes is not UNSET:
            field_dict["observation_minutes"] = observation_minutes
        if holds_host is not UNSET:
            field_dict["holds_host"] = holds_host
        if set_by is not UNSET:
            field_dict["set_by"] = set_by

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        test_guid = d.pop("test_guid")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        def _parse_set_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        set_by = _parse_set_by(d.pop("set_by", UNSET))

        test_settings = cls(
            test_guid=test_guid,
            updated_at=updated_at,
            observation_minutes=observation_minutes,
            holds_host=holds_host,
            set_by=set_by,
        )

        test_settings.additional_properties = d
        return test_settings

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
