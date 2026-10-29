from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.set_owner_request_take_owned import SetOwnerRequestTakeOwned


T = TypeVar("T", bound="SetOwnerRequest")


@_attrs_define
class SetOwnerRequest:
    """
    Attributes:
        alert_uuids (list[str]):
        owner_id (int | None): the user who gets the alerts: the caller's own id takes them, null unassigns them
        take_owned (SetOwnerRequestTakeOwned | Unset): alert uuid -> id of the analyst the caller agreed to take it
            from. An alert another analyst owns is changed only when it is named here with that analyst; otherwise it is
            left alone and reported in `skipped`.
    """

    alert_uuids: list[str]
    owner_id: int | None
    take_owned: SetOwnerRequestTakeOwned | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_uuids = self.alert_uuids

        owner_id: int | None
        owner_id = self.owner_id

        take_owned: dict[str, Any] | Unset = UNSET
        if not isinstance(self.take_owned, Unset):
            take_owned = self.take_owned.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_uuids": alert_uuids,
                "owner_id": owner_id,
            }
        )
        if take_owned is not UNSET:
            field_dict["take_owned"] = take_owned

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.set_owner_request_take_owned import SetOwnerRequestTakeOwned

        d = dict(src_dict)
        alert_uuids = cast(list[str], d.pop("alert_uuids"))

        def _parse_owner_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        owner_id = _parse_owner_id(d.pop("owner_id"))

        _take_owned = d.pop("take_owned", UNSET)
        take_owned: SetOwnerRequestTakeOwned | Unset
        if isinstance(_take_owned, Unset):
            take_owned = UNSET
        else:
            take_owned = SetOwnerRequestTakeOwned.from_dict(_take_owned)

        set_owner_request = cls(
            alert_uuids=alert_uuids,
            owner_id=owner_id,
            take_owned=take_owned,
        )

        set_owner_request.additional_properties = d
        return set_owner_request

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
