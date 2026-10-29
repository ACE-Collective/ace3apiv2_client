from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.validation_detail_state import ValidationDetailState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_detail_counts_type_0 import ValidationDetailCountsType0
    from ..models.validation_detail_report_type_0 import ValidationDetailReportType0


T = TypeVar("T", bound="ValidationDetail")


@_attrs_define
class ValidationDetail:
    """One validation with its report (signature:read).

    Attributes:
        uuid (str):
        repository (str):
        base_sha (str):
        head_sha (str):
        branch (str):
        state (ValidationDetailState):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        attempts (int): how many times a worker has claimed it
        pr_url (None | str | Unset):
        requested_by (None | str | Unset): the user whose key requested it
        started_at (datetime.datetime | None | Unset):
        finished_at (datetime.datetime | None | Unset):
        error (None | str | Unset):
        diffed (bool | None | Unset):
        regressions (int | None | Unset): regression + regression_unconfirmed
        new_fps (int | None | Unset): new_fp + new_fp_other_rule
        compile_errors (int | None | Unset): the head's rule files that do not compile, plus one if its ruleset would
            not load
        counts (None | Unset | ValidationDetailCountsType0):
        claimed_by (None | str | Unset): the node that ran (or runs) it
        corpus_version (None | str | Unset): what the samples and their labels were when it ran
        engine_fingerprint (None | str | Unset): what decided its results besides the corpus and the commits
        report (None | Unset | ValidationDetailReportType0): how each commit compiled, the rules added, removed and
            changed, the rules that cannot be tested, the samples skipped and the timings; its listed pairs are GET
            …/results
    """

    uuid: str
    repository: str
    base_sha: str
    head_sha: str
    branch: str
    state: ValidationDetailState
    created_at: datetime.datetime
    updated_at: datetime.datetime
    attempts: int
    pr_url: None | str | Unset = UNSET
    requested_by: None | str | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    finished_at: datetime.datetime | None | Unset = UNSET
    error: None | str | Unset = UNSET
    diffed: bool | None | Unset = UNSET
    regressions: int | None | Unset = UNSET
    new_fps: int | None | Unset = UNSET
    compile_errors: int | None | Unset = UNSET
    counts: None | Unset | ValidationDetailCountsType0 = UNSET
    claimed_by: None | str | Unset = UNSET
    corpus_version: None | str | Unset = UNSET
    engine_fingerprint: None | str | Unset = UNSET
    report: None | Unset | ValidationDetailReportType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.validation_detail_counts_type_0 import ValidationDetailCountsType0
        from ..models.validation_detail_report_type_0 import ValidationDetailReportType0

        uuid = self.uuid

        repository = self.repository

        base_sha = self.base_sha

        head_sha = self.head_sha

        branch = self.branch

        state = self.state.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        attempts = self.attempts

        pr_url: None | str | Unset
        if isinstance(self.pr_url, Unset):
            pr_url = UNSET
        else:
            pr_url = self.pr_url

        requested_by: None | str | Unset
        if isinstance(self.requested_by, Unset):
            requested_by = UNSET
        else:
            requested_by = self.requested_by

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        diffed: bool | None | Unset
        if isinstance(self.diffed, Unset):
            diffed = UNSET
        else:
            diffed = self.diffed

        regressions: int | None | Unset
        if isinstance(self.regressions, Unset):
            regressions = UNSET
        else:
            regressions = self.regressions

        new_fps: int | None | Unset
        if isinstance(self.new_fps, Unset):
            new_fps = UNSET
        else:
            new_fps = self.new_fps

        compile_errors: int | None | Unset
        if isinstance(self.compile_errors, Unset):
            compile_errors = UNSET
        else:
            compile_errors = self.compile_errors

        counts: dict[str, Any] | None | Unset
        if isinstance(self.counts, Unset):
            counts = UNSET
        elif isinstance(self.counts, ValidationDetailCountsType0):
            counts = self.counts.to_dict()
        else:
            counts = self.counts

        claimed_by: None | str | Unset
        if isinstance(self.claimed_by, Unset):
            claimed_by = UNSET
        else:
            claimed_by = self.claimed_by

        corpus_version: None | str | Unset
        if isinstance(self.corpus_version, Unset):
            corpus_version = UNSET
        else:
            corpus_version = self.corpus_version

        engine_fingerprint: None | str | Unset
        if isinstance(self.engine_fingerprint, Unset):
            engine_fingerprint = UNSET
        else:
            engine_fingerprint = self.engine_fingerprint

        report: dict[str, Any] | None | Unset
        if isinstance(self.report, Unset):
            report = UNSET
        elif isinstance(self.report, ValidationDetailReportType0):
            report = self.report.to_dict()
        else:
            report = self.report

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "repository": repository,
                "base_sha": base_sha,
                "head_sha": head_sha,
                "branch": branch,
                "state": state,
                "created_at": created_at,
                "updated_at": updated_at,
                "attempts": attempts,
            }
        )
        if pr_url is not UNSET:
            field_dict["pr_url"] = pr_url
        if requested_by is not UNSET:
            field_dict["requested_by"] = requested_by
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if error is not UNSET:
            field_dict["error"] = error
        if diffed is not UNSET:
            field_dict["diffed"] = diffed
        if regressions is not UNSET:
            field_dict["regressions"] = regressions
        if new_fps is not UNSET:
            field_dict["new_fps"] = new_fps
        if compile_errors is not UNSET:
            field_dict["compile_errors"] = compile_errors
        if counts is not UNSET:
            field_dict["counts"] = counts
        if claimed_by is not UNSET:
            field_dict["claimed_by"] = claimed_by
        if corpus_version is not UNSET:
            field_dict["corpus_version"] = corpus_version
        if engine_fingerprint is not UNSET:
            field_dict["engine_fingerprint"] = engine_fingerprint
        if report is not UNSET:
            field_dict["report"] = report

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.validation_detail_counts_type_0 import ValidationDetailCountsType0
        from ..models.validation_detail_report_type_0 import ValidationDetailReportType0

        d = dict(src_dict)
        uuid = d.pop("uuid")

        repository = d.pop("repository")

        base_sha = d.pop("base_sha")

        head_sha = d.pop("head_sha")

        branch = d.pop("branch")

        state = ValidationDetailState(d.pop("state"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        attempts = d.pop("attempts")

        def _parse_pr_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pr_url = _parse_pr_url(d.pop("pr_url", UNSET))

        def _parse_requested_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requested_by = _parse_requested_by(d.pop("requested_by", UNSET))

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

        def _parse_finished_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finished_at = _parse_finished_at(d.pop("finished_at", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_diffed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        diffed = _parse_diffed(d.pop("diffed", UNSET))

        def _parse_regressions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        regressions = _parse_regressions(d.pop("regressions", UNSET))

        def _parse_new_fps(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        new_fps = _parse_new_fps(d.pop("new_fps", UNSET))

        def _parse_compile_errors(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compile_errors = _parse_compile_errors(d.pop("compile_errors", UNSET))

        def _parse_counts(data: object) -> None | Unset | ValidationDetailCountsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                counts_type_0 = ValidationDetailCountsType0.from_dict(data)

                return counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ValidationDetailCountsType0, data)

        counts = _parse_counts(d.pop("counts", UNSET))

        def _parse_claimed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        claimed_by = _parse_claimed_by(d.pop("claimed_by", UNSET))

        def _parse_corpus_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        corpus_version = _parse_corpus_version(d.pop("corpus_version", UNSET))

        def _parse_engine_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        engine_fingerprint = _parse_engine_fingerprint(
            d.pop("engine_fingerprint", UNSET)
        )

        def _parse_report(data: object) -> None | Unset | ValidationDetailReportType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                report_type_0 = ValidationDetailReportType0.from_dict(data)

                return report_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ValidationDetailReportType0, data)

        report = _parse_report(d.pop("report", UNSET))

        validation_detail = cls(
            uuid=uuid,
            repository=repository,
            base_sha=base_sha,
            head_sha=head_sha,
            branch=branch,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            attempts=attempts,
            pr_url=pr_url,
            requested_by=requested_by,
            started_at=started_at,
            finished_at=finished_at,
            error=error,
            diffed=diffed,
            regressions=regressions,
            new_fps=new_fps,
            compile_errors=compile_errors,
            counts=counts,
            claimed_by=claimed_by,
            corpus_version=corpus_version,
            engine_fingerprint=engine_fingerprint,
            report=report,
        )

        validation_detail.additional_properties = d
        return validation_detail

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
