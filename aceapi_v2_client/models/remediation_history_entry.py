from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="RemediationHistoryEntry")


@_attrs_define
class RemediationHistoryEntry:
    """One attempt of the remediation service at a remediation. Timestamps are UTC.

    Attributes:
        insert_date (datetime.datetime):
        result (str):
        status (str):
        message (str):
    """

    insert_date: datetime.datetime
    result: str
    status: str
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        insert_date = self.insert_date.isoformat()

        result = self.result

        status = self.status

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "insert_date": insert_date,
                "result": result,
                "status": status,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        insert_date = datetime.datetime.fromisoformat(d.pop("insert_date"))

        result = d.pop("result")

        status = d.pop("status")

        message = d.pop("message")

        remediation_history_entry = cls(
            insert_date=insert_date,
            result=result,
            status=status,
            message=message,
        )

        remediation_history_entry.additional_properties = d
        return remediation_history_entry

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
