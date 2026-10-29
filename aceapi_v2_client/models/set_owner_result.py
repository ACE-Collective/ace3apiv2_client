from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.set_owner_result_skipped import SetOwnerResultSkipped


T = TypeVar("T", bound="SetOwnerResult")


@_attrs_define
class SetOwnerResult:
    """
    Attributes:
        applied (list[str]): the alerts that now have the requested owner, in the order asked for
        skipped (SetOwnerResultSkipped): alert uuid -> display name of the analyst left owning it
        message (None | str | Unset): what the GUI tells the analyst when alerts were skipped; null otherwise
    """

    applied: list[str]
    skipped: SetOwnerResultSkipped
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied = self.applied

        skipped = self.skipped.to_dict()

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied": applied,
                "skipped": skipped,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.set_owner_result_skipped import SetOwnerResultSkipped

        d = dict(src_dict)
        applied = cast(list[str], d.pop("applied"))

        skipped = SetOwnerResultSkipped.from_dict(d.pop("skipped"))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        set_owner_result = cls(
            applied=applied,
            skipped=skipped,
            message=message,
        )

        set_owner_result.additional_properties = d
        return set_owner_result

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
