from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_svs_detection import AlertSVSDetection
    from ..models.alert_svs_mismatch import AlertSVSMismatch
    from ..models.alert_svs_run import AlertSVSRun


T = TypeVar("T", bound="AlertSVS")


@_attrs_define
class AlertSVS:
    """What SVS makes of one alert (docs/SVS.md, Part 3, *What analysts see*).

    Attributes:
        alert_uuid (str):
        svs_status (None | str | Unset): test, test?, partial or mismatch; null for none
        runs (list[AlertSVSRun] | Unset): the runs whose attributions hold, oldest first
        detections (list[AlertSVSDetection] | Unset): the attributed detections
        mismatches (list[AlertSVSMismatch] | Unset): the markers in the alert that disagree with their run
    """

    alert_uuid: str
    svs_status: None | str | Unset = UNSET
    runs: list[AlertSVSRun] | Unset = UNSET
    detections: list[AlertSVSDetection] | Unset = UNSET
    mismatches: list[AlertSVSMismatch] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_uuid = self.alert_uuid

        svs_status: None | str | Unset
        if isinstance(self.svs_status, Unset):
            svs_status = UNSET
        else:
            svs_status = self.svs_status

        runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.runs, Unset):
            runs = []
            for runs_item_data in self.runs:
                runs_item = runs_item_data.to_dict()
                runs.append(runs_item)

        detections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.detections, Unset):
            detections = []
            for detections_item_data in self.detections:
                detections_item = detections_item_data.to_dict()
                detections.append(detections_item)

        mismatches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mismatches, Unset):
            mismatches = []
            for mismatches_item_data in self.mismatches:
                mismatches_item = mismatches_item_data.to_dict()
                mismatches.append(mismatches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_uuid": alert_uuid,
            }
        )
        if svs_status is not UNSET:
            field_dict["svs_status"] = svs_status
        if runs is not UNSET:
            field_dict["runs"] = runs
        if detections is not UNSET:
            field_dict["detections"] = detections
        if mismatches is not UNSET:
            field_dict["mismatches"] = mismatches

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_svs_detection import AlertSVSDetection
        from ..models.alert_svs_mismatch import AlertSVSMismatch
        from ..models.alert_svs_run import AlertSVSRun

        d = dict(src_dict)
        alert_uuid = d.pop("alert_uuid")

        def _parse_svs_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        svs_status = _parse_svs_status(d.pop("svs_status", UNSET))

        _runs = d.pop("runs", UNSET)
        runs: list[AlertSVSRun] | Unset = UNSET
        if _runs is not UNSET:
            runs = []
            for runs_item_data in _runs:
                runs_item = AlertSVSRun.from_dict(runs_item_data)

                runs.append(runs_item)

        _detections = d.pop("detections", UNSET)
        detections: list[AlertSVSDetection] | Unset = UNSET
        if _detections is not UNSET:
            detections = []
            for detections_item_data in _detections:
                detections_item = AlertSVSDetection.from_dict(detections_item_data)

                detections.append(detections_item)

        _mismatches = d.pop("mismatches", UNSET)
        mismatches: list[AlertSVSMismatch] | Unset = UNSET
        if _mismatches is not UNSET:
            mismatches = []
            for mismatches_item_data in _mismatches:
                mismatches_item = AlertSVSMismatch.from_dict(mismatches_item_data)

                mismatches.append(mismatches_item)

        alert_svs = cls(
            alert_uuid=alert_uuid,
            svs_status=svs_status,
            runs=runs,
            detections=detections,
            mismatches=mismatches,
        )

        alert_svs.additional_properties = d
        return alert_svs

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
