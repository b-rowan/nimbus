import asyncio
from datetime import datetime

import httpx

from nimbus import __version__
from nimbus.push import NimbusPushData, NimbusPushDataMessage
from nimbus.push.base import NimbusPushMessage
from nimbus.responses import NimbusPushLocation
from nimbus.responses.common import (
    NimbusMinerMessage,
    NimbusMinerMessageSeverity,
)

from ..push.data import NimbusPushHardware, NimbusPushHashboards
from ..push.data.hashrate import NimbusHashrate, NimbusHashrateUnit
from .const import *


def push_handler() -> NimbusPushDataMessage:
    return NimbusPushDataMessage(
        value=NimbusPushData(
            ip="192.168.1.25",
            mac=MAC,
            hardware=NimbusPushHardware(
                make=MAKE,
                model=MODEL,
                chips=CHIPS_PER_BOARD * BOARDS,
                cores=CHIPS_PER_BOARD * CORES_PER_CHIP * BOARDS,
                fans=FANS,
                boards=BOARDS,
                board_chips=[CHIPS_PER_BOARD for _ in range(BOARDS)],
                algo="SHA256",
            ),
            serial_number="NIM123456TEST",
            control_board="NimBoard",
            miner_version=f"v{__version__}",
            firmware_version=f"v{__version__}",
            extensions=["tuning.sethashrate", "tuning.setpower"],
            hashboards=[
                NimbusPushHashboards(
                    id=i,
                    chips=CHIPS_PER_BOARD,
                    cores=CHIPS_PER_BOARD * CORES_PER_CHIP,
                    driver=f"nimbus v{__version__}",
                    model=MINER,
                    working_chips=CHIPS_PER_BOARD,
                    expected_hashrate=4.5,
                    serial_number="NIMBOARDTEST123",
                    voltage=12.5,
                    frequency=400,
                    hashrate_1m=NimbusHashrate(rate=4.5, unit=NimbusHashrateUnit.TH),
                    hashrate_5m=NimbusHashrate(rate=4.5, unit=NimbusHashrateUnit.TH),
                    hashrate_15m=NimbusHashrate(rate=4.5, unit=NimbusHashrateUnit.TH),
                    wattage=350,
                    wattage_limit=350,
                    active=True,
                    pcb_temperature=60,
                    intake_temperature=65,
                    outlet_temperature=85,
                    tuned=True,
                )
                for i in range(BOARDS)
            ],
            wattage=1400,
            wattage_limit=1420,
            fluid_temperature=25,
            fans=[6000, 6000],
            fan_speed=100,
            psu_fans=[],
            psu_fan_speed=100,
            is_mining=True,
            messages=[
                NimbusMinerMessage(
                    when=datetime.now(),
                    message="Testing the message system.",
                    severity=NimbusMinerMessageSeverity.INFO,
                ),
                NimbusMinerMessage(
                    when=datetime.now(),
                    message="The device is getting hot. Fans are ramping to 100%.",
                    severity=NimbusMinerMessageSeverity.WARNING,
                ),
                NimbusMinerMessage(
                    when=datetime.now(),
                    message="The message system has crashed.",
                    severity=NimbusMinerMessageSeverity.ERROR,
                ),
                NimbusMinerMessage(
                    when=datetime.now(),
                    message="The device is currently on fire. Run!",
                    severity=NimbusMinerMessageSeverity.FATAL,
                ),
            ],
        )
    )


class DataPusher:
    def __init__(self, location: NimbusPushLocation):
        self.location = location
        self.task = asyncio.create_task(self._create_task())

    def _create_task(self):
        return self.data_loop()

    async def data_loop(self):
        while True:
            await self.send(push_handler())
            await asyncio.sleep(self.location.frequency)

    async def send(self, data: NimbusPushMessage):
        if data.event not in self.location.events:
            return
        async with httpx.AsyncClient() as c:
            try:
                await c.post(str(self.location.endpoint), json=data.model_dump(by_alias=True))
            except httpx.NetworkError:
                pass

    def done(self):
        return self.task.done()

    def __await__(self):
        return self.task.__await__()

    def cancel(self):
        return self.task.cancel()


class PushHandler:
    def __init__(self):
        self.pushers: dict[str, DataPusher] = {}

    def add_push(self, location: NimbusPushLocation):
        self.pushers[location.name] = DataPusher(location)

    async def remove_push(self, name: str):
        if name not in self.pushers:
            return
        try:
            self.pushers[name].cancel()
            await self.pushers[name]
        except asyncio.CancelledError:
            pass
        finally:
            del self.pushers[name]

    @property
    def pusher_list(self):
        return [p.location for p in self.pushers.values()]


handler = PushHandler()
