from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.filter_descriptor import FilterDescriptor


T = TypeVar("T", bound="FilterScreenRead")


@_attrs_define
class FilterScreenRead:
    """What a screen filters on, for a generic filter editor.

    Attributes:
        name (str):
        filters (list[FilterDescriptor]):
    """

    name: str
    filters: list[FilterDescriptor]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "filters": filters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_descriptor import FilterDescriptor

        d = dict(src_dict)
        name = d.pop("name")

        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = FilterDescriptor.from_dict(filters_item_data)

            filters.append(filters_item)

        filter_screen_read = cls(
            name=name,
            filters=filters,
        )

        filter_screen_read.additional_properties = d
        return filter_screen_read

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
