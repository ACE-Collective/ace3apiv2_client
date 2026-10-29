from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SuppressionShare")


@_attrs_define
class SuppressionShare:
    """How many of the expected signatures missing from reviewed runs were possibly suppressed: the
    trigger to revisit keeping the hunter from suppressing test targets (docs/SVS.md, Part 3, *Hunt
    suppression*). Read from every run's result as signed off.

        Attributes:
            missing (int): expected signatures missing from the signed-off results, possibly suppressed ones included
            possibly_suppressed (int): of those, the possibly suppressed
            reviewed_runs (int): the runs with a signed-off result
            trigger_reached (bool): 50 runs are reviewed, or 90 days passed since the first review
            reconsider (bool): the trigger is reached and more than 10% of the missing signatures were possibly suppressed:
                preventing suppression is worth reconsidering
            share (float | None | Unset): possibly_suppressed / missing; null while nothing is missing
            first_reviewed_at (datetime.datetime | None | Unset): when the first run was reviewed
    """

    missing: int
    possibly_suppressed: int
    reviewed_runs: int
    trigger_reached: bool
    reconsider: bool
    share: float | None | Unset = UNSET
    first_reviewed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        missing = self.missing

        possibly_suppressed = self.possibly_suppressed

        reviewed_runs = self.reviewed_runs

        trigger_reached = self.trigger_reached

        reconsider = self.reconsider

        share: float | None | Unset
        if isinstance(self.share, Unset):
            share = UNSET
        else:
            share = self.share

        first_reviewed_at: None | str | Unset
        if isinstance(self.first_reviewed_at, Unset):
            first_reviewed_at = UNSET
        elif isinstance(self.first_reviewed_at, datetime.datetime):
            first_reviewed_at = self.first_reviewed_at.isoformat()
        else:
            first_reviewed_at = self.first_reviewed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "missing": missing,
                "possibly_suppressed": possibly_suppressed,
                "reviewed_runs": reviewed_runs,
                "trigger_reached": trigger_reached,
                "reconsider": reconsider,
            }
        )
        if share is not UNSET:
            field_dict["share"] = share
        if first_reviewed_at is not UNSET:
            field_dict["first_reviewed_at"] = first_reviewed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        missing = d.pop("missing")

        possibly_suppressed = d.pop("possibly_suppressed")

        reviewed_runs = d.pop("reviewed_runs")

        trigger_reached = d.pop("trigger_reached")

        reconsider = d.pop("reconsider")

        def _parse_share(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        share = _parse_share(d.pop("share", UNSET))

        def _parse_first_reviewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_reviewed_at_type_0 = datetime.datetime.fromisoformat(data)

                return first_reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_reviewed_at = _parse_first_reviewed_at(d.pop("first_reviewed_at", UNSET))

        suppression_share = cls(
            missing=missing,
            possibly_suppressed=possibly_suppressed,
            reviewed_runs=reviewed_runs,
            trigger_reached=trigger_reached,
            reconsider=reconsider,
            share=share,
            first_reviewed_at=first_reviewed_at,
        )

        suppression_share.additional_properties = d
        return suppression_share

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
