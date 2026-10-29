from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_test_detail_test import CatalogTestDetailTest
    from ..models.platform_state import PlatformState


T = TypeVar("T", bound="CatalogTestDetail")


@_attrs_define
class CatalogTestDetail:
    """
    Attributes:
        guid (str): the test's auto_generated_guid, lower case
        repository (str): the name of the git_repo_* section it is read from
        technique (str): the ATT&CK technique of its atomic file, e.g. T1059.001
        name (str):
        platforms (list[str]): its supported_platforms
        path (str): its atomic file, relative to the repository
        commit (str): the repository commit this version of the test was first read from
        content_hash (str): sha256 of the test's entry; it changes exactly when the test does
        first_seen_at (datetime.datetime):
        updated_at (datetime.datetime): when the catalog row last changed; the changed_since key. A change to the test's
            runs or state doesn't change it
        test_state (str): never_run, awaiting_review, no_expectations, failing, stale or validated: never_run without
            runs, else the worst of its platforms' states (docs/SVS_API.md, *Tests*)
        test (CatalogTestDetailTest): the test's entry in its atomic file: executor (commands), input_arguments,
            dependencies
        technique_name (None | str | Unset):
        executor (None | str | Unset): command_prompt, powershell, sh, bash or manual
        removed_at (datetime.datetime | None | Unset): when the test disappeared from its repository; it keeps its runs
        run_count (int | Unset): every run registered for it Default: 0.
        last_run_id (None | str | Unset): its latest run's uuid
        last_run_at (datetime.datetime | None | Unset): when its latest run was registered
        last_reviewed_run_id (None | str | Unset):
        last_reviewed_at (datetime.datetime | None | Unset):
        expected_signatures (int | Unset): signatures expected of it on any platform that no ignore applies to Default:
            0.
        recent_runs (int | Unset): its latest ended or reviewed runs looked at (at most 5) Default: 0.
        recent_runs_missing (int | Unset): of those, the runs that missed an expected signature Default: 0.
        platform_states (list[PlatformState] | Unset): each platform it supports or has a run or a decision on, by
            platform
        description (None | str | Unset):
    """

    guid: str
    repository: str
    technique: str
    name: str
    platforms: list[str]
    path: str
    commit: str
    content_hash: str
    first_seen_at: datetime.datetime
    updated_at: datetime.datetime
    test_state: str
    test: CatalogTestDetailTest
    technique_name: None | str | Unset = UNSET
    executor: None | str | Unset = UNSET
    removed_at: datetime.datetime | None | Unset = UNSET
    run_count: int | Unset = 0
    last_run_id: None | str | Unset = UNSET
    last_run_at: datetime.datetime | None | Unset = UNSET
    last_reviewed_run_id: None | str | Unset = UNSET
    last_reviewed_at: datetime.datetime | None | Unset = UNSET
    expected_signatures: int | Unset = 0
    recent_runs: int | Unset = 0
    recent_runs_missing: int | Unset = 0
    platform_states: list[PlatformState] | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guid = self.guid

        repository = self.repository

        technique = self.technique

        name = self.name

        platforms = self.platforms

        path = self.path

        commit = self.commit

        content_hash = self.content_hash

        first_seen_at = self.first_seen_at.isoformat()

        updated_at = self.updated_at.isoformat()

        test_state = self.test_state

        test = self.test.to_dict()

        technique_name: None | str | Unset
        if isinstance(self.technique_name, Unset):
            technique_name = UNSET
        else:
            technique_name = self.technique_name

        executor: None | str | Unset
        if isinstance(self.executor, Unset):
            executor = UNSET
        else:
            executor = self.executor

        removed_at: None | str | Unset
        if isinstance(self.removed_at, Unset):
            removed_at = UNSET
        elif isinstance(self.removed_at, datetime.datetime):
            removed_at = self.removed_at.isoformat()
        else:
            removed_at = self.removed_at

        run_count = self.run_count

        last_run_id: None | str | Unset
        if isinstance(self.last_run_id, Unset):
            last_run_id = UNSET
        else:
            last_run_id = self.last_run_id

        last_run_at: None | str | Unset
        if isinstance(self.last_run_at, Unset):
            last_run_at = UNSET
        elif isinstance(self.last_run_at, datetime.datetime):
            last_run_at = self.last_run_at.isoformat()
        else:
            last_run_at = self.last_run_at

        last_reviewed_run_id: None | str | Unset
        if isinstance(self.last_reviewed_run_id, Unset):
            last_reviewed_run_id = UNSET
        else:
            last_reviewed_run_id = self.last_reviewed_run_id

        last_reviewed_at: None | str | Unset
        if isinstance(self.last_reviewed_at, Unset):
            last_reviewed_at = UNSET
        elif isinstance(self.last_reviewed_at, datetime.datetime):
            last_reviewed_at = self.last_reviewed_at.isoformat()
        else:
            last_reviewed_at = self.last_reviewed_at

        expected_signatures = self.expected_signatures

        recent_runs = self.recent_runs

        recent_runs_missing = self.recent_runs_missing

        platform_states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.platform_states, Unset):
            platform_states = []
            for platform_states_item_data in self.platform_states:
                platform_states_item = platform_states_item_data.to_dict()
                platform_states.append(platform_states_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "guid": guid,
                "repository": repository,
                "technique": technique,
                "name": name,
                "platforms": platforms,
                "path": path,
                "commit": commit,
                "content_hash": content_hash,
                "first_seen_at": first_seen_at,
                "updated_at": updated_at,
                "test_state": test_state,
                "test": test,
            }
        )
        if technique_name is not UNSET:
            field_dict["technique_name"] = technique_name
        if executor is not UNSET:
            field_dict["executor"] = executor
        if removed_at is not UNSET:
            field_dict["removed_at"] = removed_at
        if run_count is not UNSET:
            field_dict["run_count"] = run_count
        if last_run_id is not UNSET:
            field_dict["last_run_id"] = last_run_id
        if last_run_at is not UNSET:
            field_dict["last_run_at"] = last_run_at
        if last_reviewed_run_id is not UNSET:
            field_dict["last_reviewed_run_id"] = last_reviewed_run_id
        if last_reviewed_at is not UNSET:
            field_dict["last_reviewed_at"] = last_reviewed_at
        if expected_signatures is not UNSET:
            field_dict["expected_signatures"] = expected_signatures
        if recent_runs is not UNSET:
            field_dict["recent_runs"] = recent_runs
        if recent_runs_missing is not UNSET:
            field_dict["recent_runs_missing"] = recent_runs_missing
        if platform_states is not UNSET:
            field_dict["platform_states"] = platform_states
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_test_detail_test import CatalogTestDetailTest
        from ..models.platform_state import PlatformState

        d = dict(src_dict)
        guid = d.pop("guid")

        repository = d.pop("repository")

        technique = d.pop("technique")

        name = d.pop("name")

        platforms = cast(list[str], d.pop("platforms"))

        path = d.pop("path")

        commit = d.pop("commit")

        content_hash = d.pop("content_hash")

        first_seen_at = datetime.datetime.fromisoformat(d.pop("first_seen_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        test_state = d.pop("test_state")

        test = CatalogTestDetailTest.from_dict(d.pop("test"))

        def _parse_technique_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        technique_name = _parse_technique_name(d.pop("technique_name", UNSET))

        def _parse_executor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        executor = _parse_executor(d.pop("executor", UNSET))

        def _parse_removed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                removed_at_type_0 = datetime.datetime.fromisoformat(data)

                return removed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        removed_at = _parse_removed_at(d.pop("removed_at", UNSET))

        run_count = d.pop("run_count", UNSET)

        def _parse_last_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_run_id = _parse_last_run_id(d.pop("last_run_id", UNSET))

        def _parse_last_run_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_run_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run_at = _parse_last_run_at(d.pop("last_run_at", UNSET))

        def _parse_last_reviewed_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_reviewed_run_id = _parse_last_reviewed_run_id(
            d.pop("last_reviewed_run_id", UNSET)
        )

        def _parse_last_reviewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_reviewed_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_reviewed_at = _parse_last_reviewed_at(d.pop("last_reviewed_at", UNSET))

        expected_signatures = d.pop("expected_signatures", UNSET)

        recent_runs = d.pop("recent_runs", UNSET)

        recent_runs_missing = d.pop("recent_runs_missing", UNSET)

        _platform_states = d.pop("platform_states", UNSET)
        platform_states: list[PlatformState] | Unset = UNSET
        if _platform_states is not UNSET:
            platform_states = []
            for platform_states_item_data in _platform_states:
                platform_states_item = PlatformState.from_dict(
                    platform_states_item_data
                )

                platform_states.append(platform_states_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        catalog_test_detail = cls(
            guid=guid,
            repository=repository,
            technique=technique,
            name=name,
            platforms=platforms,
            path=path,
            commit=commit,
            content_hash=content_hash,
            first_seen_at=first_seen_at,
            updated_at=updated_at,
            test_state=test_state,
            test=test,
            technique_name=technique_name,
            executor=executor,
            removed_at=removed_at,
            run_count=run_count,
            last_run_id=last_run_id,
            last_run_at=last_run_at,
            last_reviewed_run_id=last_reviewed_run_id,
            last_reviewed_at=last_reviewed_at,
            expected_signatures=expected_signatures,
            recent_runs=recent_runs,
            recent_runs_missing=recent_runs_missing,
            platform_states=platform_states,
            description=description,
        )

        catalog_test_detail.additional_properties = d
        return catalog_test_detail

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
