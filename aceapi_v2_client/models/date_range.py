from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DateRange")


@_attrs_define
class DateRange:
    """A date filter value resolved to the window it means right now.

    Attributes:
        start (datetime.datetime):
        end (datetime.datetime):
        text (str): the window as the manage page shows it, in the requested timezone
    """

    start: datetime.datetime
    end: datetime.datetime
    text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start.isoformat()

        end = self.end.isoformat()

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start = datetime.datetime.fromisoformat(d.pop("start"))

        end = datetime.datetime.fromisoformat(d.pop("end"))

        text = d.pop("text")

        date_range = cls(
            start=start,
            end=end,
            text=text,
        )

        date_range.additional_properties = d
        return date_range

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
