from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.history_run import HistoryRun
    from ..models.signature_history import SignatureHistory


T = TypeVar("T", bound="RunHistory")


@_attrs_define
class RunHistory:
    """How the signatures of a run's result did in the test's earlier runs (docs/SVS_API.md, *Run history*).

    Attributes:
        runs (list[HistoryRun]): the test's ended and reviewed runs on this run's platform registered before this one,
            newest first
        signatures (list[SignatureHistory]): one per signature of this run's result, in its order
    """

    runs: list[HistoryRun]
    signatures: list[SignatureHistory]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runs = []
        for runs_item_data in self.runs:
            runs_item = runs_item_data.to_dict()
            runs.append(runs_item)

        signatures = []
        for signatures_item_data in self.signatures:
            signatures_item = signatures_item_data.to_dict()
            signatures.append(signatures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runs": runs,
                "signatures": signatures,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.history_run import HistoryRun
        from ..models.signature_history import SignatureHistory

        d = dict(src_dict)
        runs = []
        _runs = d.pop("runs")
        for runs_item_data in _runs:
            runs_item = HistoryRun.from_dict(runs_item_data)

            runs.append(runs_item)

        signatures = []
        _signatures = d.pop("signatures")
        for signatures_item_data in _signatures:
            signatures_item = SignatureHistory.from_dict(signatures_item_data)

            signatures.append(signatures_item)

        run_history = cls(
            runs=runs,
            signatures=signatures,
        )

        run_history.additional_properties = d
        return run_history

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
