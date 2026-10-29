from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.run_state import RunState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_target import RunTarget


T = TypeVar("T", bound="RunLifecycle")


@_attrs_define
class RunLifecycle:
    """A run as the launcher's calls return it.

    Attributes:
        run_id (str): the run's uuid
        marker (str): put this where the test's process telemetry shows it (docs/SVS_RUNS.md, *The marker*)
        state (RunState): Where a test run is (docs/SVS_RUNS.md, *Run states and timers*).
        test_guid (str):
        platform (str): the platform the run is on, an ATT&CK platform slug: its targets' test hosts' platform, else the
            test's only supported platform (docs/SVS_RUNS.md, *Registering a run*)
        targets (list[RunTarget]):
        observation_seconds (int): how long after start the run waits for its alerts before it ends
        attribution_seconds (int): how long after start its alerts are still attributed to it
        holds_host (bool): the run holds its hosts until its attribution window ends, not its observation window (its
            test's settings)
        created_at (datetime.datetime):
        started_at (datetime.datetime | None | Unset):
        cleanup_at (datetime.datetime | None | Unset): when the launcher said the test's cleanup began
        observation_ends_at (datetime.datetime | None | Unset):
        attribution_ends_at (datetime.datetime | None | Unset):
        error_reason (None | str | Unset):
        close_reason (None | str | Unset):
    """

    run_id: str
    marker: str
    state: RunState
    test_guid: str
    platform: str
    targets: list[RunTarget]
    observation_seconds: int
    attribution_seconds: int
    holds_host: bool
    created_at: datetime.datetime
    started_at: datetime.datetime | None | Unset = UNSET
    cleanup_at: datetime.datetime | None | Unset = UNSET
    observation_ends_at: datetime.datetime | None | Unset = UNSET
    attribution_ends_at: datetime.datetime | None | Unset = UNSET
    error_reason: None | str | Unset = UNSET
    close_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        marker = self.marker

        state = self.state.value

        test_guid = self.test_guid

        platform = self.platform

        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        observation_seconds = self.observation_seconds

        attribution_seconds = self.attribution_seconds

        holds_host = self.holds_host

        created_at = self.created_at.isoformat()

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        cleanup_at: None | str | Unset
        if isinstance(self.cleanup_at, Unset):
            cleanup_at = UNSET
        elif isinstance(self.cleanup_at, datetime.datetime):
            cleanup_at = self.cleanup_at.isoformat()
        else:
            cleanup_at = self.cleanup_at

        observation_ends_at: None | str | Unset
        if isinstance(self.observation_ends_at, Unset):
            observation_ends_at = UNSET
        elif isinstance(self.observation_ends_at, datetime.datetime):
            observation_ends_at = self.observation_ends_at.isoformat()
        else:
            observation_ends_at = self.observation_ends_at

        attribution_ends_at: None | str | Unset
        if isinstance(self.attribution_ends_at, Unset):
            attribution_ends_at = UNSET
        elif isinstance(self.attribution_ends_at, datetime.datetime):
            attribution_ends_at = self.attribution_ends_at.isoformat()
        else:
            attribution_ends_at = self.attribution_ends_at

        error_reason: None | str | Unset
        if isinstance(self.error_reason, Unset):
            error_reason = UNSET
        else:
            error_reason = self.error_reason

        close_reason: None | str | Unset
        if isinstance(self.close_reason, Unset):
            close_reason = UNSET
        else:
            close_reason = self.close_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run_id": run_id,
                "marker": marker,
                "state": state,
                "test_guid": test_guid,
                "platform": platform,
                "targets": targets,
                "observation_seconds": observation_seconds,
                "attribution_seconds": attribution_seconds,
                "holds_host": holds_host,
                "created_at": created_at,
            }
        )
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if cleanup_at is not UNSET:
            field_dict["cleanup_at"] = cleanup_at
        if observation_ends_at is not UNSET:
            field_dict["observation_ends_at"] = observation_ends_at
        if attribution_ends_at is not UNSET:
            field_dict["attribution_ends_at"] = attribution_ends_at
        if error_reason is not UNSET:
            field_dict["error_reason"] = error_reason
        if close_reason is not UNSET:
            field_dict["close_reason"] = close_reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.run_target import RunTarget

        d = dict(src_dict)
        run_id = d.pop("run_id")

        marker = d.pop("marker")

        state = RunState(d.pop("state"))

        test_guid = d.pop("test_guid")

        platform = d.pop("platform")

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = RunTarget.from_dict(targets_item_data)

            targets.append(targets_item)

        observation_seconds = d.pop("observation_seconds")

        attribution_seconds = d.pop("attribution_seconds")

        holds_host = d.pop("holds_host")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_cleanup_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cleanup_at_type_0 = datetime.datetime.fromisoformat(data)

                return cleanup_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cleanup_at = _parse_cleanup_at(d.pop("cleanup_at", UNSET))

        def _parse_observation_ends_at(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                observation_ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return observation_ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        observation_ends_at = _parse_observation_ends_at(
            d.pop("observation_ends_at", UNSET)
        )

        def _parse_attribution_ends_at(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                attribution_ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return attribution_ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        attribution_ends_at = _parse_attribution_ends_at(
            d.pop("attribution_ends_at", UNSET)
        )

        def _parse_error_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_reason = _parse_error_reason(d.pop("error_reason", UNSET))

        def _parse_close_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        close_reason = _parse_close_reason(d.pop("close_reason", UNSET))

        run_lifecycle = cls(
            run_id=run_id,
            marker=marker,
            state=state,
            test_guid=test_guid,
            platform=platform,
            targets=targets,
            observation_seconds=observation_seconds,
            attribution_seconds=attribution_seconds,
            holds_host=holds_host,
            created_at=created_at,
            started_at=started_at,
            cleanup_at=cleanup_at,
            observation_ends_at=observation_ends_at,
            attribution_ends_at=attribution_ends_at,
            error_reason=error_reason,
            close_reason=close_reason,
        )

        run_lifecycle.additional_properties = d
        return run_lifecycle

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
