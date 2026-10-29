from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_run_request_confirmed_takes import BulkRunRequestConfirmedTakes


T = TypeVar("T", bound="BulkRunRequest")


@_attrs_define
class BulkRunRequest:
    """A bulk action on runs, as the runs screen sends it.

    Attributes:
        run_ids (list[str]): the runs' uuids
        confirmed_takes (BulkRunRequestConfirmedTakes | Unset): run id -> the username of the person the caller agreed
            to take the run from; a run someone else owns is left alone without it
        reason (None | str | Unset): end and close only: why; required to end a run, and to close an ended run, which
            waits for a review
    """

    run_ids: list[str]
    confirmed_takes: BulkRunRequestConfirmedTakes | Unset = UNSET
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_ids = self.run_ids

        confirmed_takes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.confirmed_takes, Unset):
            confirmed_takes = self.confirmed_takes.to_dict()

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run_ids": run_ids,
            }
        )
        if confirmed_takes is not UNSET:
            field_dict["confirmed_takes"] = confirmed_takes
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_run_request_confirmed_takes import (
            BulkRunRequestConfirmedTakes,
        )

        d = dict(src_dict)
        run_ids = cast(list[str], d.pop("run_ids"))

        _confirmed_takes = d.pop("confirmed_takes", UNSET)
        confirmed_takes: BulkRunRequestConfirmedTakes | Unset
        if isinstance(_confirmed_takes, Unset):
            confirmed_takes = UNSET
        else:
            confirmed_takes = BulkRunRequestConfirmedTakes.from_dict(_confirmed_takes)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        bulk_run_request = cls(
            run_ids=run_ids,
            confirmed_takes=confirmed_takes,
            reason=reason,
        )

        bulk_run_request.additional_properties = d
        return bulk_run_request

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
