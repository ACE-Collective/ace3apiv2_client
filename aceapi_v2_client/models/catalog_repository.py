from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogRepository")


@_attrs_define
class CatalogRepository:
    """A catalog repository and the commit the catalog reflects (docs/SVS_RUNS.md, *The Atomic Red
    Team catalog*).

        Attributes:
            name (str): the name of its git_repo_* section
            configured (bool): it is in svs.catalog.repositories; one that isn't is listed while it has a row
            test_count (int): the tests read from that commit
            skipped_count (int): tests and files that read could not use
            removed_count (int): its tests removed from the catalog
            retired (bool): taken out of svs.catalog.repositories, so its tests were removed
            git_url (None | str | Unset): from its git_repo_* section, without credentials; null without one
            branch (None | str | Unset): from its git_repo_* section
            commit (None | str | Unset): the commit the catalog's tests were last read from; null until it is first read
            refreshed_at (datetime.datetime | None | Unset): when that commit was read
            error (None | str | Unset): why the last refresh failed; null when it succeeded. The catalog keeps the tests of
                the commit it last read
    """

    name: str
    configured: bool
    test_count: int
    skipped_count: int
    removed_count: int
    retired: bool
    git_url: None | str | Unset = UNSET
    branch: None | str | Unset = UNSET
    commit: None | str | Unset = UNSET
    refreshed_at: datetime.datetime | None | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        configured = self.configured

        test_count = self.test_count

        skipped_count = self.skipped_count

        removed_count = self.removed_count

        retired = self.retired

        git_url: None | str | Unset
        if isinstance(self.git_url, Unset):
            git_url = UNSET
        else:
            git_url = self.git_url

        branch: None | str | Unset
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        commit: None | str | Unset
        if isinstance(self.commit, Unset):
            commit = UNSET
        else:
            commit = self.commit

        refreshed_at: None | str | Unset
        if isinstance(self.refreshed_at, Unset):
            refreshed_at = UNSET
        elif isinstance(self.refreshed_at, datetime.datetime):
            refreshed_at = self.refreshed_at.isoformat()
        else:
            refreshed_at = self.refreshed_at

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "configured": configured,
                "test_count": test_count,
                "skipped_count": skipped_count,
                "removed_count": removed_count,
                "retired": retired,
            }
        )
        if git_url is not UNSET:
            field_dict["git_url"] = git_url
        if branch is not UNSET:
            field_dict["branch"] = branch
        if commit is not UNSET:
            field_dict["commit"] = commit
        if refreshed_at is not UNSET:
            field_dict["refreshed_at"] = refreshed_at
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        configured = d.pop("configured")

        test_count = d.pop("test_count")

        skipped_count = d.pop("skipped_count")

        removed_count = d.pop("removed_count")

        retired = d.pop("retired")

        def _parse_git_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        git_url = _parse_git_url(d.pop("git_url", UNSET))

        def _parse_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch = _parse_branch(d.pop("branch", UNSET))

        def _parse_commit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit = _parse_commit(d.pop("commit", UNSET))

        def _parse_refreshed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                refreshed_at_type_0 = datetime.datetime.fromisoformat(data)

                return refreshed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        refreshed_at = _parse_refreshed_at(d.pop("refreshed_at", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        catalog_repository = cls(
            name=name,
            configured=configured,
            test_count=test_count,
            skipped_count=skipped_count,
            removed_count=removed_count,
            retired=retired,
            git_url=git_url,
            branch=branch,
            commit=commit,
            refreshed_at=refreshed_at,
            error=error,
        )

        catalog_repository.additional_properties = d
        return catalog_repository

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
