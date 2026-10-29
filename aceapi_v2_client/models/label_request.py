from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.label_request_verdict import LabelRequestVerdict

T = TypeVar("T", bound="LabelRequest")


@_attrs_define
class LabelRequest:
    """
    Attributes:
        verdict (LabelRequestVerdict): the explicit verdict to store on every contributing detection that can take one
    """

    verdict: LabelRequestVerdict
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        verdict = self.verdict.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "verdict": verdict,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        verdict = LabelRequestVerdict(d.pop("verdict"))

        label_request = cls(
            verdict=verdict,
        )

        label_request.additional_properties = d
        return label_request

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
