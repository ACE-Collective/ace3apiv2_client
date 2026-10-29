from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.bulk_run_result_conflicts import BulkRunResultConflicts
    from ..models.bulk_run_result_left_alone import BulkRunResultLeftAlone


T = TypeVar("T", bound="BulkRunResult")


@_attrs_define
class BulkRunResult:
    """
    Attributes:
        done (list[str]): the runs the action was applied to
        left_alone (BulkRunResultLeftAlone): run id -> the username of whoever owns it, for the runs someone else owns;
            sent back as confirmed_takes it takes them
        conflicts (BulkRunResultConflicts): run id -> why the action doesn't apply to it (its state, a missing reason)
        unknown (list[str]): run ids that don't exist
    """

    done: list[str]
    left_alone: BulkRunResultLeftAlone
    conflicts: BulkRunResultConflicts
    unknown: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        left_alone = self.left_alone.to_dict()

        conflicts = self.conflicts.to_dict()

        unknown = self.unknown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "done": done,
                "left_alone": left_alone,
                "conflicts": conflicts,
                "unknown": unknown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_run_result_conflicts import BulkRunResultConflicts
        from ..models.bulk_run_result_left_alone import BulkRunResultLeftAlone

        d = dict(src_dict)
        done = cast(list[str], d.pop("done"))

        left_alone = BulkRunResultLeftAlone.from_dict(d.pop("left_alone"))

        conflicts = BulkRunResultConflicts.from_dict(d.pop("conflicts"))

        unknown = cast(list[str], d.pop("unknown"))

        bulk_run_result = cls(
            done=done,
            left_alone=left_alone,
            conflicts=conflicts,
            unknown=unknown,
        )

        bulk_run_result.additional_properties = d
        return bulk_run_result

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
