from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Ignore")


@_attrs_define
class Ignore:
    """
    Attributes:
        scope (str): global (every test's runs) or test
        signature_uuid (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime): the changed_since key
        test_guid (None | str | Unset): the test, for a test's ignore
        signature_family (None | str | Unset): the signature's family as last known
        signature_name (None | str | Unset): the signature's name as last known
        reason (None | str | Unset):
        created_by (None | str | Unset): who added it (username)
    """

    scope: str
    signature_uuid: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    test_guid: None | str | Unset = UNSET
    signature_family: None | str | Unset = UNSET
    signature_name: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    created_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope = self.scope

        signature_uuid = self.signature_uuid

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        test_guid: None | str | Unset
        if isinstance(self.test_guid, Unset):
            test_guid = UNSET
        else:
            test_guid = self.test_guid

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

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scope": scope,
                "signature_uuid": signature_uuid,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if test_guid is not UNSET:
            field_dict["test_guid"] = test_guid
        if signature_family is not UNSET:
            field_dict["signature_family"] = signature_family
        if signature_name is not UNSET:
            field_dict["signature_name"] = signature_name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        scope = d.pop("scope")

        signature_uuid = d.pop("signature_uuid")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_test_guid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        test_guid = _parse_test_guid(d.pop("test_guid", UNSET))

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

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        ignore = cls(
            scope=scope,
            signature_uuid=signature_uuid,
            created_at=created_at,
            updated_at=updated_at,
            test_guid=test_guid,
            signature_family=signature_family,
            signature_name=signature_name,
            reason=reason,
            created_by=created_by,
        )

        ignore.additional_properties = d
        return ignore

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
