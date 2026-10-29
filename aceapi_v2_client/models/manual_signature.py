from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManualSignature")


@_attrs_define
class ManualSignature:
    """A signature's mitre: tag naming the technique or a sub-technique: a manual mapping.

    Attributes:
        signature_uuid (str):
        family (str): hunt or yara
        declared (str): the technique id the tag names
        technique (str): the technique it counts toward (a revoked id becomes its successor)
        counts (bool):
        name (None | str | Unset):
        reason (None | str | Unset): why it doesn't count: not_counting (disabled, or a YARA rule in QA mode) or
            unknown_technique
    """

    signature_uuid: str
    family: str
    declared: str
    technique: str
    counts: bool
    name: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signature_uuid = self.signature_uuid

        family = self.family

        declared = self.declared

        technique = self.technique

        counts = self.counts

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signature_uuid": signature_uuid,
                "family": family,
                "declared": declared,
                "technique": technique,
                "counts": counts,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        signature_uuid = d.pop("signature_uuid")

        family = d.pop("family")

        declared = d.pop("declared")

        technique = d.pop("technique")

        counts = d.pop("counts")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        manual_signature = cls(
            signature_uuid=signature_uuid,
            family=family,
            declared=declared,
            technique=technique,
            counts=counts,
            name=name,
            reason=reason,
        )

        manual_signature.additional_properties = d
        return manual_signature

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
