from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coverage_row import CoverageRow
    from ..models.coverage_test import CoverageTest
    from ..models.manual_signature import ManualSignature
    from ..models.measured_signature import MeasuredSignature
    from ..models.removed_test import RemovedTest


T = TypeVar("T", bound="TechniqueCoverage")


@_attrs_define
class TechniqueCoverage:
    """A technique's coverage: its rows as of the last refresh, and what counts toward them now.

    Attributes:
        requested (str): the id asked for
        technique (str): the technique answered for: the requested id, or its successor when revoked
        is_subtechnique (bool):
        catalog_status (str):
        attack_release (str): the pinned ATT&CK release
        rows (list[CoverageRow]): the technique's rows, retired ones included
        sub_technique_rows (list[CoverageRow]): its sub-techniques' rows, retired ones included
        tests (list[CoverageTest]): the tests of the technique and its sub-techniques, per platform
        measured_signatures (list[MeasuredSignature]):
        manual_signatures (list[ManualSignature]):
        removed_tests (list[RemovedTest]): tests removed from their repository; they don't count
        name (None | str | Unset):
        parent (None | str | Unset):
        tactics (list[str] | Unset):
        refreshed_at (datetime.datetime | None | Unset): when the rows were last refreshed; the tests and signatures
            below are read now
        manual_signatures_error (None | str | Unset): why the signature tags couldn't be read; manual_signatures is then
            empty
    """

    requested: str
    technique: str
    is_subtechnique: bool
    catalog_status: str
    attack_release: str
    rows: list[CoverageRow]
    sub_technique_rows: list[CoverageRow]
    tests: list[CoverageTest]
    measured_signatures: list[MeasuredSignature]
    manual_signatures: list[ManualSignature]
    removed_tests: list[RemovedTest]
    name: None | str | Unset = UNSET
    parent: None | str | Unset = UNSET
    tactics: list[str] | Unset = UNSET
    refreshed_at: datetime.datetime | None | Unset = UNSET
    manual_signatures_error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested = self.requested

        technique = self.technique

        is_subtechnique = self.is_subtechnique

        catalog_status = self.catalog_status

        attack_release = self.attack_release

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        sub_technique_rows = []
        for sub_technique_rows_item_data in self.sub_technique_rows:
            sub_technique_rows_item = sub_technique_rows_item_data.to_dict()
            sub_technique_rows.append(sub_technique_rows_item)

        tests = []
        for tests_item_data in self.tests:
            tests_item = tests_item_data.to_dict()
            tests.append(tests_item)

        measured_signatures = []
        for measured_signatures_item_data in self.measured_signatures:
            measured_signatures_item = measured_signatures_item_data.to_dict()
            measured_signatures.append(measured_signatures_item)

        manual_signatures = []
        for manual_signatures_item_data in self.manual_signatures:
            manual_signatures_item = manual_signatures_item_data.to_dict()
            manual_signatures.append(manual_signatures_item)

        removed_tests = []
        for removed_tests_item_data in self.removed_tests:
            removed_tests_item = removed_tests_item_data.to_dict()
            removed_tests.append(removed_tests_item)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parent: None | str | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        tactics: list[str] | Unset = UNSET
        if not isinstance(self.tactics, Unset):
            tactics = self.tactics

        refreshed_at: None | str | Unset
        if isinstance(self.refreshed_at, Unset):
            refreshed_at = UNSET
        elif isinstance(self.refreshed_at, datetime.datetime):
            refreshed_at = self.refreshed_at.isoformat()
        else:
            refreshed_at = self.refreshed_at

        manual_signatures_error: None | str | Unset
        if isinstance(self.manual_signatures_error, Unset):
            manual_signatures_error = UNSET
        else:
            manual_signatures_error = self.manual_signatures_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requested": requested,
                "technique": technique,
                "is_subtechnique": is_subtechnique,
                "catalog_status": catalog_status,
                "attack_release": attack_release,
                "rows": rows,
                "sub_technique_rows": sub_technique_rows,
                "tests": tests,
                "measured_signatures": measured_signatures,
                "manual_signatures": manual_signatures,
                "removed_tests": removed_tests,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if tactics is not UNSET:
            field_dict["tactics"] = tactics
        if refreshed_at is not UNSET:
            field_dict["refreshed_at"] = refreshed_at
        if manual_signatures_error is not UNSET:
            field_dict["manual_signatures_error"] = manual_signatures_error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.coverage_row import CoverageRow
        from ..models.coverage_test import CoverageTest
        from ..models.manual_signature import ManualSignature
        from ..models.measured_signature import MeasuredSignature
        from ..models.removed_test import RemovedTest

        d = dict(src_dict)
        requested = d.pop("requested")

        technique = d.pop("technique")

        is_subtechnique = d.pop("is_subtechnique")

        catalog_status = d.pop("catalog_status")

        attack_release = d.pop("attack_release")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = CoverageRow.from_dict(rows_item_data)

            rows.append(rows_item)

        sub_technique_rows = []
        _sub_technique_rows = d.pop("sub_technique_rows")
        for sub_technique_rows_item_data in _sub_technique_rows:
            sub_technique_rows_item = CoverageRow.from_dict(
                sub_technique_rows_item_data
            )

            sub_technique_rows.append(sub_technique_rows_item)

        tests = []
        _tests = d.pop("tests")
        for tests_item_data in _tests:
            tests_item = CoverageTest.from_dict(tests_item_data)

            tests.append(tests_item)

        measured_signatures = []
        _measured_signatures = d.pop("measured_signatures")
        for measured_signatures_item_data in _measured_signatures:
            measured_signatures_item = MeasuredSignature.from_dict(
                measured_signatures_item_data
            )

            measured_signatures.append(measured_signatures_item)

        manual_signatures = []
        _manual_signatures = d.pop("manual_signatures")
        for manual_signatures_item_data in _manual_signatures:
            manual_signatures_item = ManualSignature.from_dict(
                manual_signatures_item_data
            )

            manual_signatures.append(manual_signatures_item)

        removed_tests = []
        _removed_tests = d.pop("removed_tests")
        for removed_tests_item_data in _removed_tests:
            removed_tests_item = RemovedTest.from_dict(removed_tests_item_data)

            removed_tests.append(removed_tests_item)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_parent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        tactics = cast(list[str], d.pop("tactics", UNSET))

        def _parse_refreshed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                refreshed_at_type_0 = datetime.datetime.fromisoformat(data)

                return refreshed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        refreshed_at = _parse_refreshed_at(d.pop("refreshed_at", UNSET))

        def _parse_manual_signatures_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manual_signatures_error = _parse_manual_signatures_error(
            d.pop("manual_signatures_error", UNSET)
        )

        technique_coverage = cls(
            requested=requested,
            technique=technique,
            is_subtechnique=is_subtechnique,
            catalog_status=catalog_status,
            attack_release=attack_release,
            rows=rows,
            sub_technique_rows=sub_technique_rows,
            tests=tests,
            measured_signatures=measured_signatures,
            manual_signatures=manual_signatures,
            removed_tests=removed_tests,
            name=name,
            parent=parent,
            tactics=tactics,
            refreshed_at=refreshed_at,
            manual_signatures_error=manual_signatures_error,
        )

        technique_coverage.additional_properties = d
        return technique_coverage

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
