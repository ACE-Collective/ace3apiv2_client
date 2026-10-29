from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="RemediationTargetKey")


@_attrs_define
class RemediationTargetKey:
    """What a remediator acts on: the remediator, and the observable it remediates.

    Attributes:
        remediator (str): the remediator's configured name
        observable_type (str):
        observable_value (str):
    """

    remediator: str
    observable_type: str
    observable_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        remediator = self.remediator

        observable_type = self.observable_type

        observable_value = self.observable_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "remediator": remediator,
                "observable_type": observable_type,
                "observable_value": observable_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        remediator = d.pop("remediator")

        observable_type = d.pop("observable_type")

        observable_value = d.pop("observable_value")

        remediation_target_key = cls(
            remediator=remediator,
            observable_type=observable_type,
            observable_value=observable_value,
        )

        remediation_target_key.additional_properties = d
        return remediation_target_key

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
