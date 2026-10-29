from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_registration_request_extra import RunRegistrationRequestExtra
    from ..models.run_target_request import RunTargetRequest


T = TypeVar("T", bound="RunRegistrationRequest")


@_attrs_define
class RunRegistrationRequest:
    """
    Attributes:
        test_guid (str): the auto_generated_guid of a test in the Atomic Red Team catalog (/api/v2/svs/tests)
        targets (list[RunTargetRequest]): the test hosts the test runs on
        launcher (str): the name of the launcher registering the run
        batch_id (None | str | Unset): a label shared by runs registered together
        extra (RunRegistrationRequestExtra | Unset): anything else the launcher wants kept with the run; stored and
            shown on the run page, at most svs.runs.max_extra_bytes as JSON
    """

    test_guid: str
    targets: list[RunTargetRequest]
    launcher: str
    batch_id: None | str | Unset = UNSET
    extra: RunRegistrationRequestExtra | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_guid = self.test_guid

        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        launcher = self.launcher

        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

        extra: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra, Unset):
            extra = self.extra.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_guid": test_guid,
                "targets": targets,
                "launcher": launcher,
            }
        )
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if extra is not UNSET:
            field_dict["extra"] = extra

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.run_registration_request_extra import RunRegistrationRequestExtra
        from ..models.run_target_request import RunTargetRequest

        d = dict(src_dict)
        test_guid = d.pop("test_guid")

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = RunTargetRequest.from_dict(targets_item_data)

            targets.append(targets_item)

        launcher = d.pop("launcher")

        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batch_id", UNSET))

        _extra = d.pop("extra", UNSET)
        extra: RunRegistrationRequestExtra | Unset
        if isinstance(_extra, Unset):
            extra = UNSET
        else:
            extra = RunRegistrationRequestExtra.from_dict(_extra)

        run_registration_request = cls(
            test_guid=test_guid,
            targets=targets,
            launcher=launcher,
            batch_id=batch_id,
            extra=extra,
        )

        run_registration_request.additional_properties = d
        return run_registration_request

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
