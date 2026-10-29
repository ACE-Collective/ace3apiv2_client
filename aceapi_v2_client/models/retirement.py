from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Retirement")


@_attrs_define
class Retirement:
    """
    Attributes:
        sha256 (str):
        rule_uuid (str):
        retired (bool): whether it is retired now (false once unretired)
        reason (str):
        retired_at (datetime.datetime):
        updated_at (datetime.datetime):
        retired_by (None | str | Unset):
        unretired_by (None | str | Unset):
        unretired_at (datetime.datetime | None | Unset):
    """

    sha256: str
    rule_uuid: str
    retired: bool
    reason: str
    retired_at: datetime.datetime
    updated_at: datetime.datetime
    retired_by: None | str | Unset = UNSET
    unretired_by: None | str | Unset = UNSET
    unretired_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sha256 = self.sha256

        rule_uuid = self.rule_uuid

        retired = self.retired

        reason = self.reason

        retired_at = self.retired_at.isoformat()

        updated_at = self.updated_at.isoformat()

        retired_by: None | str | Unset
        if isinstance(self.retired_by, Unset):
            retired_by = UNSET
        else:
            retired_by = self.retired_by

        unretired_by: None | str | Unset
        if isinstance(self.unretired_by, Unset):
            unretired_by = UNSET
        else:
            unretired_by = self.unretired_by

        unretired_at: None | str | Unset
        if isinstance(self.unretired_at, Unset):
            unretired_at = UNSET
        elif isinstance(self.unretired_at, datetime.datetime):
            unretired_at = self.unretired_at.isoformat()
        else:
            unretired_at = self.unretired_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha256": sha256,
                "rule_uuid": rule_uuid,
                "retired": retired,
                "reason": reason,
                "retired_at": retired_at,
                "updated_at": updated_at,
            }
        )
        if retired_by is not UNSET:
            field_dict["retired_by"] = retired_by
        if unretired_by is not UNSET:
            field_dict["unretired_by"] = unretired_by
        if unretired_at is not UNSET:
            field_dict["unretired_at"] = unretired_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sha256 = d.pop("sha256")

        rule_uuid = d.pop("rule_uuid")

        retired = d.pop("retired")

        reason = d.pop("reason")

        retired_at = datetime.datetime.fromisoformat(d.pop("retired_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_retired_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retired_by = _parse_retired_by(d.pop("retired_by", UNSET))

        def _parse_unretired_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unretired_by = _parse_unretired_by(d.pop("unretired_by", UNSET))

        def _parse_unretired_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                unretired_at_type_0 = datetime.datetime.fromisoformat(data)

                return unretired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        unretired_at = _parse_unretired_at(d.pop("unretired_at", UNSET))

        retirement = cls(
            sha256=sha256,
            rule_uuid=rule_uuid,
            retired=retired,
            reason=reason,
            retired_at=retired_at,
            updated_at=updated_at,
            retired_by=retired_by,
            unretired_by=unretired_by,
            unretired_at=unretired_at,
        )

        retirement.additional_properties = d
        return retirement

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
