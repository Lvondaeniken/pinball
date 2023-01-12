from enum import Enum, auto
from dataclasses import dataclass


class EventElement(Enum):
    BUMPER1 = auto()
    BUMPER2 = auto()
    BUMPER3 = auto()
    TARGET1 = auto()
    TARGET2 = auto()
    TARGET3 = auto()
    BALLSHOOTER = auto()
    KICKER_LEFT = auto()
    KICKER_RIGHT = auto()
    LIGHT_BAR1 = auto()
    LIGHT_BAR2 = auto()
    LIGHT_BAR3 = auto()
    LIGHT_BAR4 = auto()
    LIGHT_BAR5 = auto()
    LIGHT_BAR6 = auto()
    LIGHT_BAR7 = auto()
    LIGHT_BAR8 = auto()


class EventType(Enum):
    HIT = auto()
    ENABLE = auto()
    DISABLE = auto()


@dataclass
class PinballEvent:
    element: EventElement
    type: EventType

    def __repr__(self) -> str:
        return "Event source: {self.element}"


if __name__ == "__main__":
    event = PinballEvent(EventElement.BUMPER2, EventType.HIT)
