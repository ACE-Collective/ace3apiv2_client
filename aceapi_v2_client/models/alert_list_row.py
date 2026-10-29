from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertListRow")


@_attrs_define
class AlertListRow:
    """One alert as GET /api/v2/alerts lists and exports it: the row plus the analysts' comments.

    Attributes:
        uuid (str):
        insert_date (datetime.datetime):
        updated_at (datetime.datetime): when the row last changed; the changed_since key
        queue (str):
        location (str):
        archived (bool):
        event_time (datetime.datetime | None | Unset):
        disposition_time (datetime.datetime | None | Unset):
        owner_time (datetime.datetime | None | Unset):
        tool (None | str | Unset):
        tool_instance (None | str | Unset):
        alert_type (None | str | Unset):
        description (None | str | Unset):
        priority (int | None | Unset):
        disposition (None | str | Unset):
        disposition_user (None | str | Unset):
        owner (None | str | Unset):
        company (None | str | Unset):
        tags (list[str] | Unset):
        detection_count (int | Unset):  Default: 0.
        svs_status (None | str | Unset): the alert's SVS status: test, test? (attributed by context only), partial or
            mismatch; null for an alert no test run touched (docs/SVS_RUNS.md, *Attribution*)
        svs_runs (list[str] | Unset): the uuids of the SVS test runs the alert is attributed to (GET
            /api/v2/svs/runs/{run_id})
        comments (list[str] | Unset): the comments on the alert, oldest first
    """

    uuid: str
    insert_date: datetime.datetime
    updated_at: datetime.datetime
    queue: str
    location: str
    archived: bool
    event_time: datetime.datetime | None | Unset = UNSET
    disposition_time: datetime.datetime | None | Unset = UNSET
    owner_time: datetime.datetime | None | Unset = UNSET
    tool: None | str | Unset = UNSET
    tool_instance: None | str | Unset = UNSET
    alert_type: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    priority: int | None | Unset = UNSET
    disposition: None | str | Unset = UNSET
    disposition_user: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    company: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    detection_count: int | Unset = 0
    svs_status: None | str | Unset = UNSET
    svs_runs: list[str] | Unset = UNSET
    comments: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        insert_date = self.insert_date.isoformat()

        updated_at = self.updated_at.isoformat()

        queue = self.queue

        location = self.location

        archived = self.archived

        event_time: None | str | Unset
        if isinstance(self.event_time, Unset):
            event_time = UNSET
        elif isinstance(self.event_time, datetime.datetime):
            event_time = self.event_time.isoformat()
        else:
            event_time = self.event_time

        disposition_time: None | str | Unset
        if isinstance(self.disposition_time, Unset):
            disposition_time = UNSET
        elif isinstance(self.disposition_time, datetime.datetime):
            disposition_time = self.disposition_time.isoformat()
        else:
            disposition_time = self.disposition_time

        owner_time: None | str | Unset
        if isinstance(self.owner_time, Unset):
            owner_time = UNSET
        elif isinstance(self.owner_time, datetime.datetime):
            owner_time = self.owner_time.isoformat()
        else:
            owner_time = self.owner_time

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

        alert_type: None | str | Unset
        if isinstance(self.alert_type, Unset):
            alert_type = UNSET
        else:
            alert_type = self.alert_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        disposition: None | str | Unset
        if isinstance(self.disposition, Unset):
            disposition = UNSET
        else:
            disposition = self.disposition

        disposition_user: None | str | Unset
        if isinstance(self.disposition_user, Unset):
            disposition_user = UNSET
        else:
            disposition_user = self.disposition_user

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        detection_count = self.detection_count

        svs_status: None | str | Unset
        if isinstance(self.svs_status, Unset):
            svs_status = UNSET
        else:
            svs_status = self.svs_status

        svs_runs: list[str] | Unset = UNSET
        if not isinstance(self.svs_runs, Unset):
            svs_runs = self.svs_runs

        comments: list[str] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "insert_date": insert_date,
                "updated_at": updated_at,
                "queue": queue,
                "location": location,
                "archived": archived,
            }
        )
        if event_time is not UNSET:
            field_dict["event_time"] = event_time
        if disposition_time is not UNSET:
            field_dict["disposition_time"] = disposition_time
        if owner_time is not UNSET:
            field_dict["owner_time"] = owner_time
        if tool is not UNSET:
            field_dict["tool"] = tool
        if tool_instance is not UNSET:
            field_dict["tool_instance"] = tool_instance
        if alert_type is not UNSET:
            field_dict["alert_type"] = alert_type
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if disposition is not UNSET:
            field_dict["disposition"] = disposition
        if disposition_user is not UNSET:
            field_dict["disposition_user"] = disposition_user
        if owner is not UNSET:
            field_dict["owner"] = owner
        if company is not UNSET:
            field_dict["company"] = company
        if tags is not UNSET:
            field_dict["tags"] = tags
        if detection_count is not UNSET:
            field_dict["detection_count"] = detection_count
        if svs_status is not UNSET:
            field_dict["svs_status"] = svs_status
        if svs_runs is not UNSET:
            field_dict["svs_runs"] = svs_runs
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        uuid = d.pop("uuid")

        insert_date = datetime.datetime.fromisoformat(d.pop("insert_date"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        queue = d.pop("queue")

        location = d.pop("location")

        archived = d.pop("archived")

        def _parse_event_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                event_time_type_0 = datetime.datetime.fromisoformat(data)

                return event_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        event_time = _parse_event_time(d.pop("event_time", UNSET))

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

        def _parse_owner_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_time_type_0 = datetime.datetime.fromisoformat(data)

                return owner_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        owner_time = _parse_owner_time(d.pop("owner_time", UNSET))

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

        def _parse_alert_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alert_type = _parse_alert_type(d.pop("alert_type", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_disposition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disposition = _parse_disposition(d.pop("disposition", UNSET))

        def _parse_disposition_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disposition_user = _parse_disposition_user(d.pop("disposition_user", UNSET))

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        detection_count = d.pop("detection_count", UNSET)

        def _parse_svs_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        svs_status = _parse_svs_status(d.pop("svs_status", UNSET))

        svs_runs = cast(list[str], d.pop("svs_runs", UNSET))

        comments = cast(list[str], d.pop("comments", UNSET))

        alert_list_row = cls(
            uuid=uuid,
            insert_date=insert_date,
            updated_at=updated_at,
            queue=queue,
            location=location,
            archived=archived,
            event_time=event_time,
            disposition_time=disposition_time,
            owner_time=owner_time,
            tool=tool,
            tool_instance=tool_instance,
            alert_type=alert_type,
            description=description,
            priority=priority,
            disposition=disposition,
            disposition_user=disposition_user,
            owner=owner,
            company=company,
            tags=tags,
            detection_count=detection_count,
            svs_status=svs_status,
            svs_runs=svs_runs,
            comments=comments,
        )

        alert_list_row.additional_properties = d
        return alert_list_row

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
