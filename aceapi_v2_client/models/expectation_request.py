from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.expectation_request_state import ExpectationRequestState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpectationRequest")


@_attrs_define
class ExpectationRequest:
    """A decision about a signature for a test on a platform, as svs:run_manage makes it.

    Attributes:
        state (ExpectationRequestState): expected: a run of the test should fire it; rejected: it fires, but it is not
            what the test is about, and it is not proposed again
        reason (None | str | Unset):
        run_id (None | str | Unset): the run (of this test, on this platform) whose result the decision was made from;
            its event log records it
    """

    state: ExpectationRequestState
    reason: None | str | Unset = UNSET
    run_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        run_id: None | str | Unset
        if isinstance(self.run_id, Unset):
            run_id = UNSET
        else:
            run_id = self.run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if run_id is not UNSET:
            field_dict["run_id"] = run_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        state = ExpectationRequestState(d.pop("state"))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_id = _parse_run_id(d.pop("run_id", UNSET))

        expectation_request = cls(
            state=state,
            reason=reason,
            run_id=run_id,
        )

        expectation_request.additional_properties = d
        return expectation_request

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
