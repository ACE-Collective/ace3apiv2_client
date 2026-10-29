from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_platform import TestPlatform


T = TypeVar("T", bound="MeasuredSignature")


@_attrs_define
class MeasuredSignature:
    """A signature expected of the technique's tests: a measured mapping.

    Attributes:
        signature_uuid (str):
        tests (list[TestPlatform]): the (test, platform) pairs that expect it
        name (None | str | Unset):
        family (None | str | Unset):
    """

    signature_uuid: str
    tests: list[TestPlatform]
    name: None | str | Unset = UNSET
    family: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signature_uuid = self.signature_uuid

        tests = []
        for tests_item_data in self.tests:
            tests_item = tests_item_data.to_dict()
            tests.append(tests_item)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        family: None | str | Unset
        if isinstance(self.family, Unset):
            family = UNSET
        else:
            family = self.family

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signature_uuid": signature_uuid,
                "tests": tests,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if family is not UNSET:
            field_dict["family"] = family

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.test_platform import TestPlatform

        d = dict(src_dict)
        signature_uuid = d.pop("signature_uuid")

        tests = []
        _tests = d.pop("tests")
        for tests_item_data in _tests:
            tests_item = TestPlatform.from_dict(tests_item_data)

            tests.append(tests_item)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family = _parse_family(d.pop("family", UNSET))

        measured_signature = cls(
            signature_uuid=signature_uuid,
            tests=tests,
            name=name,
            family=family,
        )

        measured_signature.additional_properties = d
        return measured_signature

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
