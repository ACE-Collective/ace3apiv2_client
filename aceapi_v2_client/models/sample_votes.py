from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="SampleVotes")


@_attrs_define
class SampleVotes:
    """How many contributing detections vote TP or FP, at each strength (verdict source).

    Attributes:
        tp_explicit (int):
        fp_explicit (int):
        tp_inherited_single (int):
        fp_inherited_single (int):
        tp_inherited_multi (int):
        fp_inherited_multi (int):
    """

    tp_explicit: int
    fp_explicit: int
    tp_inherited_single: int
    fp_inherited_single: int
    tp_inherited_multi: int
    fp_inherited_multi: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tp_explicit = self.tp_explicit

        fp_explicit = self.fp_explicit

        tp_inherited_single = self.tp_inherited_single

        fp_inherited_single = self.fp_inherited_single

        tp_inherited_multi = self.tp_inherited_multi

        fp_inherited_multi = self.fp_inherited_multi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tp_explicit": tp_explicit,
                "fp_explicit": fp_explicit,
                "tp_inherited_single": tp_inherited_single,
                "fp_inherited_single": fp_inherited_single,
                "tp_inherited_multi": tp_inherited_multi,
                "fp_inherited_multi": fp_inherited_multi,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tp_explicit = d.pop("tp_explicit")

        fp_explicit = d.pop("fp_explicit")

        tp_inherited_single = d.pop("tp_inherited_single")

        fp_inherited_single = d.pop("fp_inherited_single")

        tp_inherited_multi = d.pop("tp_inherited_multi")

        fp_inherited_multi = d.pop("fp_inherited_multi")

        sample_votes = cls(
            tp_explicit=tp_explicit,
            fp_explicit=fp_explicit,
            tp_inherited_single=tp_inherited_single,
            fp_inherited_single=fp_inherited_single,
            tp_inherited_multi=tp_inherited_multi,
            fp_inherited_multi=fp_inherited_multi,
        )

        sample_votes.additional_properties = d
        return sample_votes

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
