from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QASignatureVersion")


@_attrs_define
class QASignatureVersion:
    """What was recorded for one version of a signature. The version is the commit of the rule's
    repository when it matched ('unknown' for rules outside a declared git repo).

        Attributes:
            signature_version (str):
            rule_name (str): the rule's name when it last matched under this version
            match_count (int): every match under this version, including those past the file cap
            stored_count (int): files stored under this version
            first_match_at (datetime.datetime):
            last_match_at (datetime.datetime):
            namespace (None | str | Unset):
    """

    signature_version: str
    rule_name: str
    match_count: int
    stored_count: int
    first_match_at: datetime.datetime
    last_match_at: datetime.datetime
    namespace: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signature_version = self.signature_version

        rule_name = self.rule_name

        match_count = self.match_count

        stored_count = self.stored_count

        first_match_at = self.first_match_at.isoformat()

        last_match_at = self.last_match_at.isoformat()

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signature_version": signature_version,
                "rule_name": rule_name,
                "match_count": match_count,
                "stored_count": stored_count,
                "first_match_at": first_match_at,
                "last_match_at": last_match_at,
            }
        )
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        signature_version = d.pop("signature_version")

        rule_name = d.pop("rule_name")

        match_count = d.pop("match_count")

        stored_count = d.pop("stored_count")

        first_match_at = datetime.datetime.fromisoformat(d.pop("first_match_at"))

        last_match_at = datetime.datetime.fromisoformat(d.pop("last_match_at"))

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        qa_signature_version = cls(
            signature_version=signature_version,
            rule_name=rule_name,
            match_count=match_count,
            stored_count=stored_count,
            first_match_at=first_match_at,
            last_match_at=last_match_at,
            namespace=namespace,
        )

        qa_signature_version.additional_properties = d
        return qa_signature_version

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
