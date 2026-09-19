from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="EventMembership")


@_attrs_define
class EventMembership:
    """
    Attributes:
        id (int):
        uuid (str):
        name (str):
        creation_date (datetime.date):
        status (str):
    """

    id: int
    uuid: str
    name: str
    creation_date: datetime.date
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        name = self.name

        creation_date = self.creation_date.isoformat()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "name": name,
                "creation_date": creation_date,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        uuid = d.pop("uuid")

        name = d.pop("name")

        creation_date = datetime.date.fromisoformat(d.pop("creation_date"))

        status = d.pop("status")

        event_membership = cls(
            id=id,
            uuid=uuid,
            name=name,
            creation_date=creation_date,
            status=status,
        )

        event_membership.additional_properties = d
        return event_membership

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
