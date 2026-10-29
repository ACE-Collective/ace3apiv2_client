from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ReviewBlockers")


@_attrs_define
class ReviewBlockers:
    """What a review would answer 409 with right now (docs/SVS_API.md, *Run actions*).

    Attributes:
        stale (bool): the result is being recomputed, or was never computed
        candidates (list[str]): the undecided signature uuids
        context_alerts (list[str]): the alerts with context attributions neither kept nor marked not a test
    """

    stale: bool
    candidates: list[str]
    context_alerts: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stale = self.stale

        candidates = self.candidates

        context_alerts = self.context_alerts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stale": stale,
                "candidates": candidates,
                "context_alerts": context_alerts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        stale = d.pop("stale")

        candidates = cast(list[str], d.pop("candidates"))

        context_alerts = cast(list[str], d.pop("context_alerts"))

        review_blockers = cls(
            stale=stale,
            candidates=candidates,
            context_alerts=context_alerts,
        )

        review_blockers.additional_properties = d
        return review_blockers

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
