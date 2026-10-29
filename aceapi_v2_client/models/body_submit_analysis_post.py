from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodySubmitAnalysisPost")


@_attrs_define
class BodySubmitAnalysisPost:
    """
    Attributes:
        analysis (str): the submission as a JSON object: description (required), analysis_mode, tool, tool_instance,
            type, event_time, event_time_source, details, observables, tags, queue, instructions, extensions, company_id
        file (list[str] | None | Unset): files to add as file observables (repeat for more)
    """

    analysis: str
    file: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analysis = self.analysis

        file: list[str] | None | Unset
        if isinstance(self.file, Unset):
            file = UNSET
        elif isinstance(self.file, list):
            file = self.file

        else:
            file = self.file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analysis": analysis,
            }
        )
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("analysis", (None, str(self.analysis).encode(), "text/plain")))

        if not isinstance(self.file, Unset):
            if isinstance(self.file, list):
                for file_type_0_item_element in self.file:
                    files.append(
                        (
                            "file",
                            (
                                None,
                                str(file_type_0_item_element).encode(),
                                "text/plain",
                            ),
                        )
                    )
            else:
                files.append(("file", (None, str(self.file).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        analysis = d.pop("analysis")

        def _parse_file(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_type_0 = cast(list[str], data)

                return file_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        file = _parse_file(d.pop("file", UNSET))

        body_submit_analysis_post = cls(
            analysis=analysis,
            file=file,
        )

        body_submit_analysis_post.additional_properties = d
        return body_submit_analysis_post

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
