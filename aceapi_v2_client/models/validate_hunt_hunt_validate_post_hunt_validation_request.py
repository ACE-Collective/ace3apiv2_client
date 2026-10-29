from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validate_hunt_hunt_validate_post_hunt_validation_request_compiled_hunt import (
        ValidateHuntHuntValidatePostHuntValidationRequestCompiledHunt,
    )
    from ..models.validate_hunt_hunt_validate_post_hunt_validation_request_execution_arguments_type_0 import (
        ValidateHuntHuntValidatePostHuntValidationRequestExecutionArgumentsType0,
    )


T = TypeVar("T", bound="ValidateHuntHuntValidatePostHuntValidationRequest")


@_attrs_define
class ValidateHuntHuntValidatePostHuntValidationRequest:
    """
    Attributes:
        compiled_hunt (ValidateHuntHuntValidatePostHuntValidationRequestCompiledHunt): the hunt package the validate-
            hunt CLI compiles (hunt_compiler.CompiledHunt)
        execution_arguments (None | Unset | ValidateHuntHuntValidatePostHuntValidationRequestExecutionArgumentsType0):
            run the hunt: start_time and end_time (MM/DD/YYYY:HH:MM:SS) for a query hunt, timezone, analyze_results,
            create_alerts, queue, query_results, time_range_overrides, correlate_results
    """

    compiled_hunt: ValidateHuntHuntValidatePostHuntValidationRequestCompiledHunt
    execution_arguments: (
        None
        | Unset
        | ValidateHuntHuntValidatePostHuntValidationRequestExecutionArgumentsType0
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.validate_hunt_hunt_validate_post_hunt_validation_request_execution_arguments_type_0 import (
            ValidateHuntHuntValidatePostHuntValidationRequestExecutionArgumentsType0,
        )

        compiled_hunt = self.compiled_hunt.to_dict()

        execution_arguments: dict[str, Any] | None | Unset
        if isinstance(self.execution_arguments, Unset):
            execution_arguments = UNSET
        elif isinstance(
            self.execution_arguments,
            ValidateHuntHuntValidatePostHuntValidationRequestExecutionArgumentsType0,
        ):
            execution_arguments = self.execution_arguments.to_dict()
        else:
            execution_arguments = self.execution_arguments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "compiled_hunt": compiled_hunt,
            }
        )
        if execution_arguments is not UNSET:
            field_dict["execution_arguments"] = execution_arguments

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.validate_hunt_hunt_validate_post_hunt_validation_request_compiled_hunt import (
            ValidateHuntHuntValidatePostHuntValidationRequestCompiledHunt,
        )
        from ..models.validate_hunt_hunt_validate_post_hunt_validation_request_execution_arguments_type_0 import (
            ValidateHuntHuntValidatePostHuntValidationRequestExecutionArgumentsType0,
        )

        d = dict(src_dict)
        compiled_hunt = (
            ValidateHuntHuntValidatePostHuntValidationRequestCompiledHunt.from_dict(
                d.pop("compiled_hunt")
            )
        )

        def _parse_execution_arguments(
            data: object,
        ) -> (
            None
            | Unset
            | ValidateHuntHuntValidatePostHuntValidationRequestExecutionArgumentsType0
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                execution_arguments_type_0 = ValidateHuntHuntValidatePostHuntValidationRequestExecutionArgumentsType0.from_dict(
                    data
                )

                return execution_arguments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | Unset
                | ValidateHuntHuntValidatePostHuntValidationRequestExecutionArgumentsType0,
                data,
            )

        execution_arguments = _parse_execution_arguments(
            d.pop("execution_arguments", UNSET)
        )

        validate_hunt_hunt_validate_post_hunt_validation_request = cls(
            compiled_hunt=compiled_hunt,
            execution_arguments=execution_arguments,
        )

        validate_hunt_hunt_validate_post_hunt_validation_request.additional_properties = d
        return validate_hunt_hunt_validate_post_hunt_validation_request

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
