from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.alert_search_request_lanes_item import AlertSearchRequestLanesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_filters_body import SearchFiltersBody


T = TypeVar("T", bound="AlertSearchRequest")


@_attrs_define
class AlertSearchRequest:
    """Hybrid search over alerts: exact matches for the things named with a `field:value` term,
    plus semantic matches over the alert's text (description, comments, detections, email
    content, command lines, ...).

    Either `query` or `filters` is required. With filters and no query the response is a plain
    newest-first listing: no ranking, and every result's `tier` is null.

        Attributes:
            query (None | str | Unset): free text for the semantic lanes, plus any number of `field:value` terms. A term is
                `tag:phish`, `uuid:<alert uuid>`, `<observable type>:<value>` (e.g. `ipv4:1.2.3.4`, `signature_id:<uuid>`),
                `observable:<type>:<value>` for values containing colons, or a filter slug such as `queue:default`,
                `disposition:DELIVERY`, `alert_date:-7d` or `detection_point:<signature uuid>[:<version>]`. Prefix with `-` to
                invert, quote a value containing a space or comma, separate ORed values with commas. An unrecognized prefix is
                ordinary text. A bare word or indicator is searched semantically only -- it never runs an exact lookup.
            filters (SearchFiltersBody | Unset): Filters applied before ranking. Lists match any of their values; the
                filters themselves
                are ANDed together.
            limit (int | Unset): page size Default: 20.
            offset (int | Unset):  Default: 0.
            include_hits (bool | Unset): include the matching snippets for each alert Default: True.
            lanes (list[AlertSearchRequestLanesItem] | Unset):
    """

    query: None | str | Unset = UNSET
    filters: SearchFiltersBody | Unset = UNSET
    limit: int | Unset = 20
    offset: int | Unset = 0
    include_hits: bool | Unset = True
    lanes: list[AlertSearchRequestLanesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        limit = self.limit

        offset = self.offset

        include_hits = self.include_hits

        lanes: list[str] | Unset = UNSET
        if not isinstance(self.lanes, Unset):
            lanes = []
            for lanes_item_data in self.lanes:
                lanes_item = lanes_item_data.value
                lanes.append(lanes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if filters is not UNSET:
            field_dict["filters"] = filters
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if include_hits is not UNSET:
            field_dict["include_hits"] = include_hits
        if lanes is not UNSET:
            field_dict["lanes"] = lanes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.search_filters_body import SearchFiltersBody

        d = dict(src_dict)

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: SearchFiltersBody | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = SearchFiltersBody.from_dict(_filters)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        include_hits = d.pop("include_hits", UNSET)

        _lanes = d.pop("lanes", UNSET)
        lanes: list[AlertSearchRequestLanesItem] | Unset = UNSET
        if _lanes is not UNSET:
            lanes = []
            for lanes_item_data in _lanes:
                lanes_item = AlertSearchRequestLanesItem(lanes_item_data)

                lanes.append(lanes_item)

        alert_search_request = cls(
            query=query,
            filters=filters,
            limit=limit,
            offset=offset,
            include_hits=include_hits,
            lanes=lanes,
        )

        alert_search_request.additional_properties = d
        return alert_search_request

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
