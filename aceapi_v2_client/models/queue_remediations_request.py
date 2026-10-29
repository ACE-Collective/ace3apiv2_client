from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.remediation_action import RemediationAction

if TYPE_CHECKING:
    from ..models.remediation_target_key import RemediationTargetKey


T = TypeVar("T", bound="QueueRemediationsRequest")


@_attrs_define
class QueueRemediationsRequest:
    """Queue one remediation per target. A restore uses the restore key of the target's latest
    successful removal.

        Attributes:
            action (RemediationAction):
            targets (list[RemediationTargetKey]):
    """

    action: RemediationAction
    targets: list[RemediationTargetKey]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "targets": targets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.remediation_target_key import RemediationTargetKey

        d = dict(src_dict)
        action = RemediationAction(d.pop("action"))

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = RemediationTargetKey.from_dict(targets_item_data)

            targets.append(targets_item)

        queue_remediations_request = cls(
            action=action,
            targets=targets,
        )

        queue_remediations_request.additional_properties = d
        return queue_remediations_request

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
