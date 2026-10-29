from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribution import Attribution


T = TypeVar("T", bound="RunAlertDetection")


@_attrs_define
class RunAlertDetection:
    """One detection of an alert the run holds or held, and its attribution to the run.

    Attributes:
        detection (str): the detection's content_hash
        description (None | str | Unset): null when the alert no longer has the detection
        signature_uuid (None | str | Unset):
        signature_family (None | str | Unset):
        attribution (Attribution | None | Unset): its attribution to this run, removed or not; null when it never had
            one
    """

    detection: str
    description: None | str | Unset = UNSET
    signature_uuid: None | str | Unset = UNSET
    signature_family: None | str | Unset = UNSET
    attribution: Attribution | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attribution import Attribution

        detection = self.detection

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        signature_uuid: None | str | Unset
        if isinstance(self.signature_uuid, Unset):
            signature_uuid = UNSET
        else:
            signature_uuid = self.signature_uuid

        signature_family: None | str | Unset
        if isinstance(self.signature_family, Unset):
            signature_family = UNSET
        else:
            signature_family = self.signature_family

        attribution: dict[str, Any] | None | Unset
        if isinstance(self.attribution, Unset):
            attribution = UNSET
        elif isinstance(self.attribution, Attribution):
            attribution = self.attribution.to_dict()
        else:
            attribution = self.attribution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detection": detection,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if signature_uuid is not UNSET:
            field_dict["signature_uuid"] = signature_uuid
        if signature_family is not UNSET:
            field_dict["signature_family"] = signature_family
        if attribution is not UNSET:
            field_dict["attribution"] = attribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attribution import Attribution

        d = dict(src_dict)
        detection = d.pop("detection")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_signature_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature_uuid = _parse_signature_uuid(d.pop("signature_uuid", UNSET))

        def _parse_signature_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature_family = _parse_signature_family(d.pop("signature_family", UNSET))

        def _parse_attribution(data: object) -> Attribution | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attribution_type_0 = Attribution.from_dict(data)

                return attribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Attribution | None | Unset, data)

        attribution = _parse_attribution(d.pop("attribution", UNSET))

        run_alert_detection = cls(
            detection=detection,
            description=description,
            signature_uuid=signature_uuid,
            signature_family=signature_family,
            attribution=attribution,
        )

        run_alert_detection.additional_properties = d
        return run_alert_detection

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
