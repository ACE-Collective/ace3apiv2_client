from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.review_result_counts import ReviewResultCounts
    from ..models.run_detail import RunDetail


T = TypeVar("T", bound="ReviewResult")


@_attrs_define
class ReviewResult:
    """
    Attributes:
        run (RunDetail):
        re_review (bool): the run had been reviewed before; this sign-off replaces that one
        counts (ReviewResultCounts): signatures per result status, as signed off
        alerts_closed (int): alerts that became SIMULATED
        fp_verdicts (int): detections of ignored signatures given an FP verdict
    """

    run: RunDetail
    re_review: bool
    counts: ReviewResultCounts
    alerts_closed: int
    fp_verdicts: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run = self.run.to_dict()

        re_review = self.re_review

        counts = self.counts.to_dict()

        alerts_closed = self.alerts_closed

        fp_verdicts = self.fp_verdicts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run": run,
                "re_review": re_review,
                "counts": counts,
                "alerts_closed": alerts_closed,
                "fp_verdicts": fp_verdicts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.review_result_counts import ReviewResultCounts
        from ..models.run_detail import RunDetail

        d = dict(src_dict)
        run = RunDetail.from_dict(d.pop("run"))

        re_review = d.pop("re_review")

        counts = ReviewResultCounts.from_dict(d.pop("counts"))

        alerts_closed = d.pop("alerts_closed")

        fp_verdicts = d.pop("fp_verdicts")

        review_result = cls(
            run=run,
            re_review=re_review,
            counts=counts,
            alerts_closed=alerts_closed,
            fp_verdicts=fp_verdicts,
        )

        review_result.additional_properties = d
        return review_result

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
