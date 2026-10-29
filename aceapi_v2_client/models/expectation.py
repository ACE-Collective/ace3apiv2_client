from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Expectation")


@_attrs_define
class Expectation:
    """
    Attributes:
        test_guid (str):
        platform (str): the platform the decision is about: only the test's runs on it are judged by it
        signature_uuid (str):
        state (str): expected or rejected
        decided_at (datetime.datetime):
        updated_at (datetime.datetime): the changed_since key
        signature_family (None | str | Unset): the signature's family as last known
        signature_name (None | str | Unset): the signature's name as last known
        reason (None | str | Unset):
        decided_from_run_id (None | str | Unset): the uuid of the run the decision was made from
        decided_by (None | str | Unset): who decided (username)
    """

    test_guid: str
    platform: str
    signature_uuid: str
    state: str
    decided_at: datetime.datetime
    updated_at: datetime.datetime
    signature_family: None | str | Unset = UNSET
    signature_name: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    decided_from_run_id: None | str | Unset = UNSET
    decided_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_guid = self.test_guid

        platform = self.platform

        signature_uuid = self.signature_uuid

        state = self.state

        decided_at = self.decided_at.isoformat()

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

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        decided_from_run_id: None | str | Unset
        if isinstance(self.decided_from_run_id, Unset):
            decided_from_run_id = UNSET
        else:
            decided_from_run_id = self.decided_from_run_id

        decided_by: None | str | Unset
        if isinstance(self.decided_by, Unset):
            decided_by = UNSET
        else:
            decided_by = self.decided_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_guid": test_guid,
                "platform": platform,
                "signature_uuid": signature_uuid,
                "state": state,
                "decided_at": decided_at,
                "updated_at": updated_at,
            }
        )
        if signature_family is not UNSET:
            field_dict["signature_family"] = signature_family
        if signature_name is not UNSET:
            field_dict["signature_name"] = signature_name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if decided_from_run_id is not UNSET:
            field_dict["decided_from_run_id"] = decided_from_run_id
        if decided_by is not UNSET:
            field_dict["decided_by"] = decided_by

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        test_guid = d.pop("test_guid")

        platform = d.pop("platform")

        signature_uuid = d.pop("signature_uuid")

        state = d.pop("state")

        decided_at = datetime.datetime.fromisoformat(d.pop("decided_at"))

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

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_decided_from_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decided_from_run_id = _parse_decided_from_run_id(
            d.pop("decided_from_run_id", UNSET)
        )

        def _parse_decided_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decided_by = _parse_decided_by(d.pop("decided_by", UNSET))

        expectation = cls(
            test_guid=test_guid,
            platform=platform,
            signature_uuid=signature_uuid,
            state=state,
            decided_at=decided_at,
            updated_at=updated_at,
            signature_family=signature_family,
            signature_name=signature_name,
            reason=reason,
            decided_from_run_id=decided_from_run_id,
            decided_by=decided_by,
        )

        expectation.additional_properties = d
        return expectation

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
