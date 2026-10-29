from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RunComment")


@_attrs_define
class RunComment:
    """
    Attributes:
        id (int):
        run_id (str):
        comment (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        user (None | str | Unset): its author's username
    """

    id: int
    run_id: str
    comment: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    user: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        run_id = self.run_id

        comment = self.comment

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        user: None | str | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "run_id": run_id,
                "comment": comment,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        run_id = d.pop("run_id")

        comment = d.pop("comment")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        run_comment = cls(
            id=id,
            run_id=run_id,
            comment=comment,
            created_at=created_at,
            updated_at=updated_at,
            user=user,
        )

        run_comment.additional_properties = d
        return run_comment

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
