from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.label_action_result_label_source_type_0 import (
    LabelActionResultLabelSourceType0,
)
from ..models.label_action_result_label_type_0 import LabelActionResultLabelType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.skipped_detection import SkippedDetection


T = TypeVar("T", bound="LabelActionResult")


@_attrs_define
class LabelActionResult:
    """What a relabel, reset or confirm wrote, and the sample's label afterwards.

    Attributes:
        changed (int): how many contributing detections changed
        unchanged (int): how many already were as asked
        skipped (list[SkippedDetection]): the contributing detections that cannot take an analyst's verdict (on a false
            positive, unclassified or test alert), each with why
        label (LabelActionResultLabelType0 | None | Unset):
        label_source (LabelActionResultLabelSourceType0 | None | Unset):
    """

    changed: int
    unchanged: int
    skipped: list[SkippedDetection]
    label: LabelActionResultLabelType0 | None | Unset = UNSET
    label_source: LabelActionResultLabelSourceType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        unchanged = self.unchanged

        skipped = []
        for skipped_item_data in self.skipped:
            skipped_item = skipped_item_data.to_dict()
            skipped.append(skipped_item)

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        elif isinstance(self.label, LabelActionResultLabelType0):
            label = self.label.value
        else:
            label = self.label

        label_source: None | str | Unset
        if isinstance(self.label_source, Unset):
            label_source = UNSET
        elif isinstance(self.label_source, LabelActionResultLabelSourceType0):
            label_source = self.label_source.value
        else:
            label_source = self.label_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changed": changed,
                "unchanged": unchanged,
                "skipped": skipped,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if label_source is not UNSET:
            field_dict["label_source"] = label_source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.skipped_detection import SkippedDetection

        d = dict(src_dict)
        changed = d.pop("changed")

        unchanged = d.pop("unchanged")

        skipped = []
        _skipped = d.pop("skipped")
        for skipped_item_data in _skipped:
            skipped_item = SkippedDetection.from_dict(skipped_item_data)

            skipped.append(skipped_item)

        def _parse_label(data: object) -> LabelActionResultLabelType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                label_type_0 = LabelActionResultLabelType0(data)

                return label_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LabelActionResultLabelType0 | None | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_label_source(
            data: object,
        ) -> LabelActionResultLabelSourceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                label_source_type_0 = LabelActionResultLabelSourceType0(data)

                return label_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LabelActionResultLabelSourceType0 | None | Unset, data)

        label_source = _parse_label_source(d.pop("label_source", UNSET))

        label_action_result = cls(
            changed=changed,
            unchanged=unchanged,
            skipped=skipped,
            label=label,
            label_source=label_source,
        )

        label_action_result.additional_properties = d
        return label_action_result

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
