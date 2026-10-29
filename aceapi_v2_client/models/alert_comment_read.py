from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="AlertCommentRead")


@_attrs_define
class AlertCommentRead:
    """
    Attributes:
        comment_id (int):
        alert_uuid (str):
        insert_date (datetime.datetime):
        user_id (int):
        user_display_name (str):
        comment (str):
    """

    comment_id: int
    alert_uuid: str
    insert_date: datetime.datetime
    user_id: int
    user_display_name: str
    comment: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        alert_uuid = self.alert_uuid

        insert_date = self.insert_date.isoformat()

        user_id = self.user_id

        user_display_name = self.user_display_name

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment_id": comment_id,
                "alert_uuid": alert_uuid,
                "insert_date": insert_date,
                "user_id": user_id,
                "user_display_name": user_display_name,
                "comment": comment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        comment_id = d.pop("comment_id")

        alert_uuid = d.pop("alert_uuid")

        insert_date = datetime.datetime.fromisoformat(d.pop("insert_date"))

        user_id = d.pop("user_id")

        user_display_name = d.pop("user_display_name")

        comment = d.pop("comment")

        alert_comment_read = cls(
            comment_id=comment_id,
            alert_uuid=alert_uuid,
            insert_date=insert_date,
            user_id=user_id,
            user_display_name=user_display_name,
            comment=comment,
        )

        alert_comment_read.additional_properties = d
        return alert_comment_read

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
