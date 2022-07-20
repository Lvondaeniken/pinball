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
    KICKER = auto()

class EventType(Enum):
    HIT = auto()
    ENABLE = auto()
    DISABLE = auto()

@dataclass
class PinballEvent:
    element: EventElement
    type: EventType 

if __name__=='__main__':
    event = PinballEvent(EventElement.BUMPER2, EventType.HIT)
