from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_svs_run import AlertSVSRun


T = TypeVar("T", bound="AlertSVSMismatch")


@_attrs_define
class AlertSVSMismatch:
    """
    Attributes:
        marker (str):
        result (str): how it disagrees with its run: unknown, other host or outside window
        run (AlertSVSRun | None | Unset): the run the marker belongs to; null when no run has it
    """

    marker: str
    result: str
    run: AlertSVSRun | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alert_svs_run import AlertSVSRun

        marker = self.marker

        result = self.result

        run: dict[str, Any] | None | Unset
        if isinstance(self.run, Unset):
            run = UNSET
        elif isinstance(self.run, AlertSVSRun):
            run = self.run.to_dict()
        else:
            run = self.run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marker": marker,
                "result": result,
            }
        )
        if run is not UNSET:
            field_dict["run"] = run

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_svs_run import AlertSVSRun

        d = dict(src_dict)
        marker = d.pop("marker")

        result = d.pop("result")

        def _parse_run(data: object) -> AlertSVSRun | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                run_type_0 = AlertSVSRun.from_dict(data)

                return run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertSVSRun | None | Unset, data)

        run = _parse_run(d.pop("run", UNSET))

        alert_svs_mismatch = cls(
            marker=marker,
            result=result,
            run=run,
        )

        alert_svs_mismatch.additional_properties = d
        return alert_svs_mismatch

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
