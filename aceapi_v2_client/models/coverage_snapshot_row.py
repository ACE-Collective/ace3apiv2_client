from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CoverageSnapshotRow")


@_attrs_define
class CoverageSnapshotRow:
    """A coverage row as it was on one day.

    Attributes:
        snapshot_date (datetime.date): the UTC day
        technique (str):
        platform (str):
        attack_release (str):
        is_subtechnique (bool):
        state (str):
        own_state (str):
        tests_total (int):
        tests_validated (int):
        tests_failing (int):
        tests_stale (int):
        manual_signatures (int):
        measured_signatures (int):
        updated_at (datetime.datetime): when the row was written; a second snapshot the same day rewrites it
        parent (None | str | Unset):
    """

    snapshot_date: datetime.date
    technique: str
    platform: str
    attack_release: str
    is_subtechnique: bool
    state: str
    own_state: str
    tests_total: int
    tests_validated: int
    tests_failing: int
    tests_stale: int
    manual_signatures: int
    measured_signatures: int
    updated_at: datetime.datetime
    parent: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_date = self.snapshot_date.isoformat()

        technique = self.technique

        platform = self.platform

        attack_release = self.attack_release

        is_subtechnique = self.is_subtechnique

        state = self.state

        own_state = self.own_state

        tests_total = self.tests_total

        tests_validated = self.tests_validated

        tests_failing = self.tests_failing

        tests_stale = self.tests_stale

        manual_signatures = self.manual_signatures

        measured_signatures = self.measured_signatures

        updated_at = self.updated_at.isoformat()

        parent: None | str | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshot_date": snapshot_date,
                "technique": technique,
                "platform": platform,
                "attack_release": attack_release,
                "is_subtechnique": is_subtechnique,
                "state": state,
                "own_state": own_state,
                "tests_total": tests_total,
                "tests_validated": tests_validated,
                "tests_failing": tests_failing,
                "tests_stale": tests_stale,
                "manual_signatures": manual_signatures,
                "measured_signatures": measured_signatures,
                "updated_at": updated_at,
            }
        )
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        snapshot_date = datetime.date.fromisoformat(d.pop("snapshot_date"))

        technique = d.pop("technique")

        platform = d.pop("platform")

        attack_release = d.pop("attack_release")

        is_subtechnique = d.pop("is_subtechnique")

        state = d.pop("state")

        own_state = d.pop("own_state")

        tests_total = d.pop("tests_total")

        tests_validated = d.pop("tests_validated")

        tests_failing = d.pop("tests_failing")

        tests_stale = d.pop("tests_stale")

        manual_signatures = d.pop("manual_signatures")

        measured_signatures = d.pop("measured_signatures")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_parent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        coverage_snapshot_row = cls(
            snapshot_date=snapshot_date,
            technique=technique,
            platform=platform,
            attack_release=attack_release,
            is_subtechnique=is_subtechnique,
            state=state,
            own_state=own_state,
            tests_total=tests_total,
            tests_validated=tests_validated,
            tests_failing=tests_failing,
            tests_stale=tests_stale,
            manual_signatures=manual_signatures,
            measured_signatures=measured_signatures,
            updated_at=updated_at,
            parent=parent,
        )

        coverage_snapshot_row.additional_properties = d
        return coverage_snapshot_row

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
