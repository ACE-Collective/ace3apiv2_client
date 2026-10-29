from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.period_counts_own_states import PeriodCountsOwnStates
    from ..models.period_counts_states import PeriodCountsStates


T = TypeVar("T", bound="PeriodCounts")


@_attrs_define
class PeriodCounts:
    """
    Attributes:
        period (str): the day (2026-10-16) or the month (2026-10)
        snapshot_date (datetime.date): the snapshot counted: the day's, or the month's last
        rows (int):
        states (PeriodCountsStates): rows per state, every state named
        own_states (PeriodCountsOwnStates): rows per own_state, every state named
    """

    period: str
    snapshot_date: datetime.date
    rows: int
    states: PeriodCountsStates
    own_states: PeriodCountsOwnStates
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period = self.period

        snapshot_date = self.snapshot_date.isoformat()

        rows = self.rows

        states = self.states.to_dict()

        own_states = self.own_states.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
                "snapshot_date": snapshot_date,
                "rows": rows,
                "states": states,
                "own_states": own_states,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.period_counts_own_states import PeriodCountsOwnStates
        from ..models.period_counts_states import PeriodCountsStates

        d = dict(src_dict)
        period = d.pop("period")

        snapshot_date = datetime.date.fromisoformat(d.pop("snapshot_date"))

        rows = d.pop("rows")

        states = PeriodCountsStates.from_dict(d.pop("states"))

        own_states = PeriodCountsOwnStates.from_dict(d.pop("own_states"))

        period_counts = cls(
            period=period,
            snapshot_date=snapshot_date,
            rows=rows,
            states=states,
            own_states=own_states,
        )

        period_counts.additional_properties = d
        return period_counts

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
