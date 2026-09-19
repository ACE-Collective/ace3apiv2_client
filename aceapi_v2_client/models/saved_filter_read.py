from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_entry import FilterEntry


T = TypeVar("T", bound="SavedFilterRead")


@_attrs_define
class SavedFilterRead:
    """A saved filter as returned to callers.

    Attributes:
        uuid (str):
        kind (str):
        filters (list[FilterEntry]):
        owner_id (int):
        owner_display_name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (None | str | Unset):
        description (None | str | Unset):
        quick_filter_order (int | None | Unset):
        quick_filter_indicator (bool | Unset):  Default: False.
    """

    uuid: str
    kind: str
    filters: list[FilterEntry]
    owner_id: int
    owner_display_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    quick_filter_order: int | None | Unset = UNSET
    quick_filter_indicator: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        kind = self.kind

        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        owner_id = self.owner_id

        owner_display_name = self.owner_display_name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        quick_filter_order: int | None | Unset
        if isinstance(self.quick_filter_order, Unset):
            quick_filter_order = UNSET
        else:
            quick_filter_order = self.quick_filter_order

        quick_filter_indicator = self.quick_filter_indicator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "kind": kind,
                "filters": filters,
                "owner_id": owner_id,
                "owner_display_name": owner_display_name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if quick_filter_order is not UNSET:
            field_dict["quick_filter_order"] = quick_filter_order
        if quick_filter_indicator is not UNSET:
            field_dict["quick_filter_indicator"] = quick_filter_indicator

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_entry import FilterEntry

        d = dict(src_dict)
        uuid = d.pop("uuid")

        kind = d.pop("kind")

        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = FilterEntry.from_dict(filters_item_data)

            filters.append(filters_item)

        owner_id = d.pop("owner_id")

        owner_display_name = d.pop("owner_display_name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_quick_filter_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quick_filter_order = _parse_quick_filter_order(
            d.pop("quick_filter_order", UNSET)
        )

        quick_filter_indicator = d.pop("quick_filter_indicator", UNSET)

        saved_filter_read = cls(
            uuid=uuid,
            kind=kind,
            filters=filters,
            owner_id=owner_id,
            owner_display_name=owner_display_name,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            description=description,
            quick_filter_order=quick_filter_order,
            quick_filter_indicator=quick_filter_indicator,
        )

        saved_filter_read.additional_properties = d
        return saved_filter_read

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
