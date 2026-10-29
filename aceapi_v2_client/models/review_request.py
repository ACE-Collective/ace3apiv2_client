from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewRequest")


@_attrs_define
class ReviewRequest:
    """
    Attributes:
        confirmed_take_from (None | str | Unset): the username of the run's owner the caller agreed to take it from,
            when someone else owns it
    """

    confirmed_take_from: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confirmed_take_from: None | str | Unset
        if isinstance(self.confirmed_take_from, Unset):
            confirmed_take_from = UNSET
        else:
            confirmed_take_from = self.confirmed_take_from

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirmed_take_from is not UNSET:
            field_dict["confirmed_take_from"] = confirmed_take_from

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_confirmed_take_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confirmed_take_from = _parse_confirmed_take_from(
            d.pop("confirmed_take_from", UNSET)
        )

        review_request = cls(
            confirmed_take_from=confirmed_take_from,
        )

        review_request.additional_properties = d
        return review_request

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
