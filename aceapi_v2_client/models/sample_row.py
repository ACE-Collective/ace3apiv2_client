from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.sample_row_label_source_type_0 import SampleRowLabelSourceType0
from ..models.sample_row_label_type_0 import SampleRowLabelType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sample_votes import SampleVotes


T = TypeVar("T", bound="SampleRow")


@_attrs_define
class SampleRow:
    """One sample: a file and a YARA rule it matched, over every alert it was captured from.

    Timestamps are UTC.

        Attributes:
            sha256 (str): the file's sha256
            rule_uuid (str): the rule's uuid meta; the signature_uuid of its detections
            rule_name (str): the rule's name in the latest capture
            file_path (str): the file's path in the latest capture, relative to its alert's files directory
            capture_count (int): how many captures (one per alert) the sample has
            stored (int): how many captures hold the file
            missing (int): how many captures could not keep the file (state missing)
            missing_data (int): how many captures lack something: the file, or the match record
            unknown_version (int): how many captures recorded signature version 'unknown'
            first_captured (datetime.datetime):
            last_captured (datetime.datetime):
            updated_at (datetime.datetime): the latest change of any of its captures
            latest_capture_id (int):
            votes (SampleVotes): How many contributing detections vote TP or FP, at each strength (verdict source).
            retired (bool): whether the sample is retired for its rule: YARA validation only counts it
            local (bool): whether this node can serve the file: always with a shared pool
            namespace (None | str | Unset): the rule's namespace in the latest capture, relative to the signature directory
            file_size (int | None | Unset):
            label (None | SampleRowLabelType0 | Unset): the sample's grade for the rule, aggregated from the verdicts of its
                contributing detections: tp, fp, or conflicted when votes of the strongest strength present disagree; null when
                no detection has a verdict
            label_source (None | SampleRowLabelSourceType0 | Unset): the strength that decided the label: explicit >
                inherited_single > inherited_multi
            retired_by (None | str | Unset): who retired it, while it is retired
            retired_at (datetime.datetime | None | Unset):
            retired_reason (None | str | Unset):
    """

    sha256: str
    rule_uuid: str
    rule_name: str
    file_path: str
    capture_count: int
    stored: int
    missing: int
    missing_data: int
    unknown_version: int
    first_captured: datetime.datetime
    last_captured: datetime.datetime
    updated_at: datetime.datetime
    latest_capture_id: int
    votes: SampleVotes
    retired: bool
    local: bool
    namespace: None | str | Unset = UNSET
    file_size: int | None | Unset = UNSET
    label: None | SampleRowLabelType0 | Unset = UNSET
    label_source: None | SampleRowLabelSourceType0 | Unset = UNSET
    retired_by: None | str | Unset = UNSET
    retired_at: datetime.datetime | None | Unset = UNSET
    retired_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sha256 = self.sha256

        rule_uuid = self.rule_uuid

        rule_name = self.rule_name

        file_path = self.file_path

        capture_count = self.capture_count

        stored = self.stored

        missing = self.missing

        missing_data = self.missing_data

        unknown_version = self.unknown_version

        first_captured = self.first_captured.isoformat()

        last_captured = self.last_captured.isoformat()

        updated_at = self.updated_at.isoformat()

        latest_capture_id = self.latest_capture_id

        votes = self.votes.to_dict()

        retired = self.retired

        local = self.local

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        file_size: int | None | Unset
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        elif isinstance(self.label, SampleRowLabelType0):
            label = self.label.value
        else:
            label = self.label

        label_source: None | str | Unset
        if isinstance(self.label_source, Unset):
            label_source = UNSET
        elif isinstance(self.label_source, SampleRowLabelSourceType0):
            label_source = self.label_source.value
        else:
            label_source = self.label_source

        retired_by: None | str | Unset
        if isinstance(self.retired_by, Unset):
            retired_by = UNSET
        else:
            retired_by = self.retired_by

        retired_at: None | str | Unset
        if isinstance(self.retired_at, Unset):
            retired_at = UNSET
        elif isinstance(self.retired_at, datetime.datetime):
            retired_at = self.retired_at.isoformat()
        else:
            retired_at = self.retired_at

        retired_reason: None | str | Unset
        if isinstance(self.retired_reason, Unset):
            retired_reason = UNSET
        else:
            retired_reason = self.retired_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha256": sha256,
                "rule_uuid": rule_uuid,
                "rule_name": rule_name,
                "file_path": file_path,
                "capture_count": capture_count,
                "stored": stored,
                "missing": missing,
                "missing_data": missing_data,
                "unknown_version": unknown_version,
                "first_captured": first_captured,
                "last_captured": last_captured,
                "updated_at": updated_at,
                "latest_capture_id": latest_capture_id,
                "votes": votes,
                "retired": retired,
                "local": local,
            }
        )
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if label is not UNSET:
            field_dict["label"] = label
        if label_source is not UNSET:
            field_dict["label_source"] = label_source
        if retired_by is not UNSET:
            field_dict["retired_by"] = retired_by
        if retired_at is not UNSET:
            field_dict["retired_at"] = retired_at
        if retired_reason is not UNSET:
            field_dict["retired_reason"] = retired_reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sample_votes import SampleVotes

        d = dict(src_dict)
        sha256 = d.pop("sha256")

        rule_uuid = d.pop("rule_uuid")

        rule_name = d.pop("rule_name")

        file_path = d.pop("file_path")

        capture_count = d.pop("capture_count")

        stored = d.pop("stored")

        missing = d.pop("missing")

        missing_data = d.pop("missing_data")

        unknown_version = d.pop("unknown_version")

        first_captured = datetime.datetime.fromisoformat(d.pop("first_captured"))

        last_captured = datetime.datetime.fromisoformat(d.pop("last_captured"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        latest_capture_id = d.pop("latest_capture_id")

        votes = SampleVotes.from_dict(d.pop("votes"))

        retired = d.pop("retired")

        local = d.pop("local")

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_file_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size = _parse_file_size(d.pop("file_size", UNSET))

        def _parse_label(data: object) -> None | SampleRowLabelType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                label_type_0 = SampleRowLabelType0(data)

                return label_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SampleRowLabelType0 | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_label_source(
            data: object,
        ) -> None | SampleRowLabelSourceType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                label_source_type_0 = SampleRowLabelSourceType0(data)

                return label_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SampleRowLabelSourceType0 | Unset, data)

        label_source = _parse_label_source(d.pop("label_source", UNSET))

        def _parse_retired_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retired_by = _parse_retired_by(d.pop("retired_by", UNSET))

        def _parse_retired_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retired_at_type_0 = datetime.datetime.fromisoformat(data)

                return retired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        retired_at = _parse_retired_at(d.pop("retired_at", UNSET))

        def _parse_retired_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retired_reason = _parse_retired_reason(d.pop("retired_reason", UNSET))

        sample_row = cls(
            sha256=sha256,
            rule_uuid=rule_uuid,
            rule_name=rule_name,
            file_path=file_path,
            capture_count=capture_count,
            stored=stored,
            missing=missing,
            missing_data=missing_data,
            unknown_version=unknown_version,
            first_captured=first_captured,
            last_captured=last_captured,
            updated_at=updated_at,
            latest_capture_id=latest_capture_id,
            votes=votes,
            retired=retired,
            local=local,
            namespace=namespace,
            file_size=file_size,
            label=label,
            label_source=label_source,
            retired_by=retired_by,
            retired_at=retired_at,
            retired_reason=retired_reason,
        )

        sample_row.additional_properties = d
        return sample_row

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
