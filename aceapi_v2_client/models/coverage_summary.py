from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coverage_summary_own_states import CoverageSummaryOwnStates
    from ..models.coverage_summary_states import CoverageSummaryStates
    from ..models.platform_counts import PlatformCounts


T = TypeVar("T", bound="CoverageSummary")


@_attrs_define
class CoverageSummary:
    """The rows the filters match, counted, and what the last refresh did.

    Attributes:
        rows (int):
        states (CoverageSummaryStates): rows per state, every state named
        own_states (CoverageSummaryOwnStates): rows per own_state, every state named
        platforms (list[PlatformCounts]): the same per platform, in the release's platform order
        attack_release (None | str | Unset): the ATT&CK release of the last refresh
        refreshed_at (datetime.datetime | None | Unset): when the last refresh completed; null before the first
        duration_ms (int | None | Unset):
        unknown_tags (int | Unset): mitre: tags naming an id the release doesn't have Default: 0.
        ignored_tags (int | Unset): mitre: tags that aren't technique ids (templated, tactics) Default: 0.
        error (None | str | Unset): why the latest refresh failed; null once one completes
    """

    rows: int
    states: CoverageSummaryStates
    own_states: CoverageSummaryOwnStates
    platforms: list[PlatformCounts]
    attack_release: None | str | Unset = UNSET
    refreshed_at: datetime.datetime | None | Unset = UNSET
    duration_ms: int | None | Unset = UNSET
    unknown_tags: int | Unset = 0
    ignored_tags: int | Unset = 0
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rows = self.rows

        states = self.states.to_dict()

        own_states = self.own_states.to_dict()

        platforms = []
        for platforms_item_data in self.platforms:
            platforms_item = platforms_item_data.to_dict()
            platforms.append(platforms_item)

        attack_release: None | str | Unset
        if isinstance(self.attack_release, Unset):
            attack_release = UNSET
        else:
            attack_release = self.attack_release

        refreshed_at: None | str | Unset
        if isinstance(self.refreshed_at, Unset):
            refreshed_at = UNSET
        elif isinstance(self.refreshed_at, datetime.datetime):
            refreshed_at = self.refreshed_at.isoformat()
        else:
            refreshed_at = self.refreshed_at

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        unknown_tags = self.unknown_tags

        ignored_tags = self.ignored_tags

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rows": rows,
                "states": states,
                "own_states": own_states,
                "platforms": platforms,
            }
        )
        if attack_release is not UNSET:
            field_dict["attack_release"] = attack_release
        if refreshed_at is not UNSET:
            field_dict["refreshed_at"] = refreshed_at
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if unknown_tags is not UNSET:
            field_dict["unknown_tags"] = unknown_tags
        if ignored_tags is not UNSET:
            field_dict["ignored_tags"] = ignored_tags
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.coverage_summary_own_states import CoverageSummaryOwnStates
        from ..models.coverage_summary_states import CoverageSummaryStates
        from ..models.platform_counts import PlatformCounts

        d = dict(src_dict)
        rows = d.pop("rows")

        states = CoverageSummaryStates.from_dict(d.pop("states"))

        own_states = CoverageSummaryOwnStates.from_dict(d.pop("own_states"))

        platforms = []
        _platforms = d.pop("platforms")
        for platforms_item_data in _platforms:
            platforms_item = PlatformCounts.from_dict(platforms_item_data)

            platforms.append(platforms_item)

        def _parse_attack_release(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attack_release = _parse_attack_release(d.pop("attack_release", UNSET))

        def _parse_refreshed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                refreshed_at_type_0 = datetime.datetime.fromisoformat(data)

                return refreshed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        refreshed_at = _parse_refreshed_at(d.pop("refreshed_at", UNSET))

        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        unknown_tags = d.pop("unknown_tags", UNSET)

        ignored_tags = d.pop("ignored_tags", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        coverage_summary = cls(
            rows=rows,
            states=states,
            own_states=own_states,
            platforms=platforms,
            attack_release=attack_release,
            refreshed_at=refreshed_at,
            duration_ms=duration_ms,
            unknown_tags=unknown_tags,
            ignored_tags=ignored_tags,
            error=error,
        )

        coverage_summary.additional_properties = d
        return coverage_summary

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
