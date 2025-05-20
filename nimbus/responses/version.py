from importlib.metadata import version
from typing import Annotated

from pydantic import AliasChoices, BaseModel, BeforeValidator, ConfigDict, Field

from nimbus.util.serialize import to_cgminer

from .base import NimbusBaseCommandResult


def validate_semantic_version(value: str):
    if not value.startswith("v"):
        raise ValueError("Value should be a semantic version.")
    return value


class NimbusVersionResult(BaseModel):
    """
    CGMiner compatible version information.

    Attributes:
        firmware: The version of the firmware.
            This value should be denoted as a semantic version, such as `v1.0.0`
        api: The version of the API, defaults to the nimbus version.
            This value should be denoted as a semantic version, such as `v1.0.0`
        miner: The version of the mining process, such as CGMiner.
            This value should be denoted as a semantic version, such as `v1.0.0`
        type: The model name of the device.

    Example:
        ```python3
        command_version_result = NimbusVersionResult(
            firmware="v1.0.0",
            miner="v1.0.0",
            type="Antminer S9"
        )

        print(command_version_result.model_dump(by_alias=True))

        # {
        #     "Firmware": "v1.0.0",
        #     "API": "v0.1.0",
        #     "Miner": "v1.0.0",
        #     "Type": "Antminer S9",
        # }
        ```
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    firmware: Annotated[str, BeforeValidator(validate_semantic_version)]
    api: Annotated[str, BeforeValidator(validate_semantic_version)] = Field(
        serialization_alias="API",
        validation_alias=AliasChoices("api", "API"),
        default=f"v{version('nimbus')}",
    )
    miner: Annotated[str, BeforeValidator(validate_semantic_version)]
    type: str


class NimbusVersionCommandResult(NimbusBaseCommandResult):
    """
    CGMiner compatible version command result.

    Attributes:
        version: The result of the version command. CGMiner compatible.
        status: A status result for the command being sent. CGMiner compatible.
    """

    version: list[NimbusVersionResult]
