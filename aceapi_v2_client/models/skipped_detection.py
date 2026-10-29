from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="SkippedDetection")


@_attrs_define
class SkippedDetection:
    """
    Attributes:
        alert_uuid (str):
        content_hash (str):
        reason (str): why this detection could not take the verdict
    """

    alert_uuid: str
    content_hash: str
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_uuid = self.alert_uuid

        content_hash = self.content_hash

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_uuid": alert_uuid,
                "content_hash": content_hash,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alert_uuid = d.pop("alert_uuid")

        content_hash = d.pop("content_hash")

        reason = d.pop("reason")

        skipped_detection = cls(
            alert_uuid=alert_uuid,
            content_hash=content_hash,
            reason=reason,
        )

        skipped_detection.additional_properties = d
        return skipped_detection

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
