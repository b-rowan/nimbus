from importlib.metadata import version
from typing import Annotated

from pydantic import AliasChoices, BaseModel, BeforeValidator, ConfigDict, Field
from pydantic.alias_generators import to_pascal

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
        compile_time: The compile time of the firmware version in use.
            This value should be in the datetime format `%a %b %d %H:%M:%S %Z %Y`, such as `Tue May 13 14:56:45 CST 2025`
        type: The model name of the device.

    Example:
        ```python3
        command_version_result = NimbusVersionResult(
            firmware="v1.0.0",
            miner="v1.0.0",
            compile_time="Tue May 13 14:56:45 CST 2025",
            type="Antminer S9"
        )

        print(command_version_result.model_dump(by_alias=True))

        # {
        #     "Firmware": "v1.0.0",
        #     "API": "v0.1.0",
        #     "Miner": "v1.0.0",
        #     "CompileTime": "Tue May 13 14:56:45 CST 2025",
        #     "Type": "Antminer S9",
        # }
        ```
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    firmware: Annotated[str, BeforeValidator(validate_semantic_version)]
    api: Annotated[str, BeforeValidator(validate_semantic_version)] = Field(
        serialization_alias="API",
        validation_alias=AliasChoices("api", "API"),
        default=f"v{version('nimbus')}",
    )
    miner: Annotated[str, BeforeValidator(validate_semantic_version)]
    compile_time: str
    type: str


class NimbusVersionCommandResult(NimbusBaseCommandResult):
    """
    CGMiner compatible version command result.

    Attributes:
        version: The result of the version command. CGMiner compatible.
        status: A status result for the command being sent. CGMiner compatible.
    """

    version: list[NimbusVersionResult] = Field(
        serialization_alias="VERSION",
        validation_alias=AliasChoices("version", "VERSION"),
    )
