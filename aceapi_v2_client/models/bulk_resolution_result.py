from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.worklist_conflict_item import WorklistConflictItem
    from ..models.worklist_key import WorklistKey


T = TypeVar("T", bound="BulkResolutionResult")


@_attrs_define
class BulkResolutionResult:
    """
    Attributes:
        done (list[WorklistKey]): the rows resolved
        conflicts (list[WorklistConflictItem]): rows that are confirmed, informational, retired or removed; left alone
        unknown (list[WorklistKey]): rows that don't exist
    """

    done: list[WorklistKey]
    conflicts: list[WorklistConflictItem]
    unknown: list[WorklistKey]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = []
        for done_item_data in self.done:
            done_item = done_item_data.to_dict()
            done.append(done_item)

        conflicts = []
        for conflicts_item_data in self.conflicts:
            conflicts_item = conflicts_item_data.to_dict()
            conflicts.append(conflicts_item)

        unknown = []
        for unknown_item_data in self.unknown:
            unknown_item = unknown_item_data.to_dict()
            unknown.append(unknown_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "done": done,
                "conflicts": conflicts,
                "unknown": unknown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.worklist_conflict_item import WorklistConflictItem
        from ..models.worklist_key import WorklistKey

        d = dict(src_dict)
        done = []
        _done = d.pop("done")
        for done_item_data in _done:
            done_item = WorklistKey.from_dict(done_item_data)

            done.append(done_item)

        conflicts = []
        _conflicts = d.pop("conflicts")
        for conflicts_item_data in _conflicts:
            conflicts_item = WorklistConflictItem.from_dict(conflicts_item_data)

            conflicts.append(conflicts_item)

        unknown = []
        _unknown = d.pop("unknown")
        for unknown_item_data in _unknown:
            unknown_item = WorklistKey.from_dict(unknown_item_data)

            unknown.append(unknown_item)

        bulk_resolution_result = cls(
            done=done,
            conflicts=conflicts,
            unknown=unknown,
        )

        bulk_resolution_result.additional_properties = d
        return bulk_resolution_result

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
