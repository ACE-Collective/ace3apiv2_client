from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterEntryBase")


@_attrs_define
class FilterEntryBase:
    """The shape of a filter entry, valid for any screen. Which names and values a screen
    accepts is that screen's entry model (saq/gui/filter_screens.py).

        Attributes:
            name (str): a filter name of the screen the filter belongs to
            values (list[list[str] | str]): the values to filter on
            inverted (bool | Unset): negate this filter Default: False.
    """

    name: str
    values: list[list[str] | str]
    inverted: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        values = []
        for values_item_data in self.values:
            values_item: list[str] | str
            if isinstance(values_item_data, list):
                values_item = values_item_data

            else:
                values_item = values_item_data
            values.append(values_item)

        inverted = self.inverted

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "values": values,
            }
        )
        if inverted is not UNSET:
            field_dict["inverted"] = inverted

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:

            def _parse_values_item(data: object) -> list[str] | str:
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    values_item_type_1 = cast(list[str], data)

                    return values_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(list[str] | str, data)

            values_item = _parse_values_item(values_item_data)

            values.append(values_item)

        inverted = d.pop("inverted", UNSET)

        filter_entry_base = cls(
            name=name,
            values=values,
            inverted=inverted,
        )

        return filter_entry_base
