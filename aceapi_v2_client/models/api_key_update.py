from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_scope import ApiKeyScope


T = TypeVar("T", bound="ApiKeyUpdate")


@_attrs_define
class ApiKeyUpdate:
    """Request to change an existing key's name and scope. The scope is replaced wholesale, under
    the same exactly-one-of rule as creation. The secret itself never changes: editing a key
    is how a deployed credential gets new permissions without being reissued.

        Attributes:
            name (str):
            inherit (bool | Unset):  Default: False.
            scope (list[ApiKeyScope] | Unset):
    """

    name: str
    inherit: bool | Unset = False
    scope: list[ApiKeyScope] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        inherit = self.inherit

        scope: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = []
            for scope_item_data in self.scope:
                scope_item = scope_item_data.to_dict()
                scope.append(scope_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if inherit is not UNSET:
            field_dict["inherit"] = inherit
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.api_key_scope import ApiKeyScope

        d = dict(src_dict)
        name = d.pop("name")

        inherit = d.pop("inherit", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: list[ApiKeyScope] | Unset = UNSET
        if _scope is not UNSET:
            scope = []
            for scope_item_data in _scope:
                scope_item = ApiKeyScope.from_dict(scope_item_data)

                scope.append(scope_item)

        api_key_update = cls(
            name=name,
            inherit=inherit,
            scope=scope,
        )

        api_key_update.additional_properties = d
        return api_key_update

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
