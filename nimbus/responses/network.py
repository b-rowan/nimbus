from pydantic import BaseModel, ConfigDict, Field

from nimbus.util.serialize import to_cgminer

from .base import NimbusBaseCommandResult


class NimbusNetworkResult(BaseModel):
    """
    Network information.
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_cgminer)

    ip: str = Field(alias="IP", title="IP")
    """
    The current IP address of the device.
    """
    gateway: str
    """
    The gateway the device is configured to use.
    """
    subnet_mask: str
    """
    The subnet mask of the network.
    This must be in the form `"WWW.XXX.YYY.ZZZ"`.
    For example, for a `/24` subnet (255 addresses), the mask should be `"255.255.255.0"`.
    """
    dynamic: bool = True
    """
    Whether the device is using DHCP or not.
    """
    mac: str = Field(alias="MAC", title="MAC")
    """
    The MAC address of the device.
    """


class NimbusNetworkCommandResult(NimbusBaseCommandResult):
    """
    Network command result.
    """

    network: list[NimbusNetworkResult]
    """
    The result of the network command.
    """
