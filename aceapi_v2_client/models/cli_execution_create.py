from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CliExecutionCreate")


@_attrs_define
class CliExecutionCreate:
    """
    Attributes:
        command (str): the command line after `ace`, e.g. `cas verify --pool yara_qa`; a leading `ace` is ignored
        node_ids (list[int] | None | Unset): the nodes to run it on, once on each; the primary node when omitted
        timeout_seconds (int | Unset): the run is stopped (SIGTERM, then SIGKILL) after this many seconds Default: 300.
    """

    command: str
    node_ids: list[int] | None | Unset = UNSET
    timeout_seconds: int | Unset = 300
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        node_ids: list[int] | None | Unset
        if isinstance(self.node_ids, Unset):
            node_ids = UNSET
        elif isinstance(self.node_ids, list):
            node_ids = self.node_ids

        else:
            node_ids = self.node_ids

        timeout_seconds = self.timeout_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
            }
        )
        if node_ids is not UNSET:
            field_dict["node_ids"] = node_ids
        if timeout_seconds is not UNSET:
            field_dict["timeout_seconds"] = timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        command = d.pop("command")

        def _parse_node_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                node_ids_type_0 = cast(list[int], data)

                return node_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        node_ids = _parse_node_ids(d.pop("node_ids", UNSET))

        timeout_seconds = d.pop("timeout_seconds", UNSET)

        cli_execution_create = cls(
            command=command,
            node_ids=node_ids,
            timeout_seconds=timeout_seconds,
        )

        cli_execution_create.additional_properties = d
        return cli_execution_create

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
