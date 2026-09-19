from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_membership import EventMembership
    from ..models.observable_lookup_result_disposition_counts import (
        ObservableLookupResultDispositionCounts,
    )
    from ..models.recent_alert_summary import RecentAlertSummary


T = TypeVar("T", bound="ObservableLookupResult")


@_attrs_define
class ObservableLookupResult:
    """Per-pair result, positionally aligned with the request (key on index, not value: the
    echoed type/value are the normalized forms, e.g. a lowercased file hash).

    Alerts with alert_type 'faqueue' are never counted. disposition_counts is the raw
    histogram including OPEN and UNKNOWN (unlike the GUI's disposition history, which drops
    UNKNOWN), so total_alert_count == sum(disposition_counts.values()) always holds.
    found=false with error=null means the observable has never been indexed; found=true with
    total_alert_count=0 means every containing alert was faqueue, excluded, or before since.

        Attributes:
            index (int):
            type_ (str):
            value (None | str | Unset):
            found (bool | Unset):  Default: False.
            error (None | str | Unset):
            total_alert_count (int | Unset):  Default: 0.
            first_seen (datetime.datetime | None | Unset):
            last_seen (datetime.datetime | None | Unset):
            disposition_counts (ObservableLookupResultDispositionCounts | Unset):
            recent_alerts (list[RecentAlertSummary] | Unset):
            events (list[EventMembership] | Unset):
    """

    index: int
    type_: str
    value: None | str | Unset = UNSET
    found: bool | Unset = False
    error: None | str | Unset = UNSET
    total_alert_count: int | Unset = 0
    first_seen: datetime.datetime | None | Unset = UNSET
    last_seen: datetime.datetime | None | Unset = UNSET
    disposition_counts: ObservableLookupResultDispositionCounts | Unset = UNSET
    recent_alerts: list[RecentAlertSummary] | Unset = UNSET
    events: list[EventMembership] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        type_ = self.type_

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        found = self.found

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        total_alert_count = self.total_alert_count

        first_seen: None | str | Unset
        if isinstance(self.first_seen, Unset):
            first_seen = UNSET
        elif isinstance(self.first_seen, datetime.datetime):
            first_seen = self.first_seen.isoformat()
        else:
            first_seen = self.first_seen

        last_seen: None | str | Unset
        if isinstance(self.last_seen, Unset):
            last_seen = UNSET
        elif isinstance(self.last_seen, datetime.datetime):
            last_seen = self.last_seen.isoformat()
        else:
            last_seen = self.last_seen

        disposition_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disposition_counts, Unset):
            disposition_counts = self.disposition_counts.to_dict()

        recent_alerts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recent_alerts, Unset):
            recent_alerts = []
            for recent_alerts_item_data in self.recent_alerts:
                recent_alerts_item = recent_alerts_item_data.to_dict()
                recent_alerts.append(recent_alerts_item)

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "type": type_,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if found is not UNSET:
            field_dict["found"] = found
        if error is not UNSET:
            field_dict["error"] = error
        if total_alert_count is not UNSET:
            field_dict["total_alert_count"] = total_alert_count
        if first_seen is not UNSET:
            field_dict["first_seen"] = first_seen
        if last_seen is not UNSET:
            field_dict["last_seen"] = last_seen
        if disposition_counts is not UNSET:
            field_dict["disposition_counts"] = disposition_counts
        if recent_alerts is not UNSET:
            field_dict["recent_alerts"] = recent_alerts
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.event_membership import EventMembership
        from ..models.observable_lookup_result_disposition_counts import (
            ObservableLookupResultDispositionCounts,
        )
        from ..models.recent_alert_summary import RecentAlertSummary

        d = dict(src_dict)
        index = d.pop("index")

        type_ = d.pop("type")

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        found = d.pop("found", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        total_alert_count = d.pop("total_alert_count", UNSET)

        def _parse_first_seen(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_seen_type_0 = datetime.datetime.fromisoformat(data)

                return first_seen_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_seen = _parse_first_seen(d.pop("first_seen", UNSET))

        def _parse_last_seen(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_type_0 = datetime.datetime.fromisoformat(data)

                return last_seen_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_seen = _parse_last_seen(d.pop("last_seen", UNSET))

        _disposition_counts = d.pop("disposition_counts", UNSET)
        disposition_counts: ObservableLookupResultDispositionCounts | Unset
        if isinstance(_disposition_counts, Unset):
            disposition_counts = UNSET
        else:
            disposition_counts = ObservableLookupResultDispositionCounts.from_dict(
                _disposition_counts
            )

        _recent_alerts = d.pop("recent_alerts", UNSET)
        recent_alerts: list[RecentAlertSummary] | Unset = UNSET
        if _recent_alerts is not UNSET:
            recent_alerts = []
            for recent_alerts_item_data in _recent_alerts:
                recent_alerts_item = RecentAlertSummary.from_dict(
                    recent_alerts_item_data
                )

                recent_alerts.append(recent_alerts_item)

        _events = d.pop("events", UNSET)
        events: list[EventMembership] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = EventMembership.from_dict(events_item_data)

                events.append(events_item)

        observable_lookup_result = cls(
            index=index,
            type_=type_,
            value=value,
            found=found,
            error=error,
            total_alert_count=total_alert_count,
            first_seen=first_seen,
            last_seen=last_seen,
            disposition_counts=disposition_counts,
            recent_alerts=recent_alerts,
            events=events,
        )

        observable_lookup_result.additional_properties = d
        return observable_lookup_result

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
