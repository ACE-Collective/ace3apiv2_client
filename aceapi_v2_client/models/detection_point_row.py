from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.detection_point_row_override_type_0 import DetectionPointRowOverrideType0
from ..models.detection_point_row_verdict_source_type_0 import (
    DetectionPointRowVerdictSourceType0,
)
from ..models.detection_point_row_verdict_type_0 import DetectionPointRowVerdictType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="DetectionPointRow")


@_attrs_define
class DetectionPointRow:
    """One detection of an alert, with its effective verdict (docs/SVS.md, Part 1).

    Timestamps are UTC.

        Attributes:
            alert_uuid (str):
            content_hash (str): the detection's stable identity within its alert: a hash of the node it sits on, its
                signature, description and details. Verdicts are keyed on it
            description (str):
            signature_uuid (str):
            signature_version (str):
            insert_date (datetime.datetime):
            details (Any | None | Unset): the detection's structured details, if any
            queue (None | str | Unset): the queue the detection asked its alert to be routed to
            signature_family (None | str | Unset): yara, hunt, observable_modifier or builtin; null if unknown
            node_kind (None | str | Unset): root, observable or analysis; null on a row synced before node identity
            node_type (None | str | Unset): the observable's type (for an analysis node, the analyzed observable's)
            node_value_sha256 (None | str | Unset): the observable's observables.sha256 key in hex; a file's content sha256
            node_module_path (None | str | Unset): the analysis module, for an analysis node
            verdict (DetectionPointRowVerdictType0 | None | Unset): the effective verdict; null when the alert's disposition
                is unclassified
            verdict_source (DetectionPointRowVerdictSourceType0 | None | Unset): explicit: set or confirmed by an analyst.
                inherited_single: inherited from the alert, which covered this detection directly (an FP alert, or a TP alert
                with one signature). inherited_multi: inherited TP on an alert where several signatures fired, unconfirmed
            override (DetectionPointRowOverrideType0 | None | Unset): the stored explicit verdict, if any; masked on an FP
                alert
            override_user (None | str | Unset):
            override_set_at (datetime.datetime | None | Unset):
    """

    alert_uuid: str
    content_hash: str
    description: str
    signature_uuid: str
    signature_version: str
    insert_date: datetime.datetime
    details: Any | None | Unset = UNSET
    queue: None | str | Unset = UNSET
    signature_family: None | str | Unset = UNSET
    node_kind: None | str | Unset = UNSET
    node_type: None | str | Unset = UNSET
    node_value_sha256: None | str | Unset = UNSET
    node_module_path: None | str | Unset = UNSET
    verdict: DetectionPointRowVerdictType0 | None | Unset = UNSET
    verdict_source: DetectionPointRowVerdictSourceType0 | None | Unset = UNSET
    override: DetectionPointRowOverrideType0 | None | Unset = UNSET
    override_user: None | str | Unset = UNSET
    override_set_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_uuid = self.alert_uuid

        content_hash = self.content_hash

        description = self.description

        signature_uuid = self.signature_uuid

        signature_version = self.signature_version

        insert_date = self.insert_date.isoformat()

        details: Any | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        queue: None | str | Unset
        if isinstance(self.queue, Unset):
            queue = UNSET
        else:
            queue = self.queue

        signature_family: None | str | Unset
        if isinstance(self.signature_family, Unset):
            signature_family = UNSET
        else:
            signature_family = self.signature_family

        node_kind: None | str | Unset
        if isinstance(self.node_kind, Unset):
            node_kind = UNSET
        else:
            node_kind = self.node_kind

        node_type: None | str | Unset
        if isinstance(self.node_type, Unset):
            node_type = UNSET
        else:
            node_type = self.node_type

        node_value_sha256: None | str | Unset
        if isinstance(self.node_value_sha256, Unset):
            node_value_sha256 = UNSET
        else:
            node_value_sha256 = self.node_value_sha256

        node_module_path: None | str | Unset
        if isinstance(self.node_module_path, Unset):
            node_module_path = UNSET
        else:
            node_module_path = self.node_module_path

        verdict: None | str | Unset
        if isinstance(self.verdict, Unset):
            verdict = UNSET
        elif isinstance(self.verdict, DetectionPointRowVerdictType0):
            verdict = self.verdict.value
        else:
            verdict = self.verdict

        verdict_source: None | str | Unset
        if isinstance(self.verdict_source, Unset):
            verdict_source = UNSET
        elif isinstance(self.verdict_source, DetectionPointRowVerdictSourceType0):
            verdict_source = self.verdict_source.value
        else:
            verdict_source = self.verdict_source

        override: None | str | Unset
        if isinstance(self.override, Unset):
            override = UNSET
        elif isinstance(self.override, DetectionPointRowOverrideType0):
            override = self.override.value
        else:
            override = self.override

        override_user: None | str | Unset
        if isinstance(self.override_user, Unset):
            override_user = UNSET
        else:
            override_user = self.override_user

        override_set_at: None | str | Unset
        if isinstance(self.override_set_at, Unset):
            override_set_at = UNSET
        elif isinstance(self.override_set_at, datetime.datetime):
            override_set_at = self.override_set_at.isoformat()
        else:
            override_set_at = self.override_set_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_uuid": alert_uuid,
                "content_hash": content_hash,
                "description": description,
                "signature_uuid": signature_uuid,
                "signature_version": signature_version,
                "insert_date": insert_date,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if queue is not UNSET:
            field_dict["queue"] = queue
        if signature_family is not UNSET:
            field_dict["signature_family"] = signature_family
        if node_kind is not UNSET:
            field_dict["node_kind"] = node_kind
        if node_type is not UNSET:
            field_dict["node_type"] = node_type
        if node_value_sha256 is not UNSET:
            field_dict["node_value_sha256"] = node_value_sha256
        if node_module_path is not UNSET:
            field_dict["node_module_path"] = node_module_path
        if verdict is not UNSET:
            field_dict["verdict"] = verdict
        if verdict_source is not UNSET:
            field_dict["verdict_source"] = verdict_source
        if override is not UNSET:
            field_dict["override"] = override
        if override_user is not UNSET:
            field_dict["override_user"] = override_user
        if override_set_at is not UNSET:
            field_dict["override_set_at"] = override_set_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alert_uuid = d.pop("alert_uuid")

        content_hash = d.pop("content_hash")

        description = d.pop("description")

        signature_uuid = d.pop("signature_uuid")

        signature_version = d.pop("signature_version")

        insert_date = datetime.datetime.fromisoformat(d.pop("insert_date"))

        def _parse_details(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_queue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queue = _parse_queue(d.pop("queue", UNSET))

        def _parse_signature_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature_family = _parse_signature_family(d.pop("signature_family", UNSET))

        def _parse_node_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_kind = _parse_node_kind(d.pop("node_kind", UNSET))

        def _parse_node_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_type = _parse_node_type(d.pop("node_type", UNSET))

        def _parse_node_value_sha256(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_value_sha256 = _parse_node_value_sha256(d.pop("node_value_sha256", UNSET))

        def _parse_node_module_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_module_path = _parse_node_module_path(d.pop("node_module_path", UNSET))

        def _parse_verdict(
            data: object,
        ) -> DetectionPointRowVerdictType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verdict_type_0 = DetectionPointRowVerdictType0(data)

                return verdict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DetectionPointRowVerdictType0 | None | Unset, data)

        verdict = _parse_verdict(d.pop("verdict", UNSET))

        def _parse_verdict_source(
            data: object,
        ) -> DetectionPointRowVerdictSourceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verdict_source_type_0 = DetectionPointRowVerdictSourceType0(data)

                return verdict_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DetectionPointRowVerdictSourceType0 | None | Unset, data)

        verdict_source = _parse_verdict_source(d.pop("verdict_source", UNSET))

        def _parse_override(
            data: object,
        ) -> DetectionPointRowOverrideType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                override_type_0 = DetectionPointRowOverrideType0(data)

                return override_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DetectionPointRowOverrideType0 | None | Unset, data)

        override = _parse_override(d.pop("override", UNSET))

        def _parse_override_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        override_user = _parse_override_user(d.pop("override_user", UNSET))

        def _parse_override_set_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                override_set_at_type_0 = datetime.datetime.fromisoformat(data)

                return override_set_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        override_set_at = _parse_override_set_at(d.pop("override_set_at", UNSET))

        detection_point_row = cls(
            alert_uuid=alert_uuid,
            content_hash=content_hash,
            description=description,
            signature_uuid=signature_uuid,
            signature_version=signature_version,
            insert_date=insert_date,
            details=details,
            queue=queue,
            signature_family=signature_family,
            node_kind=node_kind,
            node_type=node_type,
            node_value_sha256=node_value_sha256,
            node_module_path=node_module_path,
            verdict=verdict,
            verdict_source=verdict_source,
            override=override,
            override_user=override_user,
            override_set_at=override_set_at,
        )

        detection_point_row.additional_properties = d
        return detection_point_row

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
