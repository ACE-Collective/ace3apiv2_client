from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuickFilterOrder")


@_attrs_define
class QuickFilterOrder:
    """The complete, ordered set of pinned quick filters. Anything not listed is unpinned,
    which makes the call idempotent and lets a reorder UI submit its whole state.

        Attributes:
            filter_uuids (list[str] | Unset):
    """

    filter_uuids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        filter_uuids: list[str] | Unset = UNSET
        if not isinstance(self.filter_uuids, Unset):
            filter_uuids = self.filter_uuids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if filter_uuids is not UNSET:
            field_dict["filter_uuids"] = filter_uuids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        filter_uuids = cast(list[str], d.pop("filter_uuids", UNSET))

        quick_filter_order = cls(
            filter_uuids=filter_uuids,
        )

        return quick_filter_order
