from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_entry import FilterEntry


T = TypeVar("T", bound="SavedFilterCreate")


@_attrs_define
class SavedFilterCreate:
    """
    Attributes:
        name (str):
        filters (list[FilterEntry]):
        description (None | str | Unset):
        quick_filter (bool | Unset): pin as a quick filter badge Default: False.
        quick_filter_indicator (bool | Unset): show an alert count on the badge Default: False.
    """

    name: str
    filters: list[FilterEntry]
    description: None | str | Unset = UNSET
    quick_filter: bool | Unset = False
    quick_filter_indicator: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        quick_filter = self.quick_filter

        quick_filter_indicator = self.quick_filter_indicator

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "filters": filters,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if quick_filter is not UNSET:
            field_dict["quick_filter"] = quick_filter
        if quick_filter_indicator is not UNSET:
            field_dict["quick_filter_indicator"] = quick_filter_indicator

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_entry import FilterEntry

        d = dict(src_dict)
        name = d.pop("name")

        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = FilterEntry.from_dict(filters_item_data)

            filters.append(filters_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        quick_filter = d.pop("quick_filter", UNSET)

        quick_filter_indicator = d.pop("quick_filter_indicator", UNSET)

        saved_filter_create = cls(
            name=name,
            filters=filters,
            description=description,
            quick_filter=quick_filter,
            quick_filter_indicator=quick_filter_indicator,
        )

        return saved_filter_create
