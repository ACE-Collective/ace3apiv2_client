from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Attribution")


@_attrs_define
class Attribution:
    """One detection of an alert attributed to a run, removed ones included (docs/SVS_API.md,
    *Attributions*).

        Attributes:
            id (int): the row's id
            run_id (str): the run's uuid
            alert_uuid (str):
            detection (str): the detection's content_hash (its detection_points row)
            signature_uuid (str):
            confidence (str): marker or context; a person's association is marker
            late (bool): the alert's event came after the run's observation window
            cleanup (bool): its event time is at or after the run's cleanup_at: the test's cleanup caused it, so it is left
                out of the run's candidates and expectations
            fallback_time (bool): event_time is a fallback (query_time, now or insert_time), which may have put the alert in
                the wrong window
            source (str): router (the marker router) or manual (a person associated the alert)
            actor (str): who attributed it: svs for the router, else the person
            created_at (datetime.datetime):
            updated_at (datetime.datetime): the feed's changed_since key
            signature_family (None | str | Unset):
            event_time (datetime.datetime | None | Unset): the alert's event time it was judged by; null for attributions
                written before it was kept
            event_time_source (None | str | Unset): where event_time came from: event (the event's own), query_time (a hunt
                couldn't extract it), now (nothing gave the alert a time, so its producer used the time it created it) or
                insert_time (the alert has none); null for attributions written before it was kept
            scan_point (None | str | Unset): where the agreeing marker was found; null for context or manual
            actor_user (None | str | Unset): the person's username
            removed_at (datetime.datetime | None | Unset): when it stopped holding; null while it holds
            removed_by (None | str | Unset): svs (the router found it no longer applies) or the person who disassociated it
            removed_by_user (None | str | Unset):
            removal_reason (None | str | Unset):
            kept_at (datetime.datetime | None | Unset): when a person kept this context attribution
            kept_by_user (None | str | Unset):
    """

    id: int
    run_id: str
    alert_uuid: str
    detection: str
    signature_uuid: str
    confidence: str
    late: bool
    cleanup: bool
    fallback_time: bool
    source: str
    actor: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    signature_family: None | str | Unset = UNSET
    event_time: datetime.datetime | None | Unset = UNSET
    event_time_source: None | str | Unset = UNSET
    scan_point: None | str | Unset = UNSET
    actor_user: None | str | Unset = UNSET
    removed_at: datetime.datetime | None | Unset = UNSET
    removed_by: None | str | Unset = UNSET
    removed_by_user: None | str | Unset = UNSET
    removal_reason: None | str | Unset = UNSET
    kept_at: datetime.datetime | None | Unset = UNSET
    kept_by_user: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        run_id = self.run_id

        alert_uuid = self.alert_uuid

        detection = self.detection

        signature_uuid = self.signature_uuid

        confidence = self.confidence

        late = self.late

        cleanup = self.cleanup

        fallback_time = self.fallback_time

        source = self.source

        actor = self.actor

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        signature_family: None | str | Unset
        if isinstance(self.signature_family, Unset):
            signature_family = UNSET
        else:
            signature_family = self.signature_family

        event_time: None | str | Unset
        if isinstance(self.event_time, Unset):
            event_time = UNSET
        elif isinstance(self.event_time, datetime.datetime):
            event_time = self.event_time.isoformat()
        else:
            event_time = self.event_time

        event_time_source: None | str | Unset
        if isinstance(self.event_time_source, Unset):
            event_time_source = UNSET
        else:
            event_time_source = self.event_time_source

        scan_point: None | str | Unset
        if isinstance(self.scan_point, Unset):
            scan_point = UNSET
        else:
            scan_point = self.scan_point

        actor_user: None | str | Unset
        if isinstance(self.actor_user, Unset):
            actor_user = UNSET
        else:
            actor_user = self.actor_user

        removed_at: None | str | Unset
        if isinstance(self.removed_at, Unset):
            removed_at = UNSET
        elif isinstance(self.removed_at, datetime.datetime):
            removed_at = self.removed_at.isoformat()
        else:
            removed_at = self.removed_at

        removed_by: None | str | Unset
        if isinstance(self.removed_by, Unset):
            removed_by = UNSET
        else:
            removed_by = self.removed_by

        removed_by_user: None | str | Unset
        if isinstance(self.removed_by_user, Unset):
            removed_by_user = UNSET
        else:
            removed_by_user = self.removed_by_user

        removal_reason: None | str | Unset
        if isinstance(self.removal_reason, Unset):
            removal_reason = UNSET
        else:
            removal_reason = self.removal_reason

        kept_at: None | str | Unset
        if isinstance(self.kept_at, Unset):
            kept_at = UNSET
        elif isinstance(self.kept_at, datetime.datetime):
            kept_at = self.kept_at.isoformat()
        else:
            kept_at = self.kept_at

        kept_by_user: None | str | Unset
        if isinstance(self.kept_by_user, Unset):
            kept_by_user = UNSET
        else:
            kept_by_user = self.kept_by_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "run_id": run_id,
                "alert_uuid": alert_uuid,
                "detection": detection,
                "signature_uuid": signature_uuid,
                "confidence": confidence,
                "late": late,
                "cleanup": cleanup,
                "fallback_time": fallback_time,
                "source": source,
                "actor": actor,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if signature_family is not UNSET:
            field_dict["signature_family"] = signature_family
        if event_time is not UNSET:
            field_dict["event_time"] = event_time
        if event_time_source is not UNSET:
            field_dict["event_time_source"] = event_time_source
        if scan_point is not UNSET:
            field_dict["scan_point"] = scan_point
        if actor_user is not UNSET:
            field_dict["actor_user"] = actor_user
        if removed_at is not UNSET:
            field_dict["removed_at"] = removed_at
        if removed_by is not UNSET:
            field_dict["removed_by"] = removed_by
        if removed_by_user is not UNSET:
            field_dict["removed_by_user"] = removed_by_user
        if removal_reason is not UNSET:
            field_dict["removal_reason"] = removal_reason
        if kept_at is not UNSET:
            field_dict["kept_at"] = kept_at
        if kept_by_user is not UNSET:
            field_dict["kept_by_user"] = kept_by_user

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        run_id = d.pop("run_id")

        alert_uuid = d.pop("alert_uuid")

        detection = d.pop("detection")

        signature_uuid = d.pop("signature_uuid")

        confidence = d.pop("confidence")

        late = d.pop("late")

        cleanup = d.pop("cleanup")

        fallback_time = d.pop("fallback_time")

        source = d.pop("source")

        actor = d.pop("actor")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_signature_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature_family = _parse_signature_family(d.pop("signature_family", UNSET))

        def _parse_event_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                event_time_type_0 = datetime.datetime.fromisoformat(data)

                return event_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        event_time = _parse_event_time(d.pop("event_time", UNSET))

        def _parse_event_time_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_time_source = _parse_event_time_source(d.pop("event_time_source", UNSET))

        def _parse_scan_point(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scan_point = _parse_scan_point(d.pop("scan_point", UNSET))

        def _parse_actor_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actor_user = _parse_actor_user(d.pop("actor_user", UNSET))

        def _parse_removed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                removed_at_type_0 = datetime.datetime.fromisoformat(data)

                return removed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        removed_at = _parse_removed_at(d.pop("removed_at", UNSET))

        def _parse_removed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        removed_by = _parse_removed_by(d.pop("removed_by", UNSET))

        def _parse_removed_by_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        removed_by_user = _parse_removed_by_user(d.pop("removed_by_user", UNSET))

        def _parse_removal_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        removal_reason = _parse_removal_reason(d.pop("removal_reason", UNSET))

        def _parse_kept_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kept_at_type_0 = datetime.datetime.fromisoformat(data)

                return kept_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        kept_at = _parse_kept_at(d.pop("kept_at", UNSET))

        def _parse_kept_by_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kept_by_user = _parse_kept_by_user(d.pop("kept_by_user", UNSET))

        attribution = cls(
            id=id,
            run_id=run_id,
            alert_uuid=alert_uuid,
            detection=detection,
            signature_uuid=signature_uuid,
            confidence=confidence,
            late=late,
            cleanup=cleanup,
            fallback_time=fallback_time,
            source=source,
            actor=actor,
            created_at=created_at,
            updated_at=updated_at,
            signature_family=signature_family,
            event_time=event_time,
            event_time_source=event_time_source,
            scan_point=scan_point,
            actor_user=actor_user,
            removed_at=removed_at,
            removed_by=removed_by,
            removed_by_user=removed_by_user,
            removal_reason=removal_reason,
            kept_at=kept_at,
            kept_by_user=kept_by_user,
        )

        attribution.additional_properties = d
        return attribution

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
