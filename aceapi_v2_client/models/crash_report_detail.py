from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crash_report_detail_omitted_item import CrashReportDetailOmittedItem
    from ..models.crash_report_file import CrashReportFile


T = TypeVar("T", bound="CrashReportDetail")


@_attrs_define
class CrashReportDetail:
    """A crash report's full metadata, read from the report directory or from shared storage.

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
        remote (bool | Unset): true if this response was served from shared object storage rather than from this node's
            own disk Default: False.
        complete (bool | Unset): false if the report has no metadata.json, meaning the worker was killed while writing
            its own crash report. The report is still served; what is there is still evidence. Default: True.
        report_dir (None | str | Unset): the report directory, relative to the data dir
        timestamp (None | str | Unset):
        hostname (None | str | Unset):
        pid (int | None | Unset):
        worker_name (None | str | Unset):
        observable_uuid (None | str | Unset):
        maximum_analysis_time (int | None | Unset):
        module_start_time (None | str | Unset):
        elapsed_seconds (float | None | Unset):
        root_storage_dir (None | str | Unset):
        root_description (None | str | Unset):
        file_name (None | str | Unset):
        file_size (int | None | Unset):
        file_sha256 (None | str | Unset):
        omitted (list[CrashReportDetailOmittedItem] | Unset): what this report does not contain and why (size caps,
            missing sources). An empty list means the report is complete.
        files (list[CrashReportFile] | Unset):
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
    remote: bool | Unset = False
    complete: bool | Unset = True
    report_dir: None | str | Unset = UNSET
    timestamp: None | str | Unset = UNSET
    hostname: None | str | Unset = UNSET
    pid: int | None | Unset = UNSET
    worker_name: None | str | Unset = UNSET
    observable_uuid: None | str | Unset = UNSET
    maximum_analysis_time: int | None | Unset = UNSET
    module_start_time: None | str | Unset = UNSET
    elapsed_seconds: float | None | Unset = UNSET
    root_storage_dir: None | str | Unset = UNSET
    root_description: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    file_size: int | None | Unset = UNSET
    file_sha256: None | str | Unset = UNSET
    omitted: list[CrashReportDetailOmittedItem] | Unset = UNSET
    files: list[CrashReportFile] | Unset = UNSET
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

        remote = self.remote

        complete = self.complete

        report_dir: None | str | Unset
        if isinstance(self.report_dir, Unset):
            report_dir = UNSET
        else:
            report_dir = self.report_dir

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = self.timestamp

        hostname: None | str | Unset
        if isinstance(self.hostname, Unset):
            hostname = UNSET
        else:
            hostname = self.hostname

        pid: int | None | Unset
        if isinstance(self.pid, Unset):
            pid = UNSET
        else:
            pid = self.pid

        worker_name: None | str | Unset
        if isinstance(self.worker_name, Unset):
            worker_name = UNSET
        else:
            worker_name = self.worker_name

        observable_uuid: None | str | Unset
        if isinstance(self.observable_uuid, Unset):
            observable_uuid = UNSET
        else:
            observable_uuid = self.observable_uuid

        maximum_analysis_time: int | None | Unset
        if isinstance(self.maximum_analysis_time, Unset):
            maximum_analysis_time = UNSET
        else:
            maximum_analysis_time = self.maximum_analysis_time

        module_start_time: None | str | Unset
        if isinstance(self.module_start_time, Unset):
            module_start_time = UNSET
        else:
            module_start_time = self.module_start_time

        elapsed_seconds: float | None | Unset
        if isinstance(self.elapsed_seconds, Unset):
            elapsed_seconds = UNSET
        else:
            elapsed_seconds = self.elapsed_seconds

        root_storage_dir: None | str | Unset
        if isinstance(self.root_storage_dir, Unset):
            root_storage_dir = UNSET
        else:
            root_storage_dir = self.root_storage_dir

        root_description: None | str | Unset
        if isinstance(self.root_description, Unset):
            root_description = UNSET
        else:
            root_description = self.root_description

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        file_size: int | None | Unset
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        file_sha256: None | str | Unset
        if isinstance(self.file_sha256, Unset):
            file_sha256 = UNSET
        else:
            file_sha256 = self.file_sha256

        omitted: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.omitted, Unset):
            omitted = []
            for omitted_item_data in self.omitted:
                omitted_item = omitted_item_data.to_dict()
                omitted.append(omitted_item)

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

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
        if remote is not UNSET:
            field_dict["remote"] = remote
        if complete is not UNSET:
            field_dict["complete"] = complete
        if report_dir is not UNSET:
            field_dict["report_dir"] = report_dir
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if pid is not UNSET:
            field_dict["pid"] = pid
        if worker_name is not UNSET:
            field_dict["worker_name"] = worker_name
        if observable_uuid is not UNSET:
            field_dict["observable_uuid"] = observable_uuid
        if maximum_analysis_time is not UNSET:
            field_dict["maximum_analysis_time"] = maximum_analysis_time
        if module_start_time is not UNSET:
            field_dict["module_start_time"] = module_start_time
        if elapsed_seconds is not UNSET:
            field_dict["elapsed_seconds"] = elapsed_seconds
        if root_storage_dir is not UNSET:
            field_dict["root_storage_dir"] = root_storage_dir
        if root_description is not UNSET:
            field_dict["root_description"] = root_description
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if file_sha256 is not UNSET:
            field_dict["file_sha256"] = file_sha256
        if omitted is not UNSET:
            field_dict["omitted"] = omitted
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.crash_report_detail_omitted_item import (
            CrashReportDetailOmittedItem,
        )
        from ..models.crash_report_file import CrashReportFile

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

        remote = d.pop("remote", UNSET)

        complete = d.pop("complete", UNSET)

        def _parse_report_dir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        report_dir = _parse_report_dir(d.pop("report_dir", UNSET))

        def _parse_timestamp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        def _parse_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostname = _parse_hostname(d.pop("hostname", UNSET))

        def _parse_pid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pid = _parse_pid(d.pop("pid", UNSET))

        def _parse_worker_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        worker_name = _parse_worker_name(d.pop("worker_name", UNSET))

        def _parse_observable_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        observable_uuid = _parse_observable_uuid(d.pop("observable_uuid", UNSET))

        def _parse_maximum_analysis_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        maximum_analysis_time = _parse_maximum_analysis_time(
            d.pop("maximum_analysis_time", UNSET)
        )

        def _parse_module_start_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        module_start_time = _parse_module_start_time(d.pop("module_start_time", UNSET))

        def _parse_elapsed_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        elapsed_seconds = _parse_elapsed_seconds(d.pop("elapsed_seconds", UNSET))

        def _parse_root_storage_dir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root_storage_dir = _parse_root_storage_dir(d.pop("root_storage_dir", UNSET))

        def _parse_root_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root_description = _parse_root_description(d.pop("root_description", UNSET))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        def _parse_file_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size = _parse_file_size(d.pop("file_size", UNSET))

        def _parse_file_sha256(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_sha256 = _parse_file_sha256(d.pop("file_sha256", UNSET))

        _omitted = d.pop("omitted", UNSET)
        omitted: list[CrashReportDetailOmittedItem] | Unset = UNSET
        if _omitted is not UNSET:
            omitted = []
            for omitted_item_data in _omitted:
                omitted_item = CrashReportDetailOmittedItem.from_dict(omitted_item_data)

                omitted.append(omitted_item)

        _files = d.pop("files", UNSET)
        files: list[CrashReportFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = CrashReportFile.from_dict(files_item_data)

                files.append(files_item)

        crash_report_detail = cls(
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
            remote=remote,
            complete=complete,
            report_dir=report_dir,
            timestamp=timestamp,
            hostname=hostname,
            pid=pid,
            worker_name=worker_name,
            observable_uuid=observable_uuid,
            maximum_analysis_time=maximum_analysis_time,
            module_start_time=module_start_time,
            elapsed_seconds=elapsed_seconds,
            root_storage_dir=root_storage_dir,
            root_description=root_description,
            file_name=file_name,
            file_size=file_size,
            file_sha256=file_sha256,
            omitted=omitted,
            files=files,
        )

        crash_report_detail.additional_properties = d
        return crash_report_detail

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
