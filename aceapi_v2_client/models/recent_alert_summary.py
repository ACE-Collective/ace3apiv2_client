from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="RecentAlertSummary")


@_attrs_define
class RecentAlertSummary:
    """
    Attributes:
        uuid (str):
        disposition (str):
        insert_date (datetime.datetime):
    """

    uuid: str
    disposition: str
    insert_date: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        disposition = self.disposition

        insert_date = self.insert_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "disposition": disposition,
                "insert_date": insert_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        uuid = d.pop("uuid")

        disposition = d.pop("disposition")

        insert_date = datetime.datetime.fromisoformat(d.pop("insert_date"))

        recent_alert_summary = cls(
            uuid=uuid,
            disposition=disposition,
            insert_date=insert_date,
        )

        recent_alert_summary.additional_properties = d
        return recent_alert_summary

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
