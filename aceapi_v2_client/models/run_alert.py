from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_row import AlertRow
    from ..models.run_alert_detection import RunAlertDetection


T = TypeVar("T", bound="RunAlert")


@_attrs_define
class RunAlert:
    """An alert attributed to the run, now or before (docs/SVS_API.md, *Run alerts*).

    Attributes:
        alert_uuid (str):
        holds (bool): some attribution of it to the run holds
        late (bool): an attribution that holds is late
        cleanup (bool): every attribution that holds is the test's cleanup's
        fallback_time (bool): an attribution that holds was judged by a fallback event time
        manual (bool): an attribution that holds was made by a person
        kept (bool): a person kept its context attributions
        undecided_context (bool): it has a context attribution that holds and nobody kept: a review waits for keep or
            not-a-test
        detections (list[RunAlertDetection]): every detection of the alert, and those it no longer has that were
            attributed
        alert (AlertRow | None | Unset): the alert as GET /api/v2/alerts lists it; null when it is gone
        confidence (None | str | Unset): of those that hold: marker when any is (a person's association is marker), else
            context
    """

    alert_uuid: str
    holds: bool
    late: bool
    cleanup: bool
    fallback_time: bool
    manual: bool
    kept: bool
    undecided_context: bool
    detections: list[RunAlertDetection]
    alert: AlertRow | None | Unset = UNSET
    confidence: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alert_row import AlertRow

        alert_uuid = self.alert_uuid

        holds = self.holds

        late = self.late

        cleanup = self.cleanup

        fallback_time = self.fallback_time

        manual = self.manual

        kept = self.kept

        undecided_context = self.undecided_context

        detections = []
        for detections_item_data in self.detections:
            detections_item = detections_item_data.to_dict()
            detections.append(detections_item)

        alert: dict[str, Any] | None | Unset
        if isinstance(self.alert, Unset):
            alert = UNSET
        elif isinstance(self.alert, AlertRow):
            alert = self.alert.to_dict()
        else:
            alert = self.alert

        confidence: None | str | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_uuid": alert_uuid,
                "holds": holds,
                "late": late,
                "cleanup": cleanup,
                "fallback_time": fallback_time,
                "manual": manual,
                "kept": kept,
                "undecided_context": undecided_context,
                "detections": detections,
            }
        )
        if alert is not UNSET:
            field_dict["alert"] = alert
        if confidence is not UNSET:
            field_dict["confidence"] = confidence

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_row import AlertRow
        from ..models.run_alert_detection import RunAlertDetection

        d = dict(src_dict)
        alert_uuid = d.pop("alert_uuid")

        holds = d.pop("holds")

        late = d.pop("late")

        cleanup = d.pop("cleanup")

        fallback_time = d.pop("fallback_time")

        manual = d.pop("manual")

        kept = d.pop("kept")

        undecided_context = d.pop("undecided_context")

        detections = []
        _detections = d.pop("detections")
        for detections_item_data in _detections:
            detections_item = RunAlertDetection.from_dict(detections_item_data)

            detections.append(detections_item)

        def _parse_alert(data: object) -> AlertRow | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alert_type_0 = AlertRow.from_dict(data)

                return alert_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertRow | None | Unset, data)

        alert = _parse_alert(d.pop("alert", UNSET))

        def _parse_confidence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        run_alert = cls(
            alert_uuid=alert_uuid,
            holds=holds,
            late=late,
            cleanup=cleanup,
            fallback_time=fallback_time,
            manual=manual,
            kept=kept,
            undecided_context=undecided_context,
            detections=detections,
            alert=alert,
            confidence=confidence,
        )

        run_alert.additional_properties = d
        return run_alert

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
