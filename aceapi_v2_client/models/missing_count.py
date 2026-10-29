from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.missing_count_reason import MissingCountReason

T = TypeVar("T", bound="MissingCount")


@_attrs_define
class MissingCount:
    """
    Attributes:
        rule_uuid (str):
        rule_name (str):
        reason (MissingCountReason):
        count (int):
    """

    rule_uuid: str
    rule_name: str
    reason: MissingCountReason
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_uuid = self.rule_uuid

        rule_name = self.rule_name

        reason = self.reason.value

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_uuid": rule_uuid,
                "rule_name": rule_name,
                "reason": reason,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rule_uuid = d.pop("rule_uuid")

        rule_name = d.pop("rule_name")

        reason = MissingCountReason(d.pop("reason"))

        count = d.pop("count")

        missing_count = cls(
            rule_uuid=rule_uuid,
            rule_name=rule_name,
            reason=reason,
            count=count,
        )

        missing_count.additional_properties = d
        return missing_count

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
