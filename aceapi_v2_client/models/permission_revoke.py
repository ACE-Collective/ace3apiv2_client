from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PermissionRevoke")


@_attrs_define
class PermissionRevoke:
    """The permission ROWS to delete, by auth_user_permission / auth_group_permission id.

    These are not user ids and not group ids. PermissionGrant uses `users` and `groups` for those.
    extra="forbid" rejects unknown field names.

        Attributes:
            user_permission_ids (list[int] | Unset):
            group_permission_ids (list[int] | Unset):
    """

    user_permission_ids: list[int] | Unset = UNSET
    group_permission_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_permission_ids: list[int] | Unset = UNSET
        if not isinstance(self.user_permission_ids, Unset):
            user_permission_ids = self.user_permission_ids

        group_permission_ids: list[int] | Unset = UNSET
        if not isinstance(self.group_permission_ids, Unset):
            group_permission_ids = self.group_permission_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_permission_ids is not UNSET:
            field_dict["user_permission_ids"] = user_permission_ids
        if group_permission_ids is not UNSET:
            field_dict["group_permission_ids"] = group_permission_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user_permission_ids = cast(list[int], d.pop("user_permission_ids", UNSET))

        group_permission_ids = cast(list[int], d.pop("group_permission_ids", UNSET))

        permission_revoke = cls(
            user_permission_ids=user_permission_ids,
            group_permission_ids=group_permission_ids,
        )

        return permission_revoke
