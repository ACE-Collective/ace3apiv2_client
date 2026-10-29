from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.validation_result_row_base import ValidationResultRowBase
from ..models.validation_result_row_head import ValidationResultRowHead
from ..models.validation_result_row_label_source_type_0 import (
    ValidationResultRowLabelSourceType0,
)
from ..models.validation_result_row_label_type_0 import ValidationResultRowLabelType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationResultRow")


@_attrs_define
class ValidationResultRow:
    """One (sample, rule uuid) pair the report lists, with the sample's label when it ran.

    Attributes:
        id (int):
        sha256 (str):
        rule_uuid (str):
        rule_name (str):
        base (ValidationResultRowBase): the outcome under base_sha: match (the rule would make a detection), miss or
            error
        head (ValidationResultRowHead):
        raw_base (bool): whether the rule matched under base at all, before enabled and the qa/no_alert modifiers
        raw_head (bool):
        category (str):
        namespace (None | str | Unset):
        label (None | Unset | ValidationResultRowLabelType0):
        label_source (None | Unset | ValidationResultRowLabelSourceType0):
        note (None | str | Unset):
    """

    id: int
    sha256: str
    rule_uuid: str
    rule_name: str
    base: ValidationResultRowBase
    head: ValidationResultRowHead
    raw_base: bool
    raw_head: bool
    category: str
    namespace: None | str | Unset = UNSET
    label: None | Unset | ValidationResultRowLabelType0 = UNSET
    label_source: None | Unset | ValidationResultRowLabelSourceType0 = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sha256 = self.sha256

        rule_uuid = self.rule_uuid

        rule_name = self.rule_name

        base = self.base.value

        head = self.head.value

        raw_base = self.raw_base

        raw_head = self.raw_head

        category = self.category

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        elif isinstance(self.label, ValidationResultRowLabelType0):
            label = self.label.value
        else:
            label = self.label

        label_source: None | str | Unset
        if isinstance(self.label_source, Unset):
            label_source = UNSET
        elif isinstance(self.label_source, ValidationResultRowLabelSourceType0):
            label_source = self.label_source.value
        else:
            label_source = self.label_source

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sha256": sha256,
                "rule_uuid": rule_uuid,
                "rule_name": rule_name,
                "base": base,
                "head": head,
                "raw_base": raw_base,
                "raw_head": raw_head,
                "category": category,
            }
        )
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if label is not UNSET:
            field_dict["label"] = label
        if label_source is not UNSET:
            field_dict["label_source"] = label_source
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        sha256 = d.pop("sha256")

        rule_uuid = d.pop("rule_uuid")

        rule_name = d.pop("rule_name")

        base = ValidationResultRowBase(d.pop("base"))

        head = ValidationResultRowHead(d.pop("head"))

        raw_base = d.pop("raw_base")

        raw_head = d.pop("raw_head")

        category = d.pop("category")

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_label(data: object) -> None | Unset | ValidationResultRowLabelType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                label_type_0 = ValidationResultRowLabelType0(data)

                return label_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ValidationResultRowLabelType0, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_label_source(
            data: object,
        ) -> None | Unset | ValidationResultRowLabelSourceType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                label_source_type_0 = ValidationResultRowLabelSourceType0(data)

                return label_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ValidationResultRowLabelSourceType0, data)

        label_source = _parse_label_source(d.pop("label_source", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        validation_result_row = cls(
            id=id,
            sha256=sha256,
            rule_uuid=rule_uuid,
            rule_name=rule_name,
            base=base,
            head=head,
            raw_base=raw_base,
            raw_head=raw_head,
            category=category,
            namespace=namespace,
            label=label,
            label_source=label_source,
            note=note,
        )

        validation_result_row.additional_properties = d
        return validation_result_row

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
