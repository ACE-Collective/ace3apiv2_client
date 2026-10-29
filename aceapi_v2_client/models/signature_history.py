from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="SignatureHistory")


@_attrs_define
class SignatureHistory:
    """
    Attributes:
        signature_uuid (str):
        statuses (list[None | str]): its status in each of the runs, in their order: as reviewed for a reviewed run,
            else live; null when it isn't in that run's result
    """

    signature_uuid: str
    statuses: list[None | str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signature_uuid = self.signature_uuid

        statuses = []
        for statuses_item_data in self.statuses:
            statuses_item: None | str
            statuses_item = statuses_item_data
            statuses.append(statuses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signature_uuid": signature_uuid,
                "statuses": statuses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        signature_uuid = d.pop("signature_uuid")

        statuses = []
        _statuses = d.pop("statuses")
        for statuses_item_data in _statuses:

            def _parse_statuses_item(data: object) -> None | str:
                if data is None:
                    return data
                return cast(None | str, data)

            statuses_item = _parse_statuses_item(statuses_item_data)

            statuses.append(statuses_item)

        signature_history = cls(
            signature_uuid=signature_uuid,
            statuses=statuses,
        )

        signature_history.additional_properties = d
        return signature_history

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
