from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.sample_capture_missing_reason_type_0 import (
    SampleCaptureMissingReasonType0,
)
from ..models.sample_capture_state import SampleCaptureState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sample_capture_match_summary import SampleCaptureMatchSummary
    from ..models.sample_detection import SampleDetection


T = TypeVar("T", bound="SampleCapture")


@_attrs_define
class SampleCapture:
    """One capture of the sample: the file as one alert had it.

    Attributes:
        id (int):
        alert_uuid (str):
        observable_uuid (str):
        rule_name (str):
        signature_version (str): the commit of the rule's repository when it matched, or 'unknown'
        file_path (str):
        yara_meta_tags (list[str]):
        state (SampleCaptureState):
        has_record (bool): whether the match record is stored (GET /svs/samples/captures/{id}/record)
        match_summary (SampleCaptureMatchSummary): the match record's summary: meta, tags, and per string how many times
            it matched and where first
        node (str):
        local (bool): whether this node can serve the match record
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        detections (list[SampleDetection]): its contributing detections; empty when the alert was deleted
        namespace (None | str | Unset):
        rule_content_hash (None | str | Unset):
        file_size (int | None | Unset):
        missing_reason (None | SampleCaptureMissingReasonType0 | Unset):
        yara_python_version (None | str | Unset):
        yara_scanner_version (None | str | Unset):
        stored_at (datetime.datetime | None | Unset):
    """

    id: int
    alert_uuid: str
    observable_uuid: str
    rule_name: str
    signature_version: str
    file_path: str
    yara_meta_tags: list[str]
    state: SampleCaptureState
    has_record: bool
    match_summary: SampleCaptureMatchSummary
    node: str
    local: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    detections: list[SampleDetection]
    namespace: None | str | Unset = UNSET
    rule_content_hash: None | str | Unset = UNSET
    file_size: int | None | Unset = UNSET
    missing_reason: None | SampleCaptureMissingReasonType0 | Unset = UNSET
    yara_python_version: None | str | Unset = UNSET
    yara_scanner_version: None | str | Unset = UNSET
    stored_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        alert_uuid = self.alert_uuid

        observable_uuid = self.observable_uuid

        rule_name = self.rule_name

        signature_version = self.signature_version

        file_path = self.file_path

        yara_meta_tags = self.yara_meta_tags

        state = self.state.value

        has_record = self.has_record

        match_summary = self.match_summary.to_dict()

        node = self.node

        local = self.local

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        detections = []
        for detections_item_data in self.detections:
            detections_item = detections_item_data.to_dict()
            detections.append(detections_item)

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        rule_content_hash: None | str | Unset
        if isinstance(self.rule_content_hash, Unset):
            rule_content_hash = UNSET
        else:
            rule_content_hash = self.rule_content_hash

        file_size: int | None | Unset
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        missing_reason: None | str | Unset
        if isinstance(self.missing_reason, Unset):
            missing_reason = UNSET
        elif isinstance(self.missing_reason, SampleCaptureMissingReasonType0):
            missing_reason = self.missing_reason.value
        else:
            missing_reason = self.missing_reason

        yara_python_version: None | str | Unset
        if isinstance(self.yara_python_version, Unset):
            yara_python_version = UNSET
        else:
            yara_python_version = self.yara_python_version

        yara_scanner_version: None | str | Unset
        if isinstance(self.yara_scanner_version, Unset):
            yara_scanner_version = UNSET
        else:
            yara_scanner_version = self.yara_scanner_version

        stored_at: None | str | Unset
        if isinstance(self.stored_at, Unset):
            stored_at = UNSET
        elif isinstance(self.stored_at, datetime.datetime):
            stored_at = self.stored_at.isoformat()
        else:
            stored_at = self.stored_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "alert_uuid": alert_uuid,
                "observable_uuid": observable_uuid,
                "rule_name": rule_name,
                "signature_version": signature_version,
                "file_path": file_path,
                "yara_meta_tags": yara_meta_tags,
                "state": state,
                "has_record": has_record,
                "match_summary": match_summary,
                "node": node,
                "local": local,
                "created_at": created_at,
                "updated_at": updated_at,
                "detections": detections,
            }
        )
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if rule_content_hash is not UNSET:
            field_dict["rule_content_hash"] = rule_content_hash
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if missing_reason is not UNSET:
            field_dict["missing_reason"] = missing_reason
        if yara_python_version is not UNSET:
            field_dict["yara_python_version"] = yara_python_version
        if yara_scanner_version is not UNSET:
            field_dict["yara_scanner_version"] = yara_scanner_version
        if stored_at is not UNSET:
            field_dict["stored_at"] = stored_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sample_capture_match_summary import SampleCaptureMatchSummary
        from ..models.sample_detection import SampleDetection

        d = dict(src_dict)
        id = d.pop("id")

        alert_uuid = d.pop("alert_uuid")

        observable_uuid = d.pop("observable_uuid")

        rule_name = d.pop("rule_name")

        signature_version = d.pop("signature_version")

        file_path = d.pop("file_path")

        yara_meta_tags = cast(list[str], d.pop("yara_meta_tags"))

        state = SampleCaptureState(d.pop("state"))

        has_record = d.pop("has_record")

        match_summary = SampleCaptureMatchSummary.from_dict(d.pop("match_summary"))

        node = d.pop("node")

        local = d.pop("local")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        detections = []
        _detections = d.pop("detections")
        for detections_item_data in _detections:
            detections_item = SampleDetection.from_dict(detections_item_data)

            detections.append(detections_item)

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_rule_content_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rule_content_hash = _parse_rule_content_hash(d.pop("rule_content_hash", UNSET))

        def _parse_file_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size = _parse_file_size(d.pop("file_size", UNSET))

        def _parse_missing_reason(
            data: object,
        ) -> None | SampleCaptureMissingReasonType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                missing_reason_type_0 = SampleCaptureMissingReasonType0(data)

                return missing_reason_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SampleCaptureMissingReasonType0 | Unset, data)

        missing_reason = _parse_missing_reason(d.pop("missing_reason", UNSET))

        def _parse_yara_python_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yara_python_version = _parse_yara_python_version(
            d.pop("yara_python_version", UNSET)
        )

        def _parse_yara_scanner_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yara_scanner_version = _parse_yara_scanner_version(
            d.pop("yara_scanner_version", UNSET)
        )

        def _parse_stored_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stored_at_type_0 = datetime.datetime.fromisoformat(data)

                return stored_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        stored_at = _parse_stored_at(d.pop("stored_at", UNSET))

        sample_capture = cls(
            id=id,
            alert_uuid=alert_uuid,
            observable_uuid=observable_uuid,
            rule_name=rule_name,
            signature_version=signature_version,
            file_path=file_path,
            yara_meta_tags=yara_meta_tags,
            state=state,
            has_record=has_record,
            match_summary=match_summary,
            node=node,
            local=local,
            created_at=created_at,
            updated_at=updated_at,
            detections=detections,
            namespace=namespace,
            rule_content_hash=rule_content_hash,
            file_size=file_size,
            missing_reason=missing_reason,
            yara_python_version=yara_python_version,
            yara_scanner_version=yara_scanner_version,
            stored_at=stored_at,
        )

        sample_capture.additional_properties = d
        return sample_capture

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
