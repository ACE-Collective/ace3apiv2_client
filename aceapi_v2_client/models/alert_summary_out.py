from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertSummaryOut")


@_attrs_define
class AlertSummaryOut:
    """
    Attributes:
        uuid (str):
        description (str):
        alert_type (None | str | Unset):
        tool (None | str | Unset):
        tool_instance (None | str | Unset):
        queue (None | str | Unset):
        disposition (None | str | Unset):
        disposition_time (datetime.datetime | None | Unset):
        insert_date (datetime.datetime | None | Unset):
        owner (None | str | Unset):
        location (None | str | Unset):
        tags (list[str] | Unset):
    """

    uuid: str
    description: str
    alert_type: None | str | Unset = UNSET
    tool: None | str | Unset = UNSET
    tool_instance: None | str | Unset = UNSET
    queue: None | str | Unset = UNSET
    disposition: None | str | Unset = UNSET
    disposition_time: datetime.datetime | None | Unset = UNSET
    insert_date: datetime.datetime | None | Unset = UNSET
    owner: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        description = self.description

        alert_type: None | str | Unset
        if isinstance(self.alert_type, Unset):
            alert_type = UNSET
        else:
            alert_type = self.alert_type

        tool: None | str | Unset
        if isinstance(self.tool, Unset):
            tool = UNSET
        else:
            tool = self.tool

        tool_instance: None | str | Unset
        if isinstance(self.tool_instance, Unset):
            tool_instance = UNSET
        else:
            tool_instance = self.tool_instance

        queue: None | str | Unset
        if isinstance(self.queue, Unset):
            queue = UNSET
        else:
            queue = self.queue

        disposition: None | str | Unset
        if isinstance(self.disposition, Unset):
            disposition = UNSET
        else:
            disposition = self.disposition

        disposition_time: None | str | Unset
        if isinstance(self.disposition_time, Unset):
            disposition_time = UNSET
        elif isinstance(self.disposition_time, datetime.datetime):
            disposition_time = self.disposition_time.isoformat()
        else:
            disposition_time = self.disposition_time

        insert_date: None | str | Unset
        if isinstance(self.insert_date, Unset):
            insert_date = UNSET
        elif isinstance(self.insert_date, datetime.datetime):
            insert_date = self.insert_date.isoformat()
        else:
            insert_date = self.insert_date

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "description": description,
            }
        )
        if alert_type is not UNSET:
            field_dict["alert_type"] = alert_type
        if tool is not UNSET:
            field_dict["tool"] = tool
        if tool_instance is not UNSET:
            field_dict["tool_instance"] = tool_instance
        if queue is not UNSET:
            field_dict["queue"] = queue
        if disposition is not UNSET:
            field_dict["disposition"] = disposition
        if disposition_time is not UNSET:
            field_dict["disposition_time"] = disposition_time
        if insert_date is not UNSET:
            field_dict["insert_date"] = insert_date
        if owner is not UNSET:
            field_dict["owner"] = owner
        if location is not UNSET:
            field_dict["location"] = location
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        uuid = d.pop("uuid")

        description = d.pop("description")

        def _parse_alert_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alert_type = _parse_alert_type(d.pop("alert_type", UNSET))

        def _parse_tool(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool = _parse_tool(d.pop("tool", UNSET))

        def _parse_tool_instance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_instance = _parse_tool_instance(d.pop("tool_instance", UNSET))

        def _parse_queue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queue = _parse_queue(d.pop("queue", UNSET))

        def _parse_disposition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disposition = _parse_disposition(d.pop("disposition", UNSET))

        def _parse_disposition_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disposition_time_type_0 = datetime.datetime.fromisoformat(data)

                return disposition_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        disposition_time = _parse_disposition_time(d.pop("disposition_time", UNSET))

        def _parse_insert_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                insert_date_type_0 = datetime.datetime.fromisoformat(data)

                return insert_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        insert_date = _parse_insert_date(d.pop("insert_date", UNSET))

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        alert_summary_out = cls(
            uuid=uuid,
            description=description,
            alert_type=alert_type,
            tool=tool,
            tool_instance=tool_instance,
            queue=queue,
            disposition=disposition,
            disposition_time=disposition_time,
            insert_date=insert_date,
            owner=owner,
            location=location,
            tags=tags,
        )

        alert_summary_out.additional_properties = d
        return alert_summary_out

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
