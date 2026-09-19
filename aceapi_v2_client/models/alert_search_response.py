from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.alert_search_response_lanes_used_item import (
    AlertSearchResponseLanesUsedItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_search_response_timings_ms import AlertSearchResponseTimingsMs
    from ..models.alert_search_result_out import AlertSearchResultOut


T = TypeVar("T", bound="AlertSearchResponse")


@_attrs_define
class AlertSearchResponse:
    """
    Attributes:
        query (str):
        total (int): number of matching alerts (capped by the search.max_results setting)
        offset (int):
        limit (int):
        results (list[AlertSearchResultOut]):
        lanes_used (list[AlertSearchResponseLanesUsedItem]):
        timings_ms (AlertSearchResponseTimingsMs):
        errors (list[str] | Unset): query language problems. When this is non-empty nothing was searched: a term that
            cannot be honored is reported rather than dropped, because dropping it would return MORE alerts than were asked
            for
    """

    query: str
    total: int
    offset: int
    limit: int
    results: list[AlertSearchResultOut]
    lanes_used: list[AlertSearchResponseLanesUsedItem]
    timings_ms: AlertSearchResponseTimingsMs
    errors: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        total = self.total

        offset = self.offset

        limit = self.limit

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        lanes_used = []
        for lanes_used_item_data in self.lanes_used:
            lanes_used_item = lanes_used_item_data.value
            lanes_used.append(lanes_used_item)

        timings_ms = self.timings_ms.to_dict()

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "total": total,
                "offset": offset,
                "limit": limit,
                "results": results,
                "lanes_used": lanes_used,
                "timings_ms": timings_ms,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_search_response_timings_ms import (
            AlertSearchResponseTimingsMs,
        )
        from ..models.alert_search_result_out import (
            AlertSearchResultOut,
        )

        d = dict(src_dict)
        query = d.pop("query")

        total = d.pop("total")

        offset = d.pop("offset")

        limit = d.pop("limit")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = AlertSearchResultOut.from_dict(results_item_data)

            results.append(results_item)

        lanes_used = []
        _lanes_used = d.pop("lanes_used")
        for lanes_used_item_data in _lanes_used:
            lanes_used_item = AlertSearchResponseLanesUsedItem(lanes_used_item_data)

            lanes_used.append(lanes_used_item)

        timings_ms = AlertSearchResponseTimingsMs.from_dict(d.pop("timings_ms"))

        errors = cast(list[str], d.pop("errors", UNSET))

        alert_search_response = cls(
            query=query,
            total=total,
            offset=offset,
            limit=limit,
            results=results,
            lanes_used=lanes_used,
            timings_ms=timings_ms,
            errors=errors,
        )

        alert_search_response.additional_properties = d
        return alert_search_response

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
