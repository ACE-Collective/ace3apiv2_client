from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertDisassociation")


@_attrs_define
class AlertDisassociation:
    """What disassociating the alert from its runs left it with.

    Attributes:
        alert_uuid (str):
        run_ids (list[str]): the runs it was disassociated from
        queue (str):
        moved (bool): the alert moved back to the queue SVS took it from
        reopened (bool): the alert was SIMULATED and is OPEN again
        svs_status (None | str | Unset): test, test?, partial or mismatch; null for none
    """

    alert_uuid: str
    run_ids: list[str]
    queue: str
    moved: bool
    reopened: bool
    svs_status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_uuid = self.alert_uuid

        run_ids = self.run_ids

        queue = self.queue

        moved = self.moved

        reopened = self.reopened

        svs_status: None | str | Unset
        if isinstance(self.svs_status, Unset):
            svs_status = UNSET
        else:
            svs_status = self.svs_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_uuid": alert_uuid,
                "run_ids": run_ids,
                "queue": queue,
                "moved": moved,
                "reopened": reopened,
            }
        )
        if svs_status is not UNSET:
            field_dict["svs_status"] = svs_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alert_uuid = d.pop("alert_uuid")

        run_ids = cast(list[str], d.pop("run_ids"))

        queue = d.pop("queue")

        moved = d.pop("moved")

        reopened = d.pop("reopened")

        def _parse_svs_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        svs_status = _parse_svs_status(d.pop("svs_status", UNSET))

        alert_disassociation = cls(
            alert_uuid=alert_uuid,
            run_ids=run_ids,
            queue=queue,
            moved=moved,
            reopened=reopened,
            svs_status=svs_status,
        )

        alert_disassociation.additional_properties = d
        return alert_disassociation

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
