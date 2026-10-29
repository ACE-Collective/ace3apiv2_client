from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.filter_field_kind import FilterFieldKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterDescriptor")


@_attrs_define
class FilterDescriptor:
    """One filter a screen supports.

    Attributes:
        name (str): the filter's name, as it appears in a filter entry
        slug (str): the filter's name in a share link's f= parameter; permanent
        kind (FilterFieldKind | None | Unset): how a generic editor edits it; null when the screen has its own editor
        options (list[str] | Unset): the values a multi field offers
    """

    name: str
    slug: str
    kind: FilterFieldKind | None | Unset = UNSET
    options: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        elif isinstance(self.kind, FilterFieldKind):
            kind = self.kind.value
        else:
            kind = self.kind

        options: list[str] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        def _parse_kind(data: object) -> FilterFieldKind | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_0 = FilterFieldKind(data)

                return kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FilterFieldKind | None | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        options = cast(list[str], d.pop("options", UNSET))

        filter_descriptor = cls(
            name=name,
            slug=slug,
            kind=kind,
            options=options,
        )

        filter_descriptor.additional_properties = d
        return filter_descriptor

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
