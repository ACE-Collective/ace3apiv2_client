from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_entry_base import FilterEntryBase


T = TypeVar("T", bound="DecodedFilters")


@_attrs_define
class DecodedFilters:
    """
    Attributes:
        filters (list[FilterEntryBase]):
        warnings (list[str] | Unset): filters the link names that no longer exist; they were skipped
    """

    filters: list[FilterEntryBase]
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_entry_base import FilterEntryBase

        d = dict(src_dict)
        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = FilterEntryBase.from_dict(filters_item_data)

            filters.append(filters_item)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        decoded_filters = cls(
            filters=filters,
            warnings=warnings,
        )

        decoded_filters.additional_properties = d
        return decoded_filters

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
