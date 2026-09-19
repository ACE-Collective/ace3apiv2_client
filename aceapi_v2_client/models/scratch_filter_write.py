from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_entry import FilterEntry


T = TypeVar("T", bound="ScratchFilterWrite")


@_attrs_define
class ScratchFilterWrite:
    """Replace the caller's singleton `working` or `temp` row.

    Attributes:
        filters (list[FilterEntry] | Unset):
        label (None | str | Unset):
    """

    filters: list[FilterEntry] | Unset = UNSET
    label: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_entry import FilterEntry

        d = dict(src_dict)
        _filters = d.pop("filters", UNSET)
        filters: list[FilterEntry] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = FilterEntry.from_dict(filters_item_data)

                filters.append(filters_item)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        scratch_filter_write = cls(
            filters=filters,
            label=label,
        )

        return scratch_filter_write
