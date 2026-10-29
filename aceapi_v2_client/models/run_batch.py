from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_batch_states import RunBatchStates


T = TypeVar("T", bound="RunBatch")


@_attrs_define
class RunBatch:
    """One batch_id over the runs the filters match: only those runs are counted.

    Attributes:
        batch_id (str):
        runs (int):
        states (RunBatchStates): the runs per state, every state named
        needs_attention (int): the runs in the Needs attention view
        first_created_at (datetime.datetime): when its first run was registered
        last_created_at (datetime.datetime): when its latest run was registered; the batches are newest first by it
        result_hit (int | Unset): expected signatures that fired, summed over the runs Default: 0.
        result_expected (int | Unset): the expected signatures the results judged, summed Default: 0.
        result_missing (int | Unset): expected signatures that didn't fire, possibly suppressed ones included, summed
            Default: 0.
        result_candidate (int | Unset): undecided signatures that fired, summed Default: 0.
    """

    batch_id: str
    runs: int
    states: RunBatchStates
    needs_attention: int
    first_created_at: datetime.datetime
    last_created_at: datetime.datetime
    result_hit: int | Unset = 0
    result_expected: int | Unset = 0
    result_missing: int | Unset = 0
    result_candidate: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_id = self.batch_id

        runs = self.runs

        states = self.states.to_dict()

        needs_attention = self.needs_attention

        first_created_at = self.first_created_at.isoformat()

        last_created_at = self.last_created_at.isoformat()

        result_hit = self.result_hit

        result_expected = self.result_expected

        result_missing = self.result_missing

        result_candidate = self.result_candidate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batch_id": batch_id,
                "runs": runs,
                "states": states,
                "needs_attention": needs_attention,
                "first_created_at": first_created_at,
                "last_created_at": last_created_at,
            }
        )
        if result_hit is not UNSET:
            field_dict["result_hit"] = result_hit
        if result_expected is not UNSET:
            field_dict["result_expected"] = result_expected
        if result_missing is not UNSET:
            field_dict["result_missing"] = result_missing
        if result_candidate is not UNSET:
            field_dict["result_candidate"] = result_candidate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.run_batch_states import RunBatchStates

        d = dict(src_dict)
        batch_id = d.pop("batch_id")

        runs = d.pop("runs")

        states = RunBatchStates.from_dict(d.pop("states"))

        needs_attention = d.pop("needs_attention")

        first_created_at = datetime.datetime.fromisoformat(d.pop("first_created_at"))

        last_created_at = datetime.datetime.fromisoformat(d.pop("last_created_at"))

        result_hit = d.pop("result_hit", UNSET)

        result_expected = d.pop("result_expected", UNSET)

        result_missing = d.pop("result_missing", UNSET)

        result_candidate = d.pop("result_candidate", UNSET)

        run_batch = cls(
            batch_id=batch_id,
            runs=runs,
            states=states,
            needs_attention=needs_attention,
            first_created_at=first_created_at,
            last_created_at=last_created_at,
            result_hit=result_hit,
            result_expected=result_expected,
            result_missing=result_missing,
            result_candidate=result_candidate,
        )

        run_batch.additional_properties = d
        return run_batch

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
