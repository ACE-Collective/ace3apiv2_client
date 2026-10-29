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


T = TypeVar("T", bound="RunRow")


@_attrs_define
class RunRow:
    """A run as the runs screen lists it.

    Attributes:
        run_id (str): the run's uuid
        state (RunState): Where a test run is (docs/SVS_RUNS.md, *Run states and timers*).
        test_guid (str): the catalog test (/api/v2/svs/tests/{guid})
        platform (str): the platform the run is on, an ATT&CK platform slug: its targets' test hosts' platform, else the
            test's only supported platform (docs/SVS_RUNS.md, *Registering a run*)
        marker (str): the run's marker; svs_marker in ACE's logs
        targets (list[RunTarget]):
        launcher (str):
        created_at (datetime.datetime): when the run was registered
        changed_since_review (bool): a late alert or a manual association came after the review
        needs_attention (bool): the run is in the Needs attention view (docs/SVS_API.md, *Runs*)
        updated_at (datetime.datetime): when the row last changed; the changed_since key. A change to its result or
            alerts doesn't change it: pull GET /svs/runs/results
        test_name (None | str | Unset): from the catalog
        technique (None | str | Unset): the test's ATT&CK technique, from the catalog
        technique_name (None | str | Unset):
        batch_id (None | str | Unset):
        started_at (datetime.datetime | None | Unset):
        executed_at (datetime.datetime | None | Unset): when the launcher reported how the test executed
        exit_code (int | None | Unset):
        cleanup_at (datetime.datetime | None | Unset): when the launcher said the test's cleanup began: detections after
            it are the cleanup's
        ended_at (datetime.datetime | None | Unset):
        end_reason (None | str | Unset): why a person ended it before its observation window passed; null when the
            window passed
        canceled_at (datetime.datetime | None | Unset):
        closed_at (datetime.datetime | None | Unset):
        observation_ends_at (datetime.datetime | None | Unset): when a started run ends; moved to the end when a person
            ends it early
        attribution_ends_at (datetime.datetime | None | Unset): until when alerts are attributed to it
        error_reason (None | str | Unset):
        close_reason (None | str | Unset):
        owner (None | str | Unset): the owner's username
        reviewer (None | str | Unset): who reviewed it, by username
        reviewed_at (datetime.datetime | None | Unset):
        result_hit (int | Unset): expected signatures that fired (docs/SVS_API.md, *Results*) Default: 0.
        result_expected (int | Unset): the expected signatures the result judged: hit, missing or possibly suppressed
            Default: 0.
        result_missing (int | Unset): expected signatures that didn't fire, possibly suppressed ones included Default:
            0.
        result_possibly_suppressed (int | Unset):  Default: 0.
        result_candidate (int | Unset): signatures that fired and nobody has decided about Default: 0.
        result_rejected (int | Unset):  Default: 0.
        result_ignored (int | Unset):  Default: 0.
        result_cleanup (int | Unset): signatures that fired only during the test's cleanup Default: 0.
        result_stale (bool | Unset): the result is about to be recomputed Default: False.
        reviewed_hit (int | Unset): result_hit as signed off at the run's latest review; 0 until it is reviewed Default:
            0.
        reviewed_expected (int | Unset): result_expected as signed off Default: 0.
        reviewed_missing (int | Unset): result_missing as signed off, possibly suppressed ones included Default: 0.
        reviewed_possibly_suppressed (int | Unset): result_possibly_suppressed as signed off Default: 0.
        alerts (int | Unset): the alerts attributed to the run Default: 0.
        marker_alerts (int | Unset): of those, attributed by a marker Default: 0.
        context_alerts (int | Unset): of those, attributed by context alone (TEST?) Default: 0.
        late_alerts (int | Unset): of those, late Default: 0.
    """

    run_id: str
    state: RunState
    test_guid: str
    platform: str
    marker: str
    targets: list[RunTarget]
    launcher: str
    created_at: datetime.datetime
    changed_since_review: bool
    needs_attention: bool
    updated_at: datetime.datetime
    test_name: None | str | Unset = UNSET
    technique: None | str | Unset = UNSET
    technique_name: None | str | Unset = UNSET
    batch_id: None | str | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    executed_at: datetime.datetime | None | Unset = UNSET
    exit_code: int | None | Unset = UNSET
    cleanup_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    end_reason: None | str | Unset = UNSET
    canceled_at: datetime.datetime | None | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    observation_ends_at: datetime.datetime | None | Unset = UNSET
    attribution_ends_at: datetime.datetime | None | Unset = UNSET
    error_reason: None | str | Unset = UNSET
    close_reason: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    reviewer: None | str | Unset = UNSET
    reviewed_at: datetime.datetime | None | Unset = UNSET
    result_hit: int | Unset = 0
    result_expected: int | Unset = 0
    result_missing: int | Unset = 0
    result_possibly_suppressed: int | Unset = 0
    result_candidate: int | Unset = 0
    result_rejected: int | Unset = 0
    result_ignored: int | Unset = 0
    result_cleanup: int | Unset = 0
    result_stale: bool | Unset = False
    reviewed_hit: int | Unset = 0
    reviewed_expected: int | Unset = 0
    reviewed_missing: int | Unset = 0
    reviewed_possibly_suppressed: int | Unset = 0
    alerts: int | Unset = 0
    marker_alerts: int | Unset = 0
    context_alerts: int | Unset = 0
    late_alerts: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        state = self.state.value

        test_guid = self.test_guid

        platform = self.platform

        marker = self.marker

        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        launcher = self.launcher

        created_at = self.created_at.isoformat()

        changed_since_review = self.changed_since_review

        needs_attention = self.needs_attention

        updated_at = self.updated_at.isoformat()

        test_name: None | str | Unset
        if isinstance(self.test_name, Unset):
            test_name = UNSET
        else:
            test_name = self.test_name

        technique: None | str | Unset
        if isinstance(self.technique, Unset):
            technique = UNSET
        else:
            technique = self.technique

        technique_name: None | str | Unset
        if isinstance(self.technique_name, Unset):
            technique_name = UNSET
        else:
            technique_name = self.technique_name

        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        executed_at: None | str | Unset
        if isinstance(self.executed_at, Unset):
            executed_at = UNSET
        elif isinstance(self.executed_at, datetime.datetime):
            executed_at = self.executed_at.isoformat()
        else:
            executed_at = self.executed_at

        exit_code: int | None | Unset
        if isinstance(self.exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = self.exit_code

        cleanup_at: None | str | Unset
        if isinstance(self.cleanup_at, Unset):
            cleanup_at = UNSET
        elif isinstance(self.cleanup_at, datetime.datetime):
            cleanup_at = self.cleanup_at.isoformat()
        else:
            cleanup_at = self.cleanup_at

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        end_reason: None | str | Unset
        if isinstance(self.end_reason, Unset):
            end_reason = UNSET
        else:
            end_reason = self.end_reason

        canceled_at: None | str | Unset
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        elif isinstance(self.canceled_at, datetime.datetime):
            canceled_at = self.canceled_at.isoformat()
        else:
            canceled_at = self.canceled_at

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

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

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        reviewer: None | str | Unset
        if isinstance(self.reviewer, Unset):
            reviewer = UNSET
        else:
            reviewer = self.reviewer

        reviewed_at: None | str | Unset
        if isinstance(self.reviewed_at, Unset):
            reviewed_at = UNSET
        elif isinstance(self.reviewed_at, datetime.datetime):
            reviewed_at = self.reviewed_at.isoformat()
        else:
            reviewed_at = self.reviewed_at

        result_hit = self.result_hit

        result_expected = self.result_expected

        result_missing = self.result_missing

        result_possibly_suppressed = self.result_possibly_suppressed

        result_candidate = self.result_candidate

        result_rejected = self.result_rejected

        result_ignored = self.result_ignored

        result_cleanup = self.result_cleanup

        result_stale = self.result_stale

        reviewed_hit = self.reviewed_hit

        reviewed_expected = self.reviewed_expected

        reviewed_missing = self.reviewed_missing

        reviewed_possibly_suppressed = self.reviewed_possibly_suppressed

        alerts = self.alerts

        marker_alerts = self.marker_alerts

        context_alerts = self.context_alerts

        late_alerts = self.late_alerts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run_id": run_id,
                "state": state,
                "test_guid": test_guid,
                "platform": platform,
                "marker": marker,
                "targets": targets,
                "launcher": launcher,
                "created_at": created_at,
                "changed_since_review": changed_since_review,
                "needs_attention": needs_attention,
                "updated_at": updated_at,
            }
        )
        if test_name is not UNSET:
            field_dict["test_name"] = test_name
        if technique is not UNSET:
            field_dict["technique"] = technique
        if technique_name is not UNSET:
            field_dict["technique_name"] = technique_name
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if executed_at is not UNSET:
            field_dict["executed_at"] = executed_at
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if cleanup_at is not UNSET:
            field_dict["cleanup_at"] = cleanup_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if end_reason is not UNSET:
            field_dict["end_reason"] = end_reason
        if canceled_at is not UNSET:
            field_dict["canceled_at"] = canceled_at
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if observation_ends_at is not UNSET:
            field_dict["observation_ends_at"] = observation_ends_at
        if attribution_ends_at is not UNSET:
            field_dict["attribution_ends_at"] = attribution_ends_at
        if error_reason is not UNSET:
            field_dict["error_reason"] = error_reason
        if close_reason is not UNSET:
            field_dict["close_reason"] = close_reason
        if owner is not UNSET:
            field_dict["owner"] = owner
        if reviewer is not UNSET:
            field_dict["reviewer"] = reviewer
        if reviewed_at is not UNSET:
            field_dict["reviewed_at"] = reviewed_at
        if result_hit is not UNSET:
            field_dict["result_hit"] = result_hit
        if result_expected is not UNSET:
            field_dict["result_expected"] = result_expected
        if result_missing is not UNSET:
            field_dict["result_missing"] = result_missing
        if result_possibly_suppressed is not UNSET:
            field_dict["result_possibly_suppressed"] = result_possibly_suppressed
        if result_candidate is not UNSET:
            field_dict["result_candidate"] = result_candidate
        if result_rejected is not UNSET:
            field_dict["result_rejected"] = result_rejected
        if result_ignored is not UNSET:
            field_dict["result_ignored"] = result_ignored
        if result_cleanup is not UNSET:
            field_dict["result_cleanup"] = result_cleanup
        if result_stale is not UNSET:
            field_dict["result_stale"] = result_stale
        if reviewed_hit is not UNSET:
            field_dict["reviewed_hit"] = reviewed_hit
        if reviewed_expected is not UNSET:
            field_dict["reviewed_expected"] = reviewed_expected
        if reviewed_missing is not UNSET:
            field_dict["reviewed_missing"] = reviewed_missing
        if reviewed_possibly_suppressed is not UNSET:
            field_dict["reviewed_possibly_suppressed"] = reviewed_possibly_suppressed
        if alerts is not UNSET:
            field_dict["alerts"] = alerts
        if marker_alerts is not UNSET:
            field_dict["marker_alerts"] = marker_alerts
        if context_alerts is not UNSET:
            field_dict["context_alerts"] = context_alerts
        if late_alerts is not UNSET:
            field_dict["late_alerts"] = late_alerts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.run_target import RunTarget

        d = dict(src_dict)
        run_id = d.pop("run_id")

        state = RunState(d.pop("state"))

        test_guid = d.pop("test_guid")

        platform = d.pop("platform")

        marker = d.pop("marker")

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = RunTarget.from_dict(targets_item_data)

            targets.append(targets_item)

        launcher = d.pop("launcher")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        changed_since_review = d.pop("changed_since_review")

        needs_attention = d.pop("needs_attention")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_test_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        test_name = _parse_test_name(d.pop("test_name", UNSET))

        def _parse_technique(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        technique = _parse_technique(d.pop("technique", UNSET))

        def _parse_technique_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        technique_name = _parse_technique_name(d.pop("technique_name", UNSET))

        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batch_id", UNSET))

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

        def _parse_executed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                executed_at_type_0 = datetime.datetime.fromisoformat(data)

                return executed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        executed_at = _parse_executed_at(d.pop("executed_at", UNSET))

        def _parse_exit_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exit_code = _parse_exit_code(d.pop("exit_code", UNSET))

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

        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        def _parse_end_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_reason = _parse_end_reason(d.pop("end_reason", UNSET))

        def _parse_canceled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                canceled_at_type_0 = datetime.datetime.fromisoformat(data)

                return canceled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        canceled_at = _parse_canceled_at(d.pop("canceled_at", UNSET))

        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

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

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_reviewer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reviewer = _parse_reviewer(d.pop("reviewer", UNSET))

        def _parse_reviewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_at_type_0 = datetime.datetime.fromisoformat(data)

                return reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewed_at", UNSET))

        result_hit = d.pop("result_hit", UNSET)

        result_expected = d.pop("result_expected", UNSET)

        result_missing = d.pop("result_missing", UNSET)

        result_possibly_suppressed = d.pop("result_possibly_suppressed", UNSET)

        result_candidate = d.pop("result_candidate", UNSET)

        result_rejected = d.pop("result_rejected", UNSET)

        result_ignored = d.pop("result_ignored", UNSET)

        result_cleanup = d.pop("result_cleanup", UNSET)

        result_stale = d.pop("result_stale", UNSET)

        reviewed_hit = d.pop("reviewed_hit", UNSET)

        reviewed_expected = d.pop("reviewed_expected", UNSET)

        reviewed_missing = d.pop("reviewed_missing", UNSET)

        reviewed_possibly_suppressed = d.pop("reviewed_possibly_suppressed", UNSET)

        alerts = d.pop("alerts", UNSET)

        marker_alerts = d.pop("marker_alerts", UNSET)

        context_alerts = d.pop("context_alerts", UNSET)

        late_alerts = d.pop("late_alerts", UNSET)

        run_row = cls(
            run_id=run_id,
            state=state,
            test_guid=test_guid,
            platform=platform,
            marker=marker,
            targets=targets,
            launcher=launcher,
            created_at=created_at,
            changed_since_review=changed_since_review,
            needs_attention=needs_attention,
            updated_at=updated_at,
            test_name=test_name,
            technique=technique,
            technique_name=technique_name,
            batch_id=batch_id,
            started_at=started_at,
            executed_at=executed_at,
            exit_code=exit_code,
            cleanup_at=cleanup_at,
            ended_at=ended_at,
            end_reason=end_reason,
            canceled_at=canceled_at,
            closed_at=closed_at,
            observation_ends_at=observation_ends_at,
            attribution_ends_at=attribution_ends_at,
            error_reason=error_reason,
            close_reason=close_reason,
            owner=owner,
            reviewer=reviewer,
            reviewed_at=reviewed_at,
            result_hit=result_hit,
            result_expected=result_expected,
            result_missing=result_missing,
            result_possibly_suppressed=result_possibly_suppressed,
            result_candidate=result_candidate,
            result_rejected=result_rejected,
            result_ignored=result_ignored,
            result_cleanup=result_cleanup,
            result_stale=result_stale,
            reviewed_hit=reviewed_hit,
            reviewed_expected=reviewed_expected,
            reviewed_missing=reviewed_missing,
            reviewed_possibly_suppressed=reviewed_possibly_suppressed,
            alerts=alerts,
            marker_alerts=marker_alerts,
            context_alerts=context_alerts,
            late_alerts=late_alerts,
        )

        run_row.additional_properties = d
        return run_row

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
