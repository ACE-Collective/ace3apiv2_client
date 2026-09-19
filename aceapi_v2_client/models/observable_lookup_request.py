from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookup_pair import LookupPair


T = TypeVar("T", bound="ObservableLookupRequest")


@_attrs_define
class ObservableLookupRequest:
    """Batch prevalence lookup: how often, how recently, and with what dispositions each
    observable has appeared across alerts, and which events those alerts belong to.

    since bounds the counted/listed alerts by insert_date but does NOT filter events — an old
    event membership is still worth surfacing. exclude_alert_uuids removes specific alerts
    (typically the caller's own) from counts, recent alerts, and events; unknown UUIDs are
    silently ignored.

        Attributes:
            observables (list[LookupPair]):
            recent_alert_limit (int | Unset):  Default: 5.
            exclude_alert_uuids (list[str] | Unset):
            since (datetime.datetime | None | Unset):
    """

    observables: list[LookupPair]
    recent_alert_limit: int | Unset = 5
    exclude_alert_uuids: list[str] | Unset = UNSET
    since: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observables = []
        for observables_item_data in self.observables:
            observables_item = observables_item_data.to_dict()
            observables.append(observables_item)

        recent_alert_limit = self.recent_alert_limit

        exclude_alert_uuids: list[str] | Unset = UNSET
        if not isinstance(self.exclude_alert_uuids, Unset):
            exclude_alert_uuids = self.exclude_alert_uuids

        since: None | str | Unset
        if isinstance(self.since, Unset):
            since = UNSET
        elif isinstance(self.since, datetime.datetime):
            since = self.since.isoformat()
        else:
            since = self.since

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "observables": observables,
            }
        )
        if recent_alert_limit is not UNSET:
            field_dict["recent_alert_limit"] = recent_alert_limit
        if exclude_alert_uuids is not UNSET:
            field_dict["exclude_alert_uuids"] = exclude_alert_uuids
        if since is not UNSET:
            field_dict["since"] = since

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lookup_pair import LookupPair

        d = dict(src_dict)
        observables = []
        _observables = d.pop("observables")
        for observables_item_data in _observables:
            observables_item = LookupPair.from_dict(observables_item_data)

            observables.append(observables_item)

        recent_alert_limit = d.pop("recent_alert_limit", UNSET)

        exclude_alert_uuids = cast(list[str], d.pop("exclude_alert_uuids", UNSET))

        def _parse_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                since_type_0 = datetime.datetime.fromisoformat(data)

                return since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        since = _parse_since(d.pop("since", UNSET))

        observable_lookup_request = cls(
            observables=observables,
            recent_alert_limit=recent_alert_limit,
            exclude_alert_uuids=exclude_alert_uuids,
            since=since,
        )

        observable_lookup_request.additional_properties = d
        return observable_lookup_request

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
