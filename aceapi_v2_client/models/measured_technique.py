from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measured_test import MeasuredTest


T = TypeVar("T", bound="MeasuredTechnique")


@_attrs_define
class MeasuredTechnique:
    """
    Attributes:
        technique (str):
        tests (list[MeasuredTest]): the catalog tests, on each platform, the signature is expected of
        technique_name (None | str | Unset):
    """

    technique: str
    tests: list[MeasuredTest]
    technique_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        technique = self.technique

        tests = []
        for tests_item_data in self.tests:
            tests_item = tests_item_data.to_dict()
            tests.append(tests_item)

        technique_name: None | str | Unset
        if isinstance(self.technique_name, Unset):
            technique_name = UNSET
        else:
            technique_name = self.technique_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "technique": technique,
                "tests": tests,
            }
        )
        if technique_name is not UNSET:
            field_dict["technique_name"] = technique_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.measured_test import MeasuredTest

        d = dict(src_dict)
        technique = d.pop("technique")

        tests = []
        _tests = d.pop("tests")
        for tests_item_data in _tests:
            tests_item = MeasuredTest.from_dict(tests_item_data)

            tests.append(tests_item)

        def _parse_technique_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        technique_name = _parse_technique_name(d.pop("technique_name", UNSET))

        measured_technique = cls(
            technique=technique,
            tests=tests,
            technique_name=technique_name,
        )

        measured_technique.additional_properties = d
        return measured_technique

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
