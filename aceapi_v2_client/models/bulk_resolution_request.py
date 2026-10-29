from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.worklist_key import WorklistKey


T = TypeVar("T", bound="BulkResolutionRequest")


@_attrs_define
class BulkResolutionRequest:
    """
    Attributes:
        resolution (str): keep (the tag covers something no test reaches) or remove (the signature repository will drop
            the tag)
        reason (str): why; required
        rows (list[WorklistKey]):
        reference (None | str | Unset): an http(s) link, such as the pull request removing the tag
    """

    resolution: str
    reason: str
    rows: list[WorklistKey]
    reference: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resolution = self.resolution

        reason = self.reason

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resolution": resolution,
                "reason": reason,
                "rows": rows,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.worklist_key import WorklistKey

        d = dict(src_dict)
        resolution = d.pop("resolution")

        reason = d.pop("reason")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = WorklistKey.from_dict(rows_item_data)

            rows.append(rows_item)

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        bulk_resolution_request = cls(
            resolution=resolution,
            reason=reason,
            rows=rows,
            reference=reference,
        )

        bulk_resolution_request.additional_properties = d
        return bulk_resolution_request

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
