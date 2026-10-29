from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remediation_summary import RemediationSummary


T = TypeVar("T", bound="RemediationTargetRead")


@_attrs_define
class RemediationTargetRead:
    """
    Attributes:
        remediator (str): the remediator's configured name
        observable_type (str):
        observable_value (str):
        remediator_display_name (None | str | Unset): null when no remediator by that name is configured on this node
        current (None | RemediationSummary | Unset): the target's latest remediation, which cancel and delete act on
    """

    remediator: str
    observable_type: str
    observable_value: str
    remediator_display_name: None | str | Unset = UNSET
    current: None | RemediationSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.remediation_summary import RemediationSummary

        remediator = self.remediator

        observable_type = self.observable_type

        observable_value = self.observable_value

        remediator_display_name: None | str | Unset
        if isinstance(self.remediator_display_name, Unset):
            remediator_display_name = UNSET
        else:
            remediator_display_name = self.remediator_display_name

        current: dict[str, Any] | None | Unset
        if isinstance(self.current, Unset):
            current = UNSET
        elif isinstance(self.current, RemediationSummary):
            current = self.current.to_dict()
        else:
            current = self.current

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "remediator": remediator,
                "observable_type": observable_type,
                "observable_value": observable_value,
            }
        )
        if remediator_display_name is not UNSET:
            field_dict["remediator_display_name"] = remediator_display_name
        if current is not UNSET:
            field_dict["current"] = current

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.remediation_summary import RemediationSummary

        d = dict(src_dict)
        remediator = d.pop("remediator")

        observable_type = d.pop("observable_type")

        observable_value = d.pop("observable_value")

        def _parse_remediator_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remediator_display_name = _parse_remediator_display_name(
            d.pop("remediator_display_name", UNSET)
        )

        def _parse_current(data: object) -> None | RemediationSummary | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_type_0 = RemediationSummary.from_dict(data)

                return current_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RemediationSummary | Unset, data)

        current = _parse_current(d.pop("current", UNSET))

        remediation_target_read = cls(
            remediator=remediator,
            observable_type=observable_type,
            observable_value=observable_value,
            remediator_display_name=remediator_display_name,
            current=current,
        )

        remediation_target_read.additional_properties = d
        return remediation_target_read

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
