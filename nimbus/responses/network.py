from pydantic import AliasChoices, BaseModel, ConfigDict, Field

from nimbus.util.serialize import to_cgminer

from .base import NimbusBaseCommandResult


class NimbusNetworkResult(BaseModel):
    """
    Network information.

    Attributes:
        ip: The current IP address of the device.
        gateway: The gateway the device is configured to use.
        subnet_mask: The subnet mask of the network.
            This must be in the form `"WWW.XXX.YYY.ZZZ"`.
            For example, for a `/24` subnet (255 addresses), the mask should be `"255.255.255.0"`.
        dynamic: Whether the device is using DHCP or not.
        mac: The MAC address of the device.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    ip: str = Field(
        serialization_alias="IP",
        validation_alias=AliasChoices("ip", "IP"),
    )
    gateway: str
    subnet_mask: str
    dynamic: bool = True
    mac: str = Field(
        serialization_alias="MAC",
        validation_alias=AliasChoices("mac", "MAC"),
    )


class NimbusNetworkCommandResult(NimbusBaseCommandResult):
    """
    Network command result.

    Attributes:
        network: The result of the network command.
        status: A status result for the command being sent. CGMiner compatible.
    """

    network: list[NimbusNetworkResult]
