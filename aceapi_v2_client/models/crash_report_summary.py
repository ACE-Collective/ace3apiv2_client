from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrashReportSummary")


@_attrs_define
class CrashReportSummary:
    """One row of the crash report listing, built from the database index.

    Attributes:
        crash_id (str): the opaque id logged as crash_id= when the crash happened
        crash_type (str): exception (the module raised), timeout (it hung past maximum_analysis_time), or killed (the
            worker manager SIGKILLed the worker)
        insert_date (None | str | Unset):
        node (None | str | Unset): the node whose disk holds this report; a report only exists on the node that crashed
        module_path (None | str | Unset):
        module_name (None | str | Unset):
        analysis_mode (None | str | Unset):
        root_uuid (None | str | Unset):
        observable_type (None | str | Unset):
        observable_value (None | str | Unset):
        exception_type (None | str | Unset):
        exception_message (None | str | Unset):
        has_file (bool | Unset): true if the report carries the bytes of the file observable the module crashed on
            Default: False.
        local (bool | Unset): true if this report can be downloaded from this node -- either it is on this node's disk,
            or crash_reporting.replicate is on and a shared copy exists. Note this answers 'can I fetch it', not 'where did
            it come from'; see node for that. Default: True.
    """

    crash_id: str
    crash_type: str
    insert_date: None | str | Unset = UNSET
    node: None | str | Unset = UNSET
    module_path: None | str | Unset = UNSET
    module_name: None | str | Unset = UNSET
    analysis_mode: None | str | Unset = UNSET
    root_uuid: None | str | Unset = UNSET
    observable_type: None | str | Unset = UNSET
    observable_value: None | str | Unset = UNSET
    exception_type: None | str | Unset = UNSET
    exception_message: None | str | Unset = UNSET
    has_file: bool | Unset = False
    local: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crash_id = self.crash_id

        crash_type = self.crash_type

        insert_date: None | str | Unset
        if isinstance(self.insert_date, Unset):
            insert_date = UNSET
        else:
            insert_date = self.insert_date

        node: None | str | Unset
        if isinstance(self.node, Unset):
            node = UNSET
        else:
            node = self.node

        module_path: None | str | Unset
        if isinstance(self.module_path, Unset):
            module_path = UNSET
        else:
            module_path = self.module_path

        module_name: None | str | Unset
        if isinstance(self.module_name, Unset):
            module_name = UNSET
        else:
            module_name = self.module_name

        analysis_mode: None | str | Unset
        if isinstance(self.analysis_mode, Unset):
            analysis_mode = UNSET
        else:
            analysis_mode = self.analysis_mode

        root_uuid: None | str | Unset
        if isinstance(self.root_uuid, Unset):
            root_uuid = UNSET
        else:
            root_uuid = self.root_uuid

        observable_type: None | str | Unset
        if isinstance(self.observable_type, Unset):
            observable_type = UNSET
        else:
            observable_type = self.observable_type

        observable_value: None | str | Unset
        if isinstance(self.observable_value, Unset):
            observable_value = UNSET
        else:
            observable_value = self.observable_value

        exception_type: None | str | Unset
        if isinstance(self.exception_type, Unset):
            exception_type = UNSET
        else:
            exception_type = self.exception_type

        exception_message: None | str | Unset
        if isinstance(self.exception_message, Unset):
            exception_message = UNSET
        else:
            exception_message = self.exception_message

        has_file = self.has_file

        local = self.local

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "crash_id": crash_id,
                "crash_type": crash_type,
            }
        )
        if insert_date is not UNSET:
            field_dict["insert_date"] = insert_date
        if node is not UNSET:
            field_dict["node"] = node
        if module_path is not UNSET:
            field_dict["module_path"] = module_path
        if module_name is not UNSET:
            field_dict["module_name"] = module_name
        if analysis_mode is not UNSET:
            field_dict["analysis_mode"] = analysis_mode
        if root_uuid is not UNSET:
            field_dict["root_uuid"] = root_uuid
        if observable_type is not UNSET:
            field_dict["observable_type"] = observable_type
        if observable_value is not UNSET:
            field_dict["observable_value"] = observable_value
        if exception_type is not UNSET:
            field_dict["exception_type"] = exception_type
        if exception_message is not UNSET:
            field_dict["exception_message"] = exception_message
        if has_file is not UNSET:
            field_dict["has_file"] = has_file
        if local is not UNSET:
            field_dict["local"] = local

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        crash_id = d.pop("crash_id")

        crash_type = d.pop("crash_type")

        def _parse_insert_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        insert_date = _parse_insert_date(d.pop("insert_date", UNSET))

        def _parse_node(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node = _parse_node(d.pop("node", UNSET))

        def _parse_module_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        module_path = _parse_module_path(d.pop("module_path", UNSET))

        def _parse_module_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        module_name = _parse_module_name(d.pop("module_name", UNSET))

        def _parse_analysis_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        analysis_mode = _parse_analysis_mode(d.pop("analysis_mode", UNSET))

        def _parse_root_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root_uuid = _parse_root_uuid(d.pop("root_uuid", UNSET))

        def _parse_observable_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        observable_type = _parse_observable_type(d.pop("observable_type", UNSET))

        def _parse_observable_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        observable_value = _parse_observable_value(d.pop("observable_value", UNSET))

        def _parse_exception_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exception_type = _parse_exception_type(d.pop("exception_type", UNSET))

        def _parse_exception_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exception_message = _parse_exception_message(d.pop("exception_message", UNSET))

        has_file = d.pop("has_file", UNSET)

        local = d.pop("local", UNSET)

        crash_report_summary = cls(
            crash_id=crash_id,
            crash_type=crash_type,
            insert_date=insert_date,
            node=node,
            module_path=module_path,
            module_name=module_name,
            analysis_mode=analysis_mode,
            root_uuid=root_uuid,
            observable_type=observable_type,
            observable_value=observable_value,
            exception_type=exception_type,
            exception_message=exception_message,
            has_file=has_file,
            local=local,
        )

        crash_report_summary.additional_properties = d
        return crash_report_summary

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
