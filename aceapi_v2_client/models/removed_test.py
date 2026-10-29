from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemovedTest")


@_attrs_define
class RemovedTest:
    """
    Attributes:
        guid (str):
        name (str):
        technique (str):
        removed_at (datetime.datetime | None | Unset):
    """

    guid: str
    name: str
    technique: str
    removed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guid = self.guid

        name = self.name

        technique = self.technique

        removed_at: None | str | Unset
        if isinstance(self.removed_at, Unset):
            removed_at = UNSET
        elif isinstance(self.removed_at, datetime.datetime):
            removed_at = self.removed_at.isoformat()
        else:
            removed_at = self.removed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "guid": guid,
                "name": name,
                "technique": technique,
            }
        )
        if removed_at is not UNSET:
            field_dict["removed_at"] = removed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        guid = d.pop("guid")

        name = d.pop("name")

        technique = d.pop("technique")

        def _parse_removed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                removed_at_type_0 = datetime.datetime.fromisoformat(data)

                return removed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        removed_at = _parse_removed_at(d.pop("removed_at", UNSET))

        removed_test = cls(
            guid=guid,
            name=name,
            technique=technique,
            removed_at=removed_at,
        )

        removed_test.additional_properties = d
        return removed_test

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
