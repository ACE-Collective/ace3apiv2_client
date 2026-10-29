from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorklistRow")


@_attrs_define
class WorklistRow:
    """One signature's tag on, or measurement of, one ATT&CK technique, as of the last coverage
    refresh (the resolution as of now).

        Attributes:
            signature_uuid (str):
            technique (str): the technique in the pinned ATT&CK release (a revoked tag id counts as its successor)
            kind (str): declared (a tag of the signature), undeclared (measured, but no tag names it) or unknown (a tag
                naming an id the release doesn't have)
            status (str): confirmed, open, kept, remove_pending, removed, undeclared, unknown or retired
            declared_as (list[str]): the tag ids, as the signature writes them, that count as the technique
            tag_present (bool): the signature has the tag now
            signature_counts (bool): the signature is enabled, and isn't a YARA rule in QA mode
            counts (bool): the tag counts toward coverage as a manual mapping (from the next refresh, after a resolution)
            measured (bool): the signature is expected of a catalog test
            measured_techniques (list[str]): the techniques the signature is measured on
            first_seen_at (datetime.datetime):
            status_changed_at (datetime.datetime):
            updated_at (datetime.datetime): when the row last changed; the changed_since key
            technique_name (None | str | Unset): its name in the pinned release
            signature_family (None | str | Unset):
            signature_name (None | str | Unset):
            resolution (None | str | Unset): keep or remove; null when nobody resolved the row
            reason (None | str | Unset):
            reference (None | str | Unset): a link, such as the pull request removing the tag
            resolved_by (None | str | Unset): the username of whoever resolved it
            resolved_at (datetime.datetime | None | Unset):
    """

    signature_uuid: str
    technique: str
    kind: str
    status: str
    declared_as: list[str]
    tag_present: bool
    signature_counts: bool
    counts: bool
    measured: bool
    measured_techniques: list[str]
    first_seen_at: datetime.datetime
    status_changed_at: datetime.datetime
    updated_at: datetime.datetime
    technique_name: None | str | Unset = UNSET
    signature_family: None | str | Unset = UNSET
    signature_name: None | str | Unset = UNSET
    resolution: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    reference: None | str | Unset = UNSET
    resolved_by: None | str | Unset = UNSET
    resolved_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signature_uuid = self.signature_uuid

        technique = self.technique

        kind = self.kind

        status = self.status

        declared_as = self.declared_as

        tag_present = self.tag_present

        signature_counts = self.signature_counts

        counts = self.counts

        measured = self.measured

        measured_techniques = self.measured_techniques

        first_seen_at = self.first_seen_at.isoformat()

        status_changed_at = self.status_changed_at.isoformat()

        updated_at = self.updated_at.isoformat()

        technique_name: None | str | Unset
        if isinstance(self.technique_name, Unset):
            technique_name = UNSET
        else:
            technique_name = self.technique_name

        signature_family: None | str | Unset
        if isinstance(self.signature_family, Unset):
            signature_family = UNSET
        else:
            signature_family = self.signature_family

        signature_name: None | str | Unset
        if isinstance(self.signature_name, Unset):
            signature_name = UNSET
        else:
            signature_name = self.signature_name

        resolution: None | str | Unset
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        else:
            resolution = self.resolution

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        resolved_by: None | str | Unset
        if isinstance(self.resolved_by, Unset):
            resolved_by = UNSET
        else:
            resolved_by = self.resolved_by

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        elif isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signature_uuid": signature_uuid,
                "technique": technique,
                "kind": kind,
                "status": status,
                "declared_as": declared_as,
                "tag_present": tag_present,
                "signature_counts": signature_counts,
                "counts": counts,
                "measured": measured,
                "measured_techniques": measured_techniques,
                "first_seen_at": first_seen_at,
                "status_changed_at": status_changed_at,
                "updated_at": updated_at,
            }
        )
        if technique_name is not UNSET:
            field_dict["technique_name"] = technique_name
        if signature_family is not UNSET:
            field_dict["signature_family"] = signature_family
        if signature_name is not UNSET:
            field_dict["signature_name"] = signature_name
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reference is not UNSET:
            field_dict["reference"] = reference
        if resolved_by is not UNSET:
            field_dict["resolved_by"] = resolved_by
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        signature_uuid = d.pop("signature_uuid")

        technique = d.pop("technique")

        kind = d.pop("kind")

        status = d.pop("status")

        declared_as = cast(list[str], d.pop("declared_as"))

        tag_present = d.pop("tag_present")

        signature_counts = d.pop("signature_counts")

        counts = d.pop("counts")

        measured = d.pop("measured")

        measured_techniques = cast(list[str], d.pop("measured_techniques"))

        first_seen_at = datetime.datetime.fromisoformat(d.pop("first_seen_at"))

        status_changed_at = datetime.datetime.fromisoformat(d.pop("status_changed_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_technique_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        technique_name = _parse_technique_name(d.pop("technique_name", UNSET))

        def _parse_signature_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature_family = _parse_signature_family(d.pop("signature_family", UNSET))

        def _parse_signature_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature_name = _parse_signature_name(d.pop("signature_name", UNSET))

        def _parse_resolution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        def _parse_resolved_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_by = _parse_resolved_by(d.pop("resolved_by", UNSET))

        def _parse_resolved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))

        worklist_row = cls(
            signature_uuid=signature_uuid,
            technique=technique,
            kind=kind,
            status=status,
            declared_as=declared_as,
            tag_present=tag_present,
            signature_counts=signature_counts,
            counts=counts,
            measured=measured,
            measured_techniques=measured_techniques,
            first_seen_at=first_seen_at,
            status_changed_at=status_changed_at,
            updated_at=updated_at,
            technique_name=technique_name,
            signature_family=signature_family,
            signature_name=signature_name,
            resolution=resolution,
            reason=reason,
            reference=reference,
            resolved_by=resolved_by,
            resolved_at=resolved_at,
        )

        worklist_row.additional_properties = d
        return worklist_row

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
