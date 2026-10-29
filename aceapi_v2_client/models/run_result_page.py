from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_result import RunResult


T = TypeVar("T", bound="RunResultPage")


@_attrs_define
class RunResultPage:
    """
    Attributes:
        data (list[RunResult]):
        next_cursor (None | str | Unset):
        stale (bool | None | Unset): one run's results only: something changed since the result was computed, and the
            timers recompute it shortly
        computed_at (datetime.datetime | None | Unset): one run's results only: when it was last computed
    """

    data: list[RunResult]
    next_cursor: None | str | Unset = UNSET
    stale: bool | None | Unset = UNSET
    computed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        stale: bool | None | Unset
        if isinstance(self.stale, Unset):
            stale = UNSET
        else:
            stale = self.stale

        computed_at: None | str | Unset
        if isinstance(self.computed_at, Unset):
            computed_at = UNSET
        elif isinstance(self.computed_at, datetime.datetime):
            computed_at = self.computed_at.isoformat()
        else:
            computed_at = self.computed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if stale is not UNSET:
            field_dict["stale"] = stale
        if computed_at is not UNSET:
            field_dict["computed_at"] = computed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.run_result import RunResult

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = RunResult.from_dict(data_item_data)

            data.append(data_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        def _parse_stale(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        stale = _parse_stale(d.pop("stale", UNSET))

        def _parse_computed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                computed_at_type_0 = datetime.datetime.fromisoformat(data)

                return computed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        computed_at = _parse_computed_at(d.pop("computed_at", UNSET))

        run_result_page = cls(
            data=data,
            next_cursor=next_cursor,
            stale=stale,
            computed_at=computed_at,
        )

        run_result_page.additional_properties = d
        return run_result_page

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
