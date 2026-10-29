from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hunt_validation_result_correlation_trace_type_0 import (
        HuntValidationResultCorrelationTraceType0,
    )
    from ..models.hunt_validation_result_roots_type_0_item import (
        HuntValidationResultRootsType0Item,
    )


T = TypeVar("T", bound="HuntValidationResult")


@_attrs_define
class HuntValidationResult:
    """
    Attributes:
        valid (bool):
        error (None | str | Unset): why the hunt is not valid, or why its run failed
        remote_status_code (int | None | Unset): the data source's status, when it refused the run
        roots (list[HuntValidationResultRootsType0Item] | None | Unset): what the run produced, with details
        logs (list[str] | None | Unset): every log line the run wrote
        correlation_trace (HuntValidationResultCorrelationTraceType0 | None | Unset):
        original_events (list[Any] | None | Unset): the events before correlation
        correlate_results (Any | None | Unset): the correlate queries' results, to replay
    """

    valid: bool
    error: None | str | Unset = UNSET
    remote_status_code: int | None | Unset = UNSET
    roots: list[HuntValidationResultRootsType0Item] | None | Unset = UNSET
    logs: list[str] | None | Unset = UNSET
    correlation_trace: HuntValidationResultCorrelationTraceType0 | None | Unset = UNSET
    original_events: list[Any] | None | Unset = UNSET
    correlate_results: Any | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hunt_validation_result_correlation_trace_type_0 import (
            HuntValidationResultCorrelationTraceType0,
        )

        valid = self.valid

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        remote_status_code: int | None | Unset
        if isinstance(self.remote_status_code, Unset):
            remote_status_code = UNSET
        else:
            remote_status_code = self.remote_status_code

        roots: list[dict[str, Any]] | None | Unset
        if isinstance(self.roots, Unset):
            roots = UNSET
        elif isinstance(self.roots, list):
            roots = []
            for roots_type_0_item_data in self.roots:
                roots_type_0_item = roots_type_0_item_data.to_dict()
                roots.append(roots_type_0_item)

        else:
            roots = self.roots

        logs: list[str] | None | Unset
        if isinstance(self.logs, Unset):
            logs = UNSET
        elif isinstance(self.logs, list):
            logs = self.logs

        else:
            logs = self.logs

        correlation_trace: dict[str, Any] | None | Unset
        if isinstance(self.correlation_trace, Unset):
            correlation_trace = UNSET
        elif isinstance(
            self.correlation_trace, HuntValidationResultCorrelationTraceType0
        ):
            correlation_trace = self.correlation_trace.to_dict()
        else:
            correlation_trace = self.correlation_trace

        original_events: list[Any] | None | Unset
        if isinstance(self.original_events, Unset):
            original_events = UNSET
        elif isinstance(self.original_events, list):
            original_events = self.original_events

        else:
            original_events = self.original_events

        correlate_results: Any | None | Unset
        if isinstance(self.correlate_results, Unset):
            correlate_results = UNSET
        else:
            correlate_results = self.correlate_results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valid": valid,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if remote_status_code is not UNSET:
            field_dict["remote_status_code"] = remote_status_code
        if roots is not UNSET:
            field_dict["roots"] = roots
        if logs is not UNSET:
            field_dict["logs"] = logs
        if correlation_trace is not UNSET:
            field_dict["correlation_trace"] = correlation_trace
        if original_events is not UNSET:
            field_dict["original_events"] = original_events
        if correlate_results is not UNSET:
            field_dict["correlate_results"] = correlate_results

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hunt_validation_result_correlation_trace_type_0 import (
            HuntValidationResultCorrelationTraceType0,
        )
        from ..models.hunt_validation_result_roots_type_0_item import (
            HuntValidationResultRootsType0Item,
        )

        d = dict(src_dict)
        valid = d.pop("valid")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_remote_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        remote_status_code = _parse_remote_status_code(
            d.pop("remote_status_code", UNSET)
        )

        def _parse_roots(
            data: object,
        ) -> list[HuntValidationResultRootsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                roots_type_0 = []
                _roots_type_0 = data
                for roots_type_0_item_data in _roots_type_0:
                    roots_type_0_item = HuntValidationResultRootsType0Item.from_dict(
                        roots_type_0_item_data
                    )

                    roots_type_0.append(roots_type_0_item)

                return roots_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HuntValidationResultRootsType0Item] | None | Unset, data)

        roots = _parse_roots(d.pop("roots", UNSET))

        def _parse_logs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                logs_type_0 = cast(list[str], data)

                return logs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        logs = _parse_logs(d.pop("logs", UNSET))

        def _parse_correlation_trace(
            data: object,
        ) -> HuntValidationResultCorrelationTraceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                correlation_trace_type_0 = (
                    HuntValidationResultCorrelationTraceType0.from_dict(data)
                )

                return correlation_trace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HuntValidationResultCorrelationTraceType0 | None | Unset, data)

        correlation_trace = _parse_correlation_trace(d.pop("correlation_trace", UNSET))

        def _parse_original_events(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                original_events_type_0 = cast(list[Any], data)

                return original_events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        original_events = _parse_original_events(d.pop("original_events", UNSET))

        def _parse_correlate_results(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        correlate_results = _parse_correlate_results(d.pop("correlate_results", UNSET))

        hunt_validation_result = cls(
            valid=valid,
            error=error,
            remote_status_code=remote_status_code,
            roots=roots,
            logs=logs,
            correlation_trace=correlation_trace,
            original_events=original_events,
            correlate_results=correlate_results,
        )

        hunt_validation_result.additional_properties = d
        return hunt_validation_result

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
