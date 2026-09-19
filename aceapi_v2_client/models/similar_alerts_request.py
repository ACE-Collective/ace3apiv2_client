from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_filters_body import SearchFiltersBody


T = TypeVar("T", bound="SimilarAlertsRequest")


@_attrs_define
class SimilarAlertsRequest:
    """Alerts most similar to a given alert, by the alert's own indexed text.

    Attributes:
        alert_uuid (str):
        filters (SearchFiltersBody | Unset): Filters applied before ranking. Lists match any of their values; the
            filters themselves
            are ANDed together.
        limit (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.
        include_hits (bool | Unset):  Default: True.
    """

    alert_uuid: str
    filters: SearchFiltersBody | Unset = UNSET
    limit: int | Unset = 10
    offset: int | Unset = 0
    include_hits: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_uuid = self.alert_uuid

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        limit = self.limit

        offset = self.offset

        include_hits = self.include_hits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_uuid": alert_uuid,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if include_hits is not UNSET:
            field_dict["include_hits"] = include_hits

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.search_filters_body import SearchFiltersBody

        d = dict(src_dict)
        alert_uuid = d.pop("alert_uuid")

        _filters = d.pop("filters", UNSET)
        filters: SearchFiltersBody | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = SearchFiltersBody.from_dict(_filters)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        include_hits = d.pop("include_hits", UNSET)

        similar_alerts_request = cls(
            alert_uuid=alert_uuid,
            filters=filters,
            limit=limit,
            offset=offset,
            include_hits=include_hits,
        )

        similar_alerts_request.additional_properties = d
        return similar_alerts_request

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
