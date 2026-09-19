from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.search_hit_out_lane import SearchHitOutLane
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchHitOut")


@_attrs_define
class SearchHitOut:
    """
    Attributes:
        lane (SearchHitOutLane):
        kind (str): alert, comment, detection, analysis, context (semantic) or observable, tag, uuid (lexical)
        text (str):
        score (float): lane-native score: 1.0 for an exact match, the fused qdrant score for a semantic hit; not
            comparable across lanes
        title (None | str | Unset):
    """

    lane: SearchHitOutLane
    kind: str
    text: str
    score: float
    title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lane = self.lane.value

        kind = self.kind

        text = self.text

        score = self.score

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lane": lane,
                "kind": kind,
                "text": text,
                "score": score,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lane = SearchHitOutLane(d.pop("lane"))

        kind = d.pop("kind")

        text = d.pop("text")

        score = d.pop("score")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        search_hit_out = cls(
            lane=lane,
            kind=kind,
            text=text,
            score=score,
            title=title,
        )

        search_hit_out.additional_properties = d
        return search_hit_out

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
