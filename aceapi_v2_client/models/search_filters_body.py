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
    from ..models.lookup_pair import LookupPair


T = TypeVar("T", bound="SearchFiltersBody")


@_attrs_define
class SearchFiltersBody:
    """Filters applied before ranking. Lists match any of their values; the filters themselves
    are ANDed together.

        Attributes:
            insert_date_start (datetime.datetime | None | Unset): only alerts created at or after this time (timezone-aware)
            insert_date_end (datetime.datetime | None | Unset): only alerts created at or before this time (timezone-aware)
            alert_types (list[str] | Unset):
            dispositions (list[str] | Unset): e.g. OPEN, FALSE_POSITIVE, DELIVERY
            queues (list[str] | Unset):
            tags (list[str] | Unset): exact tag names (case-insensitive)
            exclude_alert_uuids (list[str] | Unset):
            observables (list[LookupPair] | Unset): only alerts carrying ALL of these observables; the value is normalized
                the same way the analysis engine normalizes it, and a file observable's value is its content sha256 hex digest
            detection_points (list[str] | Unset): only alerts with a detection point from ANY of these signatures, each
                written <signature uuid>[:<signature version>]; without a version any version matches
            filters (list[FilterEntry] | Unset): the rest of the alert management filter vocabulary, in the same {name,
                inverted, values} shape the GUI and share links use -- e.g. {"name": "Owner", "inverted": true, "values":
                ["None"]}
    """

    insert_date_start: datetime.datetime | None | Unset = UNSET
    insert_date_end: datetime.datetime | None | Unset = UNSET
    alert_types: list[str] | Unset = UNSET
    dispositions: list[str] | Unset = UNSET
    queues: list[str] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    exclude_alert_uuids: list[str] | Unset = UNSET
    observables: list[LookupPair] | Unset = UNSET
    detection_points: list[str] | Unset = UNSET
    filters: list[FilterEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        insert_date_start: None | str | Unset
        if isinstance(self.insert_date_start, Unset):
            insert_date_start = UNSET
        elif isinstance(self.insert_date_start, datetime.datetime):
            insert_date_start = self.insert_date_start.isoformat()
        else:
            insert_date_start = self.insert_date_start

        insert_date_end: None | str | Unset
        if isinstance(self.insert_date_end, Unset):
            insert_date_end = UNSET
        elif isinstance(self.insert_date_end, datetime.datetime):
            insert_date_end = self.insert_date_end.isoformat()
        else:
            insert_date_end = self.insert_date_end

        alert_types: list[str] | Unset = UNSET
        if not isinstance(self.alert_types, Unset):
            alert_types = self.alert_types

        dispositions: list[str] | Unset = UNSET
        if not isinstance(self.dispositions, Unset):
            dispositions = self.dispositions

        queues: list[str] | Unset = UNSET
        if not isinstance(self.queues, Unset):
            queues = self.queues

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        exclude_alert_uuids: list[str] | Unset = UNSET
        if not isinstance(self.exclude_alert_uuids, Unset):
            exclude_alert_uuids = self.exclude_alert_uuids

        observables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.observables, Unset):
            observables = []
            for observables_item_data in self.observables:
                observables_item = observables_item_data.to_dict()
                observables.append(observables_item)

        detection_points: list[str] | Unset = UNSET
        if not isinstance(self.detection_points, Unset):
            detection_points = self.detection_points

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if insert_date_start is not UNSET:
            field_dict["insert_date_start"] = insert_date_start
        if insert_date_end is not UNSET:
            field_dict["insert_date_end"] = insert_date_end
        if alert_types is not UNSET:
            field_dict["alert_types"] = alert_types
        if dispositions is not UNSET:
            field_dict["dispositions"] = dispositions
        if queues is not UNSET:
            field_dict["queues"] = queues
        if tags is not UNSET:
            field_dict["tags"] = tags
        if exclude_alert_uuids is not UNSET:
            field_dict["exclude_alert_uuids"] = exclude_alert_uuids
        if observables is not UNSET:
            field_dict["observables"] = observables
        if detection_points is not UNSET:
            field_dict["detection_points"] = detection_points
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_entry import FilterEntry
        from ..models.lookup_pair import LookupPair

        d = dict(src_dict)

        def _parse_insert_date_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                insert_date_start_type_0 = datetime.datetime.fromisoformat(data)

                return insert_date_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        insert_date_start = _parse_insert_date_start(d.pop("insert_date_start", UNSET))

        def _parse_insert_date_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                insert_date_end_type_0 = datetime.datetime.fromisoformat(data)

                return insert_date_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        insert_date_end = _parse_insert_date_end(d.pop("insert_date_end", UNSET))

        alert_types = cast(list[str], d.pop("alert_types", UNSET))

        dispositions = cast(list[str], d.pop("dispositions", UNSET))

        queues = cast(list[str], d.pop("queues", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        exclude_alert_uuids = cast(list[str], d.pop("exclude_alert_uuids", UNSET))

        _observables = d.pop("observables", UNSET)
        observables: list[LookupPair] | Unset = UNSET
        if _observables is not UNSET:
            observables = []
            for observables_item_data in _observables:
                observables_item = LookupPair.from_dict(observables_item_data)

                observables.append(observables_item)

        detection_points = cast(list[str], d.pop("detection_points", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: list[FilterEntry] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = FilterEntry.from_dict(filters_item_data)

                filters.append(filters_item)

        search_filters_body = cls(
            insert_date_start=insert_date_start,
            insert_date_end=insert_date_end,
            alert_types=alert_types,
            dispositions=dispositions,
            queues=queues,
            tags=tags,
            exclude_alert_uuids=exclude_alert_uuids,
            observables=observables,
            detection_points=detection_points,
            filters=filters,
        )

        search_filters_body.additional_properties = d
        return search_filters_body

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
