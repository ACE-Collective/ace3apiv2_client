from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileCollectionRow")


@_attrs_define
class FileCollectionRow:
    """One file collection request in the listing (file_collection:read). Timestamps are UTC.

    Attributes:
        id (int):
        collector (str): the file collector's configured name
        observable_type (str):
        observable_value (str):
        status (str): NEW, IN_PROGRESS (waiting to be tried again) or COMPLETED
        retry_count (int): the attempts so far
        max_retries (int):
        insert_date (datetime.datetime):
        result (None | str | Unset): how the latest attempt ended (SUCCESS, HOST_OFFLINE, ...)
        result_message (None | str | Unset):
        alert_uuid (None | str | Unset): the alert that asked for the file
        requested_by (None | str | Unset): the display name of the analyst who asked for it
        collected_file_sha256 (None | str | Unset):
        update_time (datetime.datetime | None | Unset):
    """

    id: int
    collector: str
    observable_type: str
    observable_value: str
    status: str
    retry_count: int
    max_retries: int
    insert_date: datetime.datetime
    result: None | str | Unset = UNSET
    result_message: None | str | Unset = UNSET
    alert_uuid: None | str | Unset = UNSET
    requested_by: None | str | Unset = UNSET
    collected_file_sha256: None | str | Unset = UNSET
    update_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        collector = self.collector

        observable_type = self.observable_type

        observable_value = self.observable_value

        status = self.status

        retry_count = self.retry_count

        max_retries = self.max_retries

        insert_date = self.insert_date.isoformat()

        result: None | str | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        else:
            result = self.result

        result_message: None | str | Unset
        if isinstance(self.result_message, Unset):
            result_message = UNSET
        else:
            result_message = self.result_message

        alert_uuid: None | str | Unset
        if isinstance(self.alert_uuid, Unset):
            alert_uuid = UNSET
        else:
            alert_uuid = self.alert_uuid

        requested_by: None | str | Unset
        if isinstance(self.requested_by, Unset):
            requested_by = UNSET
        else:
            requested_by = self.requested_by

        collected_file_sha256: None | str | Unset
        if isinstance(self.collected_file_sha256, Unset):
            collected_file_sha256 = UNSET
        else:
            collected_file_sha256 = self.collected_file_sha256

        update_time: None | str | Unset
        if isinstance(self.update_time, Unset):
            update_time = UNSET
        elif isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "collector": collector,
                "observable_type": observable_type,
                "observable_value": observable_value,
                "status": status,
                "retry_count": retry_count,
                "max_retries": max_retries,
                "insert_date": insert_date,
            }
        )
        if result is not UNSET:
            field_dict["result"] = result
        if result_message is not UNSET:
            field_dict["result_message"] = result_message
        if alert_uuid is not UNSET:
            field_dict["alert_uuid"] = alert_uuid
        if requested_by is not UNSET:
            field_dict["requested_by"] = requested_by
        if collected_file_sha256 is not UNSET:
            field_dict["collected_file_sha256"] = collected_file_sha256
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        collector = d.pop("collector")

        observable_type = d.pop("observable_type")

        observable_value = d.pop("observable_value")

        status = d.pop("status")

        retry_count = d.pop("retry_count")

        max_retries = d.pop("max_retries")

        insert_date = datetime.datetime.fromisoformat(d.pop("insert_date"))

        def _parse_result(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result = _parse_result(d.pop("result", UNSET))

        def _parse_result_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_message = _parse_result_message(d.pop("result_message", UNSET))

        def _parse_alert_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alert_uuid = _parse_alert_uuid(d.pop("alert_uuid", UNSET))

        def _parse_requested_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requested_by = _parse_requested_by(d.pop("requested_by", UNSET))

        def _parse_collected_file_sha256(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collected_file_sha256 = _parse_collected_file_sha256(
            d.pop("collected_file_sha256", UNSET)
        )

        def _parse_update_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_time_type_0 = datetime.datetime.fromisoformat(data)

                return update_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        update_time = _parse_update_time(d.pop("update_time", UNSET))

        file_collection_row = cls(
            id=id,
            collector=collector,
            observable_type=observable_type,
            observable_value=observable_value,
            status=status,
            retry_count=retry_count,
            max_retries=max_retries,
            insert_date=insert_date,
            result=result,
            result_message=result_message,
            alert_uuid=alert_uuid,
            requested_by=requested_by,
            collected_file_sha256=collected_file_sha256,
            update_time=update_time,
        )

        file_collection_row.additional_properties = d
        return file_collection_row

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
