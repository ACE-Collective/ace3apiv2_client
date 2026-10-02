from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QASignatureSummary")


@_attrs_define
class QASignatureSummary:
    """A signature in QA mode now, or one with recorded QA matches.

    Attributes:
        signature_uuid (str):
        name (str):
        status (str): qa: in QA mode now. not_qa: the rule exists but is no longer in QA mode. missing: no loaded rule
            has this uuid any more
        match_count (int): every QA match of this rule, across versions, including those past the file cap
        stored_count (int): files stored for this rule, across versions
        version_count (int): how many versions of the rule have matched
        enabled (bool | None | Unset): the rule's enabled meta; null when the rule is missing
        current_version (None | str | Unset): the version of the rule as loaded now; null when the rule is missing
        source_path (None | str | Unset): the rule's file, relative to its repository
        tags (list[str] | Unset):
        namespace (None | str | Unset): the yara namespace of the most recent match
        first_match_at (datetime.datetime | None | Unset):
        last_match_at (datetime.datetime | None | Unset):
    """

    signature_uuid: str
    name: str
    status: str
    match_count: int
    stored_count: int
    version_count: int
    enabled: bool | None | Unset = UNSET
    current_version: None | str | Unset = UNSET
    source_path: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    namespace: None | str | Unset = UNSET
    first_match_at: datetime.datetime | None | Unset = UNSET
    last_match_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signature_uuid = self.signature_uuid

        name = self.name

        status = self.status

        match_count = self.match_count

        stored_count = self.stored_count

        version_count = self.version_count

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        current_version: None | str | Unset
        if isinstance(self.current_version, Unset):
            current_version = UNSET
        else:
            current_version = self.current_version

        source_path: None | str | Unset
        if isinstance(self.source_path, Unset):
            source_path = UNSET
        else:
            source_path = self.source_path

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        first_match_at: None | str | Unset
        if isinstance(self.first_match_at, Unset):
            first_match_at = UNSET
        elif isinstance(self.first_match_at, datetime.datetime):
            first_match_at = self.first_match_at.isoformat()
        else:
            first_match_at = self.first_match_at

        last_match_at: None | str | Unset
        if isinstance(self.last_match_at, Unset):
            last_match_at = UNSET
        elif isinstance(self.last_match_at, datetime.datetime):
            last_match_at = self.last_match_at.isoformat()
        else:
            last_match_at = self.last_match_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signature_uuid": signature_uuid,
                "name": name,
                "status": status,
                "match_count": match_count,
                "stored_count": stored_count,
                "version_count": version_count,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if current_version is not UNSET:
            field_dict["current_version"] = current_version
        if source_path is not UNSET:
            field_dict["source_path"] = source_path
        if tags is not UNSET:
            field_dict["tags"] = tags
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if first_match_at is not UNSET:
            field_dict["first_match_at"] = first_match_at
        if last_match_at is not UNSET:
            field_dict["last_match_at"] = last_match_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        signature_uuid = d.pop("signature_uuid")

        name = d.pop("name")

        status = d.pop("status")

        match_count = d.pop("match_count")

        stored_count = d.pop("stored_count")

        version_count = d.pop("version_count")

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_current_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_version = _parse_current_version(d.pop("current_version", UNSET))

        def _parse_source_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_path = _parse_source_path(d.pop("source_path", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_first_match_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_match_at_type_0 = datetime.datetime.fromisoformat(data)

                return first_match_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_match_at = _parse_first_match_at(d.pop("first_match_at", UNSET))

        def _parse_last_match_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_match_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_match_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_match_at = _parse_last_match_at(d.pop("last_match_at", UNSET))

        qa_signature_summary = cls(
            signature_uuid=signature_uuid,
            name=name,
            status=status,
            match_count=match_count,
            stored_count=stored_count,
            version_count=version_count,
            enabled=enabled,
            current_version=current_version,
            source_path=source_path,
            tags=tags,
            namespace=namespace,
            first_match_at=first_match_at,
            last_match_at=last_match_at,
        )

        qa_signature_summary.additional_properties = d
        return qa_signature_summary

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
