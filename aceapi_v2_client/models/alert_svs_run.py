from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertSVSRun")


@_attrs_define
class AlertSVSRun:
    """
    Attributes:
        run_id (str): the run's uuid
        state (str):
        test_guid (str):
        test_name (None | str | Unset): null when the catalog no longer has the test
    """

    run_id: str
    state: str
    test_guid: str
    test_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        state = self.state

        test_guid = self.test_guid

        test_name: None | str | Unset
        if isinstance(self.test_name, Unset):
            test_name = UNSET
        else:
            test_name = self.test_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run_id": run_id,
                "state": state,
                "test_guid": test_guid,
            }
        )
        if test_name is not UNSET:
            field_dict["test_name"] = test_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        run_id = d.pop("run_id")

        state = d.pop("state")

        test_guid = d.pop("test_guid")

        def _parse_test_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        test_name = _parse_test_name(d.pop("test_name", UNSET))

        alert_svs_run = cls(
            run_id=run_id,
            state=state,
            test_guid=test_guid,
            test_name=test_name,
        )

        alert_svs_run.additional_properties = d
        return alert_svs_run

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
