from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.api_key_scope import ApiKeyScope


T = TypeVar("T", bound="ApiKeySelfWrite")


@_attrs_define
class ApiKeySelfWrite:
    """A user's request to create or change one of their OWN keys. Self-service keys are always
    scoped -- only an admin mints a key that inherits its owner's full permissions -- so there is
    no inherit field, and this is deliberately not ApiKeyCreate with one removed.

        Attributes:
            name (str):
            scope (list[ApiKeyScope]):
    """

    name: str
    scope: list[ApiKeyScope]

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scope = []
        for scope_item_data in self.scope:
            scope_item = scope_item_data.to_dict()
            scope.append(scope_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "scope": scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.api_key_scope import ApiKeyScope

        d = dict(src_dict)
        name = d.pop("name")

        scope = []
        _scope = d.pop("scope")
        for scope_item_data in _scope:
            scope_item = ApiKeyScope.from_dict(scope_item_data)

            scope.append(scope_item)

        api_key_self_write = cls(
            name=name,
            scope=scope,
        )

        return api_key_self_write
