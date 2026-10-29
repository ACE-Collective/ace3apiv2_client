from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.observation_source import ObservationSource
from ..models.run_validation_decision import RunValidationDecision
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_validation_target import RunValidationTarget


T = TypeVar("T", bound="RunValidation")


@_attrs_define
class RunValidation:
    """What POST /api/v2/svs/runs/ would decide for the same body, decided without changing anything.

    Attributes:
        decision (RunValidationDecision):
        status_code (int): what registering would answer: 201, 403, 409 or 422
        targets (list[RunValidationTarget]): every target, judged as registering would; empty when the registration is
            invalid before its targets are judged
        message (None | str | Unset): why the registration is invalid: the 422's detail
        platform (None | str | Unset): the platform the run would be on, when accepted
        observation_seconds (int | None | Unset): when accepted
        observation_source (None | ObservationSource | Unset): where the observation window comes from: override,
            expected or all_hunts
        attribution_seconds (int | None | Unset): when accepted
        holds_host (bool | None | Unset): when accepted: the run would hold its hosts until its attribution window ends
    """

    decision: RunValidationDecision
    status_code: int
    targets: list[RunValidationTarget]
    message: None | str | Unset = UNSET
    platform: None | str | Unset = UNSET
    observation_seconds: int | None | Unset = UNSET
    observation_source: None | ObservationSource | Unset = UNSET
    attribution_seconds: int | None | Unset = UNSET
    holds_host: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        decision = self.decision.value

        status_code = self.status_code

        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        observation_seconds: int | None | Unset
        if isinstance(self.observation_seconds, Unset):
            observation_seconds = UNSET
        else:
            observation_seconds = self.observation_seconds

        observation_source: None | str | Unset
        if isinstance(self.observation_source, Unset):
            observation_source = UNSET
        elif isinstance(self.observation_source, ObservationSource):
            observation_source = self.observation_source.value
        else:
            observation_source = self.observation_source

        attribution_seconds: int | None | Unset
        if isinstance(self.attribution_seconds, Unset):
            attribution_seconds = UNSET
        else:
            attribution_seconds = self.attribution_seconds

        holds_host: bool | None | Unset
        if isinstance(self.holds_host, Unset):
            holds_host = UNSET
        else:
            holds_host = self.holds_host

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "decision": decision,
                "status_code": status_code,
                "targets": targets,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if platform is not UNSET:
            field_dict["platform"] = platform
        if observation_seconds is not UNSET:
            field_dict["observation_seconds"] = observation_seconds
        if observation_source is not UNSET:
            field_dict["observation_source"] = observation_source
        if attribution_seconds is not UNSET:
            field_dict["attribution_seconds"] = attribution_seconds
        if holds_host is not UNSET:
            field_dict["holds_host"] = holds_host

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.run_validation_target import RunValidationTarget

        d = dict(src_dict)
        decision = RunValidationDecision(d.pop("decision"))

        status_code = d.pop("status_code")

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = RunValidationTarget.from_dict(targets_item_data)

            targets.append(targets_item)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        def _parse_observation_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        observation_seconds = _parse_observation_seconds(
            d.pop("observation_seconds", UNSET)
        )

        def _parse_observation_source(data: object) -> None | ObservationSource | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                observation_source_type_0 = ObservationSource(data)

                return observation_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ObservationSource | Unset, data)

        observation_source = _parse_observation_source(
            d.pop("observation_source", UNSET)
        )

        def _parse_attribution_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        attribution_seconds = _parse_attribution_seconds(
            d.pop("attribution_seconds", UNSET)
        )

        def _parse_holds_host(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        holds_host = _parse_holds_host(d.pop("holds_host", UNSET))

        run_validation = cls(
            decision=decision,
            status_code=status_code,
            targets=targets,
            message=message,
            platform=platform,
            observation_seconds=observation_seconds,
            observation_source=observation_source,
            attribution_seconds=attribution_seconds,
            holds_host=holds_host,
        )

        run_validation.additional_properties = d
        return run_validation

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
