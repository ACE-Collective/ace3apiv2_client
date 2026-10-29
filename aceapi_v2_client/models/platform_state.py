from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlatformState")


@_attrs_define
class PlatformState:
    """How a test does on one platform.

    Attributes:
        platform (str):
        test_state (str): never_run (no run or decision on it), awaiting_review, no_expectations, failing, stale or
            validated
        last_reviewed_run_id (None | str | Unset): its latest reviewed run on the platform
        last_reviewed_at (datetime.datetime | None | Unset):
        expected_signatures (int | Unset): signatures expected of it on the platform that no ignore applies to Default:
            0.
    """

    platform: str
    test_state: str
    last_reviewed_run_id: None | str | Unset = UNSET
    last_reviewed_at: datetime.datetime | None | Unset = UNSET
    expected_signatures: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        test_state = self.test_state

        last_reviewed_run_id: None | str | Unset
        if isinstance(self.last_reviewed_run_id, Unset):
            last_reviewed_run_id = UNSET
        else:
            last_reviewed_run_id = self.last_reviewed_run_id

        last_reviewed_at: None | str | Unset
        if isinstance(self.last_reviewed_at, Unset):
            last_reviewed_at = UNSET
        elif isinstance(self.last_reviewed_at, datetime.datetime):
            last_reviewed_at = self.last_reviewed_at.isoformat()
        else:
            last_reviewed_at = self.last_reviewed_at

        expected_signatures = self.expected_signatures

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "test_state": test_state,
            }
        )
        if last_reviewed_run_id is not UNSET:
            field_dict["last_reviewed_run_id"] = last_reviewed_run_id
        if last_reviewed_at is not UNSET:
            field_dict["last_reviewed_at"] = last_reviewed_at
        if expected_signatures is not UNSET:
            field_dict["expected_signatures"] = expected_signatures

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        platform = d.pop("platform")

        test_state = d.pop("test_state")

        def _parse_last_reviewed_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_reviewed_run_id = _parse_last_reviewed_run_id(
            d.pop("last_reviewed_run_id", UNSET)
        )

        def _parse_last_reviewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_reviewed_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_reviewed_at = _parse_last_reviewed_at(d.pop("last_reviewed_at", UNSET))

        expected_signatures = d.pop("expected_signatures", UNSET)

        platform_state = cls(
            platform=platform,
            test_state=test_state,
            last_reviewed_run_id=last_reviewed_run_id,
            last_reviewed_at=last_reviewed_at,
            expected_signatures=expected_signatures,
        )

        platform_state.additional_properties = d
        return platform_state

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
