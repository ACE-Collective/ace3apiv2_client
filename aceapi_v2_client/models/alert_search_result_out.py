from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.alert_search_result_out_lanes_item import AlertSearchResultOutLanesItem
from ..models.alert_search_result_out_tier_type_0 import AlertSearchResultOutTierType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_summary_out import AlertSummaryOut
    from ..models.search_hit_out import SearchHitOut


T = TypeVar("T", bound="AlertSearchResultOut")


@_attrs_define
class AlertSearchResultOut:
    """
    Attributes:
        alert (AlertSummaryOut):
        rank (int):
        score (float): fused rank score (for ordering only)
        lanes (list[AlertSearchResultOutLanesItem]):
        tier (AlertSearchResultOutTierType0 | None | Unset): the evidence behind the match: exact = a field term matched
            verbatim; strong = clearly similar text (or similar text sharing terms with the query); good = similar text
            above the floor; weak = only a term in common. null on a filter-only request, which is a listing rather than a
            ranking
        hits (list[SearchHitOut] | Unset):
    """

    alert: AlertSummaryOut
    rank: int
    score: float
    lanes: list[AlertSearchResultOutLanesItem]
    tier: AlertSearchResultOutTierType0 | None | Unset = UNSET
    hits: list[SearchHitOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert = self.alert.to_dict()

        rank = self.rank

        score = self.score

        lanes = []
        for lanes_item_data in self.lanes:
            lanes_item = lanes_item_data.value
            lanes.append(lanes_item)

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        elif isinstance(self.tier, AlertSearchResultOutTierType0):
            tier = self.tier.value
        else:
            tier = self.tier

        hits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hits, Unset):
            hits = []
            for hits_item_data in self.hits:
                hits_item = hits_item_data.to_dict()
                hits.append(hits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert": alert,
                "rank": rank,
                "score": score,
                "lanes": lanes,
            }
        )
        if tier is not UNSET:
            field_dict["tier"] = tier
        if hits is not UNSET:
            field_dict["hits"] = hits

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_summary_out import AlertSummaryOut
        from ..models.search_hit_out import SearchHitOut

        d = dict(src_dict)
        alert = AlertSummaryOut.from_dict(d.pop("alert"))

        rank = d.pop("rank")

        score = d.pop("score")

        lanes = []
        _lanes = d.pop("lanes")
        for lanes_item_data in _lanes:
            lanes_item = AlertSearchResultOutLanesItem(lanes_item_data)

            lanes.append(lanes_item)

        def _parse_tier(data: object) -> AlertSearchResultOutTierType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tier_type_0 = AlertSearchResultOutTierType0(data)

                return tier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertSearchResultOutTierType0 | None | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))

        _hits = d.pop("hits", UNSET)
        hits: list[SearchHitOut] | Unset = UNSET
        if _hits is not UNSET:
            hits = []
            for hits_item_data in _hits:
                hits_item = SearchHitOut.from_dict(hits_item_data)

                hits.append(hits_item)

        alert_search_result_out = cls(
            alert=alert,
            rank=rank,
            score=score,
            lanes=lanes,
            tier=tier,
            hits=hits,
        )

        alert_search_result_out.additional_properties = d
        return alert_search_result_out

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
