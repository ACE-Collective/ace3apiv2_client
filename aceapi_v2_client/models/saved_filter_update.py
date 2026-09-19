from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_entry import FilterEntry


T = TypeVar("T", bound="SavedFilterUpdate")


@_attrs_define
class SavedFilterUpdate:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        filters (list[FilterEntry] | None | Unset):
        quick_filter_indicator (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    filters: list[FilterEntry] | None | Unset = UNSET
    quick_filter_indicator: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = []
            for filters_type_0_item_data in self.filters:
                filters_type_0_item = filters_type_0_item_data.to_dict()
                filters.append(filters_type_0_item)

        else:
            filters = self.filters

        quick_filter_indicator: bool | None | Unset
        if isinstance(self.quick_filter_indicator, Unset):
            quick_filter_indicator = UNSET
        else:
            quick_filter_indicator = self.quick_filter_indicator

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if filters is not UNSET:
            field_dict["filters"] = filters
        if quick_filter_indicator is not UNSET:
            field_dict["quick_filter_indicator"] = quick_filter_indicator

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_entry import FilterEntry

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_filters(data: object) -> list[FilterEntry] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = []
                _filters_type_0 = data
                for filters_type_0_item_data in _filters_type_0:
                    filters_type_0_item = FilterEntry.from_dict(
                        filters_type_0_item_data
                    )

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterEntry] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_quick_filter_indicator(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        quick_filter_indicator = _parse_quick_filter_indicator(
            d.pop("quick_filter_indicator", UNSET)
        )

        saved_filter_update = cls(
            name=name,
            description=description,
            filters=filters,
            quick_filter_indicator=quick_filter_indicator,
        )

        return saved_filter_update
