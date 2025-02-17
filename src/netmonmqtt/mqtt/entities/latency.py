from typing import TYPE_CHECKING
from netmonmqtt.mqtt.entity import Entity

if TYPE_CHECKING:
    from netmonmqtt.mqtt.device import MQTTDevice


class LatencyEntity(Entity):
    def __init__(
        self,
        parent: "MQTTDevice",
        name: str,
        unique_id: str,
        expire: int = 60,
        unit_of_measurement: str = "ms",
    ):
        super().__init__(
            parent,
            name,
            unique_id,
            "sensor",
            device_class="duration",
            unit_of_measurement=unit_of_measurement,
            expire=expire,
        )
