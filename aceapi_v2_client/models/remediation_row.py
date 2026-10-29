from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemediationRow")


@_attrs_define
class RemediationRow:
    """One remediation in the listing (remediation:read). Timestamps are UTC.

    Attributes:
        id (int):
        remediator (str): the remediator's configured name
        observable_type (str):
        observable_value (str):
        action (str): remove or restore
        status (str): NEW, IN_PROGRESS or COMPLETED
        insert_date (datetime.datetime):
        result (None | str | Unset): how the latest attempt ended (SUCCESS, DELAYED, ...)
        analyst (None | str | Unset): the display name of the analyst who asked for it
        update_time (datetime.datetime | None | Unset):
    """

    id: int
    remediator: str
    observable_type: str
    observable_value: str
    action: str
    status: str
    insert_date: datetime.datetime
    result: None | str | Unset = UNSET
    analyst: None | str | Unset = UNSET
    update_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        remediator = self.remediator

        observable_type = self.observable_type

        observable_value = self.observable_value

        action = self.action

        status = self.status

        insert_date = self.insert_date.isoformat()

        result: None | str | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        else:
            result = self.result

        analyst: None | str | Unset
        if isinstance(self.analyst, Unset):
            analyst = UNSET
        else:
            analyst = self.analyst

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
                "remediator": remediator,
                "observable_type": observable_type,
                "observable_value": observable_value,
                "action": action,
                "status": status,
                "insert_date": insert_date,
            }
        )
        if result is not UNSET:
            field_dict["result"] = result
        if analyst is not UNSET:
            field_dict["analyst"] = analyst
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        remediator = d.pop("remediator")

        observable_type = d.pop("observable_type")

        observable_value = d.pop("observable_value")

        action = d.pop("action")

        status = d.pop("status")

        insert_date = datetime.datetime.fromisoformat(d.pop("insert_date"))

        def _parse_result(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result = _parse_result(d.pop("result", UNSET))

        def _parse_analyst(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        analyst = _parse_analyst(d.pop("analyst", UNSET))

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

        remediation_row = cls(
            id=id,
            remediator=remediator,
            observable_type=observable_type,
            observable_value=observable_value,
            action=action,
            status=status,
            insert_date=insert_date,
            result=result,
            analyst=analyst,
            update_time=update_time,
        )

        remediation_row.additional_properties = d
        return remediation_row

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
