from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationRequest")


@_attrs_define
class ValidationRequest:
    """What the signature repository's CI asks for: validate head_sha against base_sha.

    Attributes:
        repository (str): the name of a git_repo_* section (its name field), listed in svs.yara.repositories
        base_sha (str): the full id of the commit to compare against: the pull request's merge base
        head_sha (str): the full id of the commit to validate
        branch (str): the branch head_sha is on
        pr_url (None | str | Unset): the pull request, for the report's link back
    """

    repository: str
    base_sha: str
    head_sha: str
    branch: str
    pr_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository = self.repository

        base_sha = self.base_sha

        head_sha = self.head_sha

        branch = self.branch

        pr_url: None | str | Unset
        if isinstance(self.pr_url, Unset):
            pr_url = UNSET
        else:
            pr_url = self.pr_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository": repository,
                "base_sha": base_sha,
                "head_sha": head_sha,
                "branch": branch,
            }
        )
        if pr_url is not UNSET:
            field_dict["pr_url"] = pr_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        repository = d.pop("repository")

        base_sha = d.pop("base_sha")

        head_sha = d.pop("head_sha")

        branch = d.pop("branch")

        def _parse_pr_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pr_url = _parse_pr_url(d.pop("pr_url", UNSET))

        validation_request = cls(
            repository=repository,
            base_sha=base_sha,
            head_sha=head_sha,
            branch=branch,
            pr_url=pr_url,
        )

        validation_request.additional_properties = d
        return validation_request

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
