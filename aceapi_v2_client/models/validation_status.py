from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.validation_status_state import ValidationStatusState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compile_problem import CompileProblem
    from ..models.validation_status_counts_type_0 import ValidationStatusCountsType0
    from ..models.validation_status_rules import ValidationStatusRules


T = TypeVar("T", bound="ValidationStatus")


@_attrs_define
class ValidationStatus:
    """A validation as the signature repository's CI sees it (svs:validate): its state, counts, and
    rule names and uuids. It never carries a sample's sha256, file name or content.

        Attributes:
            uuid (str):
            state (ValidationStatusState):
            repository (str):
            base_sha (str):
            head_sha (str):
            branch (str):
            created_at (datetime.datetime):
            report_path (str): the report in the ACE GUI, relative to the GUI's host
            error (None | str | Unset): why a failed validation could not run
            pr_url (None | str | Unset):
            started_at (datetime.datetime | None | Unset):
            finished_at (datetime.datetime | None | Unset):
            diffed (bool | None | Unset): false when either commit's ruleset would not load, so nothing was compared
            counts (None | Unset | ValidationStatusCountsType0): pairs (sample, rule uuid) per category, every category
                included; set once completed
            rules (ValidationStatusRules | Unset): the rules with samples in each listed category, most samples first
            compile_errors (list[CompileProblem] | Unset): the head's rule files that do not compile; their rules are
                dropped
            ruleset_error (None | str | Unset): set when the head's rules would not load together: production keeps its
                previous rules
    """

    uuid: str
    state: ValidationStatusState
    repository: str
    base_sha: str
    head_sha: str
    branch: str
    created_at: datetime.datetime
    report_path: str
    error: None | str | Unset = UNSET
    pr_url: None | str | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    finished_at: datetime.datetime | None | Unset = UNSET
    diffed: bool | None | Unset = UNSET
    counts: None | Unset | ValidationStatusCountsType0 = UNSET
    rules: ValidationStatusRules | Unset = UNSET
    compile_errors: list[CompileProblem] | Unset = UNSET
    ruleset_error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.validation_status_counts_type_0 import ValidationStatusCountsType0

        uuid = self.uuid

        state = self.state.value

        repository = self.repository

        base_sha = self.base_sha

        head_sha = self.head_sha

        branch = self.branch

        created_at = self.created_at.isoformat()

        report_path = self.report_path

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        pr_url: None | str | Unset
        if isinstance(self.pr_url, Unset):
            pr_url = UNSET
        else:
            pr_url = self.pr_url

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

        diffed: bool | None | Unset
        if isinstance(self.diffed, Unset):
            diffed = UNSET
        else:
            diffed = self.diffed

        counts: dict[str, Any] | None | Unset
        if isinstance(self.counts, Unset):
            counts = UNSET
        elif isinstance(self.counts, ValidationStatusCountsType0):
            counts = self.counts.to_dict()
        else:
            counts = self.counts

        rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()

        compile_errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.compile_errors, Unset):
            compile_errors = []
            for compile_errors_item_data in self.compile_errors:
                compile_errors_item = compile_errors_item_data.to_dict()
                compile_errors.append(compile_errors_item)

        ruleset_error: None | str | Unset
        if isinstance(self.ruleset_error, Unset):
            ruleset_error = UNSET
        else:
            ruleset_error = self.ruleset_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "state": state,
                "repository": repository,
                "base_sha": base_sha,
                "head_sha": head_sha,
                "branch": branch,
                "created_at": created_at,
                "report_path": report_path,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if pr_url is not UNSET:
            field_dict["pr_url"] = pr_url
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if diffed is not UNSET:
            field_dict["diffed"] = diffed
        if counts is not UNSET:
            field_dict["counts"] = counts
        if rules is not UNSET:
            field_dict["rules"] = rules
        if compile_errors is not UNSET:
            field_dict["compile_errors"] = compile_errors
        if ruleset_error is not UNSET:
            field_dict["ruleset_error"] = ruleset_error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.compile_problem import CompileProblem
        from ..models.validation_status_counts_type_0 import ValidationStatusCountsType0
        from ..models.validation_status_rules import ValidationStatusRules

        d = dict(src_dict)
        uuid = d.pop("uuid")

        state = ValidationStatusState(d.pop("state"))

        repository = d.pop("repository")

        base_sha = d.pop("base_sha")

        head_sha = d.pop("head_sha")

        branch = d.pop("branch")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        report_path = d.pop("report_path")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_pr_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pr_url = _parse_pr_url(d.pop("pr_url", UNSET))

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

        def _parse_diffed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        diffed = _parse_diffed(d.pop("diffed", UNSET))

        def _parse_counts(data: object) -> None | Unset | ValidationStatusCountsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                counts_type_0 = ValidationStatusCountsType0.from_dict(data)

                return counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ValidationStatusCountsType0, data)

        counts = _parse_counts(d.pop("counts", UNSET))

        _rules = d.pop("rules", UNSET)
        rules: ValidationStatusRules | Unset
        if isinstance(_rules, Unset):
            rules = UNSET
        else:
            rules = ValidationStatusRules.from_dict(_rules)

        _compile_errors = d.pop("compile_errors", UNSET)
        compile_errors: list[CompileProblem] | Unset = UNSET
        if _compile_errors is not UNSET:
            compile_errors = []
            for compile_errors_item_data in _compile_errors:
                compile_errors_item = CompileProblem.from_dict(compile_errors_item_data)

                compile_errors.append(compile_errors_item)

        def _parse_ruleset_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ruleset_error = _parse_ruleset_error(d.pop("ruleset_error", UNSET))

        validation_status = cls(
            uuid=uuid,
            state=state,
            repository=repository,
            base_sha=base_sha,
            head_sha=head_sha,
            branch=branch,
            created_at=created_at,
            report_path=report_path,
            error=error,
            pr_url=pr_url,
            started_at=started_at,
            finished_at=finished_at,
            diffed=diffed,
            counts=counts,
            rules=rules,
            compile_errors=compile_errors,
            ruleset_error=ruleset_error,
        )

        validation_status.additional_properties = d
        return validation_status

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
