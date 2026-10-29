from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CoverageRow")


@_attrs_define
class CoverageRow:
    """Coverage of one ATT&CK technique on one platform, as of the last refresh.

    Attributes:
        technique (str): the ATT&CK technique id, e.g. T1059 or T1059.001
        platform (str): an ATT&CK platform slug: windows, linux, macos, iaas, ...
        is_subtechnique (bool):
        tactics (list[str]): the technique's tactic ids (TA0002) in the pinned release
        catalog_status (str): active, deprecated, or unknown (not in the pinned release)
        attack_platform (bool): ATT&CK lists the platform for the technique; otherwise only a test brought the row
        state (str): failing, stale, validated, manual, untested or none: the worst of what counts toward the technique
            and its sub-techniques on the platform
        own_state (str): the same, leaving the sub-techniques out
        tests_total (int): tests counted toward state, the sub-techniques' included
        tests_validated (int):
        tests_failing (int):
        tests_stale (int):
        manual_signatures (int): signatures whose mitre: tag counts toward state
        measured_signatures (int): signatures expected of the counted tests on the platform
        state_changed_at (datetime.datetime):
        first_seen_at (datetime.datetime):
        updated_at (datetime.datetime): when the row last changed; the changed_since key
        parent (None | str | Unset): the parent technique of a sub-technique
        technique_name (None | str | Unset):
        last_reviewed_at (datetime.datetime | None | Unset): the latest review of a run that counts
        retired_at (datetime.datetime | None | Unset): when the computation stopped producing the row; it is never
            deleted
    """

    technique: str
    platform: str
    is_subtechnique: bool
    tactics: list[str]
    catalog_status: str
    attack_platform: bool
    state: str
    own_state: str
    tests_total: int
    tests_validated: int
    tests_failing: int
    tests_stale: int
    manual_signatures: int
    measured_signatures: int
    state_changed_at: datetime.datetime
    first_seen_at: datetime.datetime
    updated_at: datetime.datetime
    parent: None | str | Unset = UNSET
    technique_name: None | str | Unset = UNSET
    last_reviewed_at: datetime.datetime | None | Unset = UNSET
    retired_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        technique = self.technique

        platform = self.platform

        is_subtechnique = self.is_subtechnique

        tactics = self.tactics

        catalog_status = self.catalog_status

        attack_platform = self.attack_platform

        state = self.state

        own_state = self.own_state

        tests_total = self.tests_total

        tests_validated = self.tests_validated

        tests_failing = self.tests_failing

        tests_stale = self.tests_stale

        manual_signatures = self.manual_signatures

        measured_signatures = self.measured_signatures

        state_changed_at = self.state_changed_at.isoformat()

        first_seen_at = self.first_seen_at.isoformat()

        updated_at = self.updated_at.isoformat()

        parent: None | str | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        technique_name: None | str | Unset
        if isinstance(self.technique_name, Unset):
            technique_name = UNSET
        else:
            technique_name = self.technique_name

        last_reviewed_at: None | str | Unset
        if isinstance(self.last_reviewed_at, Unset):
            last_reviewed_at = UNSET
        elif isinstance(self.last_reviewed_at, datetime.datetime):
            last_reviewed_at = self.last_reviewed_at.isoformat()
        else:
            last_reviewed_at = self.last_reviewed_at

        retired_at: None | str | Unset
        if isinstance(self.retired_at, Unset):
            retired_at = UNSET
        elif isinstance(self.retired_at, datetime.datetime):
            retired_at = self.retired_at.isoformat()
        else:
            retired_at = self.retired_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "technique": technique,
                "platform": platform,
                "is_subtechnique": is_subtechnique,
                "tactics": tactics,
                "catalog_status": catalog_status,
                "attack_platform": attack_platform,
                "state": state,
                "own_state": own_state,
                "tests_total": tests_total,
                "tests_validated": tests_validated,
                "tests_failing": tests_failing,
                "tests_stale": tests_stale,
                "manual_signatures": manual_signatures,
                "measured_signatures": measured_signatures,
                "state_changed_at": state_changed_at,
                "first_seen_at": first_seen_at,
                "updated_at": updated_at,
            }
        )
        if parent is not UNSET:
            field_dict["parent"] = parent
        if technique_name is not UNSET:
            field_dict["technique_name"] = technique_name
        if last_reviewed_at is not UNSET:
            field_dict["last_reviewed_at"] = last_reviewed_at
        if retired_at is not UNSET:
            field_dict["retired_at"] = retired_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        technique = d.pop("technique")

        platform = d.pop("platform")

        is_subtechnique = d.pop("is_subtechnique")

        tactics = cast(list[str], d.pop("tactics"))

        catalog_status = d.pop("catalog_status")

        attack_platform = d.pop("attack_platform")

        state = d.pop("state")

        own_state = d.pop("own_state")

        tests_total = d.pop("tests_total")

        tests_validated = d.pop("tests_validated")

        tests_failing = d.pop("tests_failing")

        tests_stale = d.pop("tests_stale")

        manual_signatures = d.pop("manual_signatures")

        measured_signatures = d.pop("measured_signatures")

        state_changed_at = datetime.datetime.fromisoformat(d.pop("state_changed_at"))

        first_seen_at = datetime.datetime.fromisoformat(d.pop("first_seen_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_parent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        def _parse_technique_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        technique_name = _parse_technique_name(d.pop("technique_name", UNSET))

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

        def _parse_retired_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retired_at_type_0 = datetime.datetime.fromisoformat(data)

                return retired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        retired_at = _parse_retired_at(d.pop("retired_at", UNSET))

        coverage_row = cls(
            technique=technique,
            platform=platform,
            is_subtechnique=is_subtechnique,
            tactics=tactics,
            catalog_status=catalog_status,
            attack_platform=attack_platform,
            state=state,
            own_state=own_state,
            tests_total=tests_total,
            tests_validated=tests_validated,
            tests_failing=tests_failing,
            tests_stale=tests_stale,
            manual_signatures=manual_signatures,
            measured_signatures=measured_signatures,
            state_changed_at=state_changed_at,
            first_seen_at=first_seen_at,
            updated_at=updated_at,
            parent=parent,
            technique_name=technique_name,
            last_reviewed_at=last_reviewed_at,
            retired_at=retired_at,
        )

        coverage_row.additional_properties = d
        return coverage_row

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
