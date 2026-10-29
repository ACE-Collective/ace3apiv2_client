from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.observable_key import ObservableKey


T = TypeVar("T", bound="TargetLookupRequest")


@_attrs_define
class TargetLookupRequest:
    """The alerts, or the observables, to find the remediation targets of: exactly one of the two.

    Attributes:
        alert_uuids (list[str] | Unset): the targets of every observable in these alerts
        observables (list[ObservableKey] | Unset): the targets of these observables
    """

    alert_uuids: list[str] | Unset = UNSET
    observables: list[ObservableKey] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_uuids: list[str] | Unset = UNSET
        if not isinstance(self.alert_uuids, Unset):
            alert_uuids = self.alert_uuids

        observables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.observables, Unset):
            observables = []
            for observables_item_data in self.observables:
                observables_item = observables_item_data.to_dict()
                observables.append(observables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_uuids is not UNSET:
            field_dict["alert_uuids"] = alert_uuids
        if observables is not UNSET:
            field_dict["observables"] = observables

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.observable_key import ObservableKey

        d = dict(src_dict)
        alert_uuids = cast(list[str], d.pop("alert_uuids", UNSET))

        _observables = d.pop("observables", UNSET)
        observables: list[ObservableKey] | Unset = UNSET
        if _observables is not UNSET:
            observables = []
            for observables_item_data in _observables:
                observables_item = ObservableKey.from_dict(observables_item_data)

                observables.append(observables_item)

        target_lookup_request = cls(
            alert_uuids=alert_uuids,
            observables=observables,
        )

        target_lookup_request.additional_properties = d
        return target_lookup_request

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
