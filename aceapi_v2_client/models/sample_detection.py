from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.sample_detection_override_type_0 import SampleDetectionOverrideType0
from ..models.sample_detection_verdict_source_type_0 import (
    SampleDetectionVerdictSourceType0,
)
from ..models.sample_detection_verdict_type_0 import SampleDetectionVerdictType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="SampleDetection")


@_attrs_define
class SampleDetection:
    """A contributing detection: a detection of the rule on the file, on the capture's alert.

    Attributes:
        content_hash (str):
        verdict (None | SampleDetectionVerdictType0 | Unset):
        verdict_source (None | SampleDetectionVerdictSourceType0 | Unset):
        override (None | SampleDetectionOverrideType0 | Unset):
        override_user (None | str | Unset):
        override_set_at (datetime.datetime | None | Unset):
    """

    content_hash: str
    verdict: None | SampleDetectionVerdictType0 | Unset = UNSET
    verdict_source: None | SampleDetectionVerdictSourceType0 | Unset = UNSET
    override: None | SampleDetectionOverrideType0 | Unset = UNSET
    override_user: None | str | Unset = UNSET
    override_set_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_hash = self.content_hash

        verdict: None | str | Unset
        if isinstance(self.verdict, Unset):
            verdict = UNSET
        elif isinstance(self.verdict, SampleDetectionVerdictType0):
            verdict = self.verdict.value
        else:
            verdict = self.verdict

        verdict_source: None | str | Unset
        if isinstance(self.verdict_source, Unset):
            verdict_source = UNSET
        elif isinstance(self.verdict_source, SampleDetectionVerdictSourceType0):
            verdict_source = self.verdict_source.value
        else:
            verdict_source = self.verdict_source

        override: None | str | Unset
        if isinstance(self.override, Unset):
            override = UNSET
        elif isinstance(self.override, SampleDetectionOverrideType0):
            override = self.override.value
        else:
            override = self.override

        override_user: None | str | Unset
        if isinstance(self.override_user, Unset):
            override_user = UNSET
        else:
            override_user = self.override_user

        override_set_at: None | str | Unset
        if isinstance(self.override_set_at, Unset):
            override_set_at = UNSET
        elif isinstance(self.override_set_at, datetime.datetime):
            override_set_at = self.override_set_at.isoformat()
        else:
            override_set_at = self.override_set_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_hash": content_hash,
            }
        )
        if verdict is not UNSET:
            field_dict["verdict"] = verdict
        if verdict_source is not UNSET:
            field_dict["verdict_source"] = verdict_source
        if override is not UNSET:
            field_dict["override"] = override
        if override_user is not UNSET:
            field_dict["override_user"] = override_user
        if override_set_at is not UNSET:
            field_dict["override_set_at"] = override_set_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        content_hash = d.pop("content_hash")

        def _parse_verdict(data: object) -> None | SampleDetectionVerdictType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verdict_type_0 = SampleDetectionVerdictType0(data)

                return verdict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SampleDetectionVerdictType0 | Unset, data)

        verdict = _parse_verdict(d.pop("verdict", UNSET))

        def _parse_verdict_source(
            data: object,
        ) -> None | SampleDetectionVerdictSourceType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verdict_source_type_0 = SampleDetectionVerdictSourceType0(data)

                return verdict_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SampleDetectionVerdictSourceType0 | Unset, data)

        verdict_source = _parse_verdict_source(d.pop("verdict_source", UNSET))

        def _parse_override(
            data: object,
        ) -> None | SampleDetectionOverrideType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                override_type_0 = SampleDetectionOverrideType0(data)

                return override_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SampleDetectionOverrideType0 | Unset, data)

        override = _parse_override(d.pop("override", UNSET))

        def _parse_override_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        override_user = _parse_override_user(d.pop("override_user", UNSET))

        def _parse_override_set_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                override_set_at_type_0 = datetime.datetime.fromisoformat(data)

                return override_set_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        override_set_at = _parse_override_set_at(d.pop("override_set_at", UNSET))

        sample_detection = cls(
            content_hash=content_hash,
            verdict=verdict,
            verdict_source=verdict_source,
            override=override,
            override_user=override_user,
            override_set_at=override_set_at,
        )

        sample_detection.additional_properties = d
        return sample_detection

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
