from importlib.metadata import version
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

from nimbus.util.serialize import to_cgminer

from ..util.validate import validate_semantic_version
from .base import NimbusBaseCommandResult


class NimbusVersionResult(BaseModel):
    """
    CGMiner compatible version information.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    firmware: Annotated[str, BeforeValidator(validate_semantic_version)]
    """
    The version of the firmware.
    This value should be denoted as a semantic version, such as `v1.0.0`.
    """
    api: Annotated[str, BeforeValidator(validate_semantic_version)] = Field(
        alias="API", default=f"v{version('nimbus')}", title="API"
    )
    """
    The version of the API, defaults to the nimbus version.
    This value should be denoted as a semantic version, such as `v1.0.0`.
    """
    miner: Annotated[str, BeforeValidator(validate_semantic_version)]
    """
    The version of the mining process, such as CGMiner.
    This value should be denoted as a semantic version, such as `v1.0.0`.
    """
    type: str
    """
    The model name of the device.
    """
    extensions: list[str] = Field(default_factory=list)
    """
    All supported extensions, such as `"tuning.power"`.
    """


class NimbusVersionCommandResult(NimbusBaseCommandResult):
    """
    CGMiner compatible version command result.
    """

    version: list[NimbusVersionResult]
    """
    The result of the version command. CGMiner compatible.
    """
