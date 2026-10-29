from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="CliExecutionSummary")


@_attrs_define
class CliExecutionSummary:
    """
    Attributes:
        id (int):
        user_id (int | None):
        username (str):
        node_id (int):
        node_name (str):
        command (str):
        status (str):
        exit_code (int | None):
        error (None | str):
        timeout_seconds (int):
        created_at (datetime.datetime):
        started_at (datetime.datetime | None):
        finished_at (datetime.datetime | None):
    """

    id: int
    user_id: int | None
    username: str
    node_id: int
    node_name: str
    command: str
    status: str
    exit_code: int | None
    error: None | str
    timeout_seconds: int
    created_at: datetime.datetime
    started_at: datetime.datetime | None
    finished_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id: int | None
        user_id = self.user_id

        username = self.username

        node_id = self.node_id

        node_name = self.node_name

        command = self.command

        status = self.status

        exit_code: int | None
        exit_code = self.exit_code

        error: None | str
        error = self.error

        timeout_seconds = self.timeout_seconds

        created_at = self.created_at.isoformat()

        started_at: None | str
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        finished_at: None | str
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "username": username,
                "node_id": node_id,
                "node_name": node_name,
                "command": command,
                "status": status,
                "exit_code": exit_code,
                "error": error,
                "timeout_seconds": timeout_seconds,
                "created_at": created_at,
                "started_at": started_at,
                "finished_at": finished_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_user_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        user_id = _parse_user_id(d.pop("user_id"))

        username = d.pop("username")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        command = d.pop("command")

        status = d.pop("status")

        def _parse_exit_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        exit_code = _parse_exit_code(d.pop("exit_code"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        timeout_seconds = d.pop("timeout_seconds")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_started_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        started_at = _parse_started_at(d.pop("started_at"))

        def _parse_finished_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        finished_at = _parse_finished_at(d.pop("finished_at"))

        cli_execution_summary = cls(
            id=id,
            user_id=user_id,
            username=username,
            node_id=node_id,
            node_name=node_name,
            command=command,
            status=status,
            exit_code=exit_code,
            error=error,
            timeout_seconds=timeout_seconds,
            created_at=created_at,
            started_at=started_at,
            finished_at=finished_at,
        )

        cli_execution_summary.additional_properties = d
        return cli_execution_summary

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
