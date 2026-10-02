from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qa_match_detail_match_summary import QAMatchDetailMatchSummary


T = TypeVar("T", bound="QAMatchDetail")


@_attrs_define
class QAMatchDetail:
    """
    Attributes:
        id (int):
        signature_uuid (str):
        signature_version (str):
        sha256 (str):
        file_name (str):
        file_size (int):
        hit_count (int): how many times this file matched this version of the rule
        first_seen (datetime.datetime):
        last_seen (datetime.datetime):
        expires_at (datetime.datetime): when the file is removed unless it matches again
        node (str): the node that stored the file
        local (bool): true when the file can be downloaded through this node: the pool is shared, or the file is on this
            node
        root_uuid (str): the analysis the file was found in
        observable_uuid (str):
        alert_uuid (None | str | Unset): set when that analysis became an alert
        match_summary (QAMatchDetailMatchSummary | Unset): the rule, its meta and tags, and per string identifier how
            many times it matched and where first. The full record is at /matches/{id}/record
    """

    id: int
    signature_uuid: str
    signature_version: str
    sha256: str
    file_name: str
    file_size: int
    hit_count: int
    first_seen: datetime.datetime
    last_seen: datetime.datetime
    expires_at: datetime.datetime
    node: str
    local: bool
    root_uuid: str
    observable_uuid: str
    alert_uuid: None | str | Unset = UNSET
    match_summary: QAMatchDetailMatchSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        signature_uuid = self.signature_uuid

        signature_version = self.signature_version

        sha256 = self.sha256

        file_name = self.file_name

        file_size = self.file_size

        hit_count = self.hit_count

        first_seen = self.first_seen.isoformat()

        last_seen = self.last_seen.isoformat()

        expires_at = self.expires_at.isoformat()

        node = self.node

        local = self.local

        root_uuid = self.root_uuid

        observable_uuid = self.observable_uuid

        alert_uuid: None | str | Unset
        if isinstance(self.alert_uuid, Unset):
            alert_uuid = UNSET
        else:
            alert_uuid = self.alert_uuid

        match_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_summary, Unset):
            match_summary = self.match_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "signature_uuid": signature_uuid,
                "signature_version": signature_version,
                "sha256": sha256,
                "file_name": file_name,
                "file_size": file_size,
                "hit_count": hit_count,
                "first_seen": first_seen,
                "last_seen": last_seen,
                "expires_at": expires_at,
                "node": node,
                "local": local,
                "root_uuid": root_uuid,
                "observable_uuid": observable_uuid,
            }
        )
        if alert_uuid is not UNSET:
            field_dict["alert_uuid"] = alert_uuid
        if match_summary is not UNSET:
            field_dict["match_summary"] = match_summary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.qa_match_detail_match_summary import (
            QAMatchDetailMatchSummary,
        )

        d = dict(src_dict)
        id = d.pop("id")

        signature_uuid = d.pop("signature_uuid")

        signature_version = d.pop("signature_version")

        sha256 = d.pop("sha256")

        file_name = d.pop("file_name")

        file_size = d.pop("file_size")

        hit_count = d.pop("hit_count")

        first_seen = datetime.datetime.fromisoformat(d.pop("first_seen"))

        last_seen = datetime.datetime.fromisoformat(d.pop("last_seen"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        node = d.pop("node")

        local = d.pop("local")

        root_uuid = d.pop("root_uuid")

        observable_uuid = d.pop("observable_uuid")

        def _parse_alert_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alert_uuid = _parse_alert_uuid(d.pop("alert_uuid", UNSET))

        _match_summary = d.pop("match_summary", UNSET)
        match_summary: QAMatchDetailMatchSummary | Unset
        if isinstance(_match_summary, Unset):
            match_summary = UNSET
        else:
            match_summary = QAMatchDetailMatchSummary.from_dict(_match_summary)

        qa_match_detail = cls(
            id=id,
            signature_uuid=signature_uuid,
            signature_version=signature_version,
            sha256=sha256,
            file_name=file_name,
            file_size=file_size,
            hit_count=hit_count,
            first_seen=first_seen,
            last_seen=last_seen,
            expires_at=expires_at,
            node=node,
            local=local,
            root_uuid=root_uuid,
            observable_uuid=observable_uuid,
            alert_uuid=alert_uuid,
            match_summary=match_summary,
        )

        qa_match_detail.additional_properties = d
        return qa_match_detail

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
