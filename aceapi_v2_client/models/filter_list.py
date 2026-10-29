from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_entry_base import FilterEntryBase


T = TypeVar("T", bound="FilterList")


@_attrs_define
class FilterList:
    """
    Attributes:
        filters (list[FilterEntryBase] | Unset):
    """

    filters: list[FilterEntryBase] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_entry_base import FilterEntryBase

        d = dict(src_dict)
        _filters = d.pop("filters", UNSET)
        filters: list[FilterEntryBase] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = FilterEntryBase.from_dict(filters_item_data)

                filters.append(filters_item)

        filter_list = cls(
            filters=filters,
        )

        return filter_list
