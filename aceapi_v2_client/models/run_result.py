from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RunResult")


@_attrs_define
class RunResult:
    """One signature of a run's result (docs/SVS_RUNS.md, *Results*; docs/SVS_API.md, *Results*).

    Attributes:
        id (int): the row's id
        run_id (str): the run's uuid
        signature_uuid (str):
        alert_count (int): the run's attributed alerts that carry the signature
        late_only (bool): every attribution of it is late
        context_only (bool): every attribution of it is by context alone
        updated_at (datetime.datetime): the feed's changed_since key
        signature_family (None | str | Unset): yara, hunt, builtin, ...
        signature_name (None | str | Unset):
        status (None | str | Unset): hit, missing, possibly_suppressed, candidate, rejected, ignored or cleanup; null
            once the signature left the live result and the row holds only the reviewed result
        fallback_time (bool | Unset): some attribution of it was judged by a fallback event time (a hunt's query time,
            or the alert's insert time) Default: False.
        content_hash (None | str | Unset): the rule's own content hash when the result was computed
        suppressing_alert_uuid (None | str | Unset): possibly_suppressed: the hunt's latest alert within its suppression
            period; null when the hunter recorded that it dropped the run's match
        reviewed_status (None | str | Unset): the status as signed off; null until the run is reviewed
        reviewed_alert_count (int | None | Unset):
        reviewed_late_only (bool | None | Unset):
        reviewed_content_hash (None | str | Unset):
    """

    id: int
    run_id: str
    signature_uuid: str
    alert_count: int
    late_only: bool
    context_only: bool
    updated_at: datetime.datetime
    signature_family: None | str | Unset = UNSET
    signature_name: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    fallback_time: bool | Unset = False
    content_hash: None | str | Unset = UNSET
    suppressing_alert_uuid: None | str | Unset = UNSET
    reviewed_status: None | str | Unset = UNSET
    reviewed_alert_count: int | None | Unset = UNSET
    reviewed_late_only: bool | None | Unset = UNSET
    reviewed_content_hash: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        run_id = self.run_id

        signature_uuid = self.signature_uuid

        alert_count = self.alert_count

        late_only = self.late_only

        context_only = self.context_only

        updated_at = self.updated_at.isoformat()

        signature_family: None | str | Unset
        if isinstance(self.signature_family, Unset):
            signature_family = UNSET
        else:
            signature_family = self.signature_family

        signature_name: None | str | Unset
        if isinstance(self.signature_name, Unset):
            signature_name = UNSET
        else:
            signature_name = self.signature_name

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        fallback_time = self.fallback_time

        content_hash: None | str | Unset
        if isinstance(self.content_hash, Unset):
            content_hash = UNSET
        else:
            content_hash = self.content_hash

        suppressing_alert_uuid: None | str | Unset
        if isinstance(self.suppressing_alert_uuid, Unset):
            suppressing_alert_uuid = UNSET
        else:
            suppressing_alert_uuid = self.suppressing_alert_uuid

        reviewed_status: None | str | Unset
        if isinstance(self.reviewed_status, Unset):
            reviewed_status = UNSET
        else:
            reviewed_status = self.reviewed_status

        reviewed_alert_count: int | None | Unset
        if isinstance(self.reviewed_alert_count, Unset):
            reviewed_alert_count = UNSET
        else:
            reviewed_alert_count = self.reviewed_alert_count

        reviewed_late_only: bool | None | Unset
        if isinstance(self.reviewed_late_only, Unset):
            reviewed_late_only = UNSET
        else:
            reviewed_late_only = self.reviewed_late_only

        reviewed_content_hash: None | str | Unset
        if isinstance(self.reviewed_content_hash, Unset):
            reviewed_content_hash = UNSET
        else:
            reviewed_content_hash = self.reviewed_content_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "run_id": run_id,
                "signature_uuid": signature_uuid,
                "alert_count": alert_count,
                "late_only": late_only,
                "context_only": context_only,
                "updated_at": updated_at,
            }
        )
        if signature_family is not UNSET:
            field_dict["signature_family"] = signature_family
        if signature_name is not UNSET:
            field_dict["signature_name"] = signature_name
        if status is not UNSET:
            field_dict["status"] = status
        if fallback_time is not UNSET:
            field_dict["fallback_time"] = fallback_time
        if content_hash is not UNSET:
            field_dict["content_hash"] = content_hash
        if suppressing_alert_uuid is not UNSET:
            field_dict["suppressing_alert_uuid"] = suppressing_alert_uuid
        if reviewed_status is not UNSET:
            field_dict["reviewed_status"] = reviewed_status
        if reviewed_alert_count is not UNSET:
            field_dict["reviewed_alert_count"] = reviewed_alert_count
        if reviewed_late_only is not UNSET:
            field_dict["reviewed_late_only"] = reviewed_late_only
        if reviewed_content_hash is not UNSET:
            field_dict["reviewed_content_hash"] = reviewed_content_hash

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        run_id = d.pop("run_id")

        signature_uuid = d.pop("signature_uuid")

        alert_count = d.pop("alert_count")

        late_only = d.pop("late_only")

        context_only = d.pop("context_only")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_signature_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature_family = _parse_signature_family(d.pop("signature_family", UNSET))

        def _parse_signature_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature_name = _parse_signature_name(d.pop("signature_name", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        fallback_time = d.pop("fallback_time", UNSET)

        def _parse_content_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_hash = _parse_content_hash(d.pop("content_hash", UNSET))

        def _parse_suppressing_alert_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suppressing_alert_uuid = _parse_suppressing_alert_uuid(
            d.pop("suppressing_alert_uuid", UNSET)
        )

        def _parse_reviewed_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reviewed_status = _parse_reviewed_status(d.pop("reviewed_status", UNSET))

        def _parse_reviewed_alert_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reviewed_alert_count = _parse_reviewed_alert_count(
            d.pop("reviewed_alert_count", UNSET)
        )

        def _parse_reviewed_late_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        reviewed_late_only = _parse_reviewed_late_only(
            d.pop("reviewed_late_only", UNSET)
        )

        def _parse_reviewed_content_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reviewed_content_hash = _parse_reviewed_content_hash(
            d.pop("reviewed_content_hash", UNSET)
        )

        run_result = cls(
            id=id,
            run_id=run_id,
            signature_uuid=signature_uuid,
            alert_count=alert_count,
            late_only=late_only,
            context_only=context_only,
            updated_at=updated_at,
            signature_family=signature_family,
            signature_name=signature_name,
            status=status,
            fallback_time=fallback_time,
            content_hash=content_hash,
            suppressing_alert_uuid=suppressing_alert_uuid,
            reviewed_status=reviewed_status,
            reviewed_alert_count=reviewed_alert_count,
            reviewed_late_only=reviewed_late_only,
            reviewed_content_hash=reviewed_content_hash,
        )

        run_result.additional_properties = d
        return run_result

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
