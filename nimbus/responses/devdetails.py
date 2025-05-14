from importlib.metadata import version
from typing import Annotated

from pydantic import (
    Field,
    AliasChoices,
    BaseModel,
    ConfigDict,
    BeforeValidator,
    computed_field,
)
from pydantic.alias_generators import to_pascal

from .base import NimbusBaseCommandResult


def validate_semantic_version(value: str):
    if not value.startswith("v"):
        raise ValueError("Value should be a semantic version.")
    return value


class NimbusDeviceDetailResult(BaseModel):
    """
    CGMiner compatible device details.

    Attributes:
        id: The board ID, indexed from 0.
            For example, for an S9 with connectors labeled 6/7/8, 6 is 0, 7 is 1, and 8 is 2.
        chips: The number of chips on this board.
        cores: The total number of cores across all chips.
        driver: The driver being used for this board.
            This value should be the same as the name of the mining process, for CGMiner this would be set to `"cgminer"`
        kernel: The name and version number of the kernel being used.
            This value is arbitrary, and will likely not be used by the end user.
        model: The model of the device this board is attached to.
            This value must match the `type` value of the [version command][nimbus.responses.version.NimbusVersionResult].
        devdetails: The same value as ID, just included for CGMiner compatibility.
            Technically this could be different from ID in the original CGMiner code, but modern requirements make using 0 indexed values more useful.

        Example:
            ```python3

            ```
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int = Field(
        serialization_alias="ID",
        validation_alias=AliasChoices("id", "ID"),
    )
    chips: int
    cores: int
    driver: str
    kernel: str | None = None
    model: str

    @computed_field(alias="DEVDETAILS")
    @property
    def devdetails(self) -> int:
        return self.id


class NimbusDeviceDetailsCommandResult(NimbusBaseCommandResult):
    """
    CGMiner compatible devdetails command result.

    Attributes:
        devdetails: The result of the devdetails command, one per board. CGMiner compatible.
        status: A status result for the command being sent. CGMiner compatible.
    """

    devdetails: list[NimbusDeviceDetailResult] = Field(
        serialization_alias="DEVDETAILS",
        validation_alias=AliasChoices("devdetails", "DEVDETAILS"),
    )
