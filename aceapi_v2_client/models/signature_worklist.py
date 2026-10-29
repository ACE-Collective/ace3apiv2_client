from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measured_technique import MeasuredTechnique
    from ..models.worklist_row import WorklistRow


T = TypeVar("T", bound="SignatureWorklist")


@_attrs_define
class SignatureWorklist:
    """A signature's worklist rows, and what it is measured on now.

    Attributes:
        signature_uuid (str):
        rows (list[WorklistRow]): every row of the signature, retired ones included
        measured (list[MeasuredTechnique]): the techniques the signature is measured on now, with the tests that measure
            it, computed at the request
        signature_family (None | str | Unset):
        signature_name (None | str | Unset):
    """

    signature_uuid: str
    rows: list[WorklistRow]
    measured: list[MeasuredTechnique]
    signature_family: None | str | Unset = UNSET
    signature_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signature_uuid = self.signature_uuid

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        measured = []
        for measured_item_data in self.measured:
            measured_item = measured_item_data.to_dict()
            measured.append(measured_item)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signature_uuid": signature_uuid,
                "rows": rows,
                "measured": measured,
            }
        )
        if signature_family is not UNSET:
            field_dict["signature_family"] = signature_family
        if signature_name is not UNSET:
            field_dict["signature_name"] = signature_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.measured_technique import MeasuredTechnique
        from ..models.worklist_row import WorklistRow

        d = dict(src_dict)
        signature_uuid = d.pop("signature_uuid")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = WorklistRow.from_dict(rows_item_data)

            rows.append(rows_item)

        measured = []
        _measured = d.pop("measured")
        for measured_item_data in _measured:
            measured_item = MeasuredTechnique.from_dict(measured_item_data)

            measured.append(measured_item)

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

        signature_worklist = cls(
            signature_uuid=signature_uuid,
            rows=rows,
            measured=measured,
            signature_family=signature_family,
            signature_name=signature_name,
        )

        signature_worklist.additional_properties = d
        return signature_worklist

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
