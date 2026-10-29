from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SampleDeletion")


@_attrs_define
class SampleDeletion:
    """The audit of a sample file deleted from SVS.

    Attributes:
        sha256 (str):
        rule_uuids (list[str]): the rules the file had captures for
        capture_count (int): how many captures were removed
        reason (str):
        deleted_at (datetime.datetime):
        node (str): the node the file's bytes were on
        updated_at (datetime.datetime):
        deleted_by (None | str | Unset):
        purged_at (datetime.datetime | None | Unset): when the file's bytes were purged; null while they are not (a
            legal hold, a storage failure): deleting the sample again retries
    """

    sha256: str
    rule_uuids: list[str]
    capture_count: int
    reason: str
    deleted_at: datetime.datetime
    node: str
    updated_at: datetime.datetime
    deleted_by: None | str | Unset = UNSET
    purged_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sha256 = self.sha256

        rule_uuids = self.rule_uuids

        capture_count = self.capture_count

        reason = self.reason

        deleted_at = self.deleted_at.isoformat()

        node = self.node

        updated_at = self.updated_at.isoformat()

        deleted_by: None | str | Unset
        if isinstance(self.deleted_by, Unset):
            deleted_by = UNSET
        else:
            deleted_by = self.deleted_by

        purged_at: None | str | Unset
        if isinstance(self.purged_at, Unset):
            purged_at = UNSET
        elif isinstance(self.purged_at, datetime.datetime):
            purged_at = self.purged_at.isoformat()
        else:
            purged_at = self.purged_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha256": sha256,
                "rule_uuids": rule_uuids,
                "capture_count": capture_count,
                "reason": reason,
                "deleted_at": deleted_at,
                "node": node,
                "updated_at": updated_at,
            }
        )
        if deleted_by is not UNSET:
            field_dict["deleted_by"] = deleted_by
        if purged_at is not UNSET:
            field_dict["purged_at"] = purged_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sha256 = d.pop("sha256")

        rule_uuids = cast(list[str], d.pop("rule_uuids"))

        capture_count = d.pop("capture_count")

        reason = d.pop("reason")

        deleted_at = datetime.datetime.fromisoformat(d.pop("deleted_at"))

        node = d.pop("node")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_deleted_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_by = _parse_deleted_by(d.pop("deleted_by", UNSET))

        def _parse_purged_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purged_at_type_0 = datetime.datetime.fromisoformat(data)

                return purged_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        purged_at = _parse_purged_at(d.pop("purged_at", UNSET))

        sample_deletion = cls(
            sha256=sha256,
            rule_uuids=rule_uuids,
            capture_count=capture_count,
            reason=reason,
            deleted_at=deleted_at,
            node=node,
            updated_at=updated_at,
            deleted_by=deleted_by,
            purged_at=purged_at,
        )

        sample_deletion.additional_properties = d
        return sample_deletion

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
