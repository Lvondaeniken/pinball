from typing import Optional
from events.events import EventElement, EventType, PinballEvent

EVENT_STR_PAIRS = {
    "b1": PinballEvent(EventElement.BUMPER1, EventType.HIT),
    "b2": PinballEvent(EventElement.BUMPER2, EventType.HIT),
    "b3": PinballEvent(EventElement.BUMPER3, EventType.HIT),
    "t1": PinballEvent(EventElement.TARGET1, EventType.HIT),
    "t2": PinballEvent(EventElement.TARGET2, EventType.HIT),
    "t3": PinballEvent(EventElement.TARGET3, EventType.HIT),
    "kl": PinballEvent(EventElement.KICKER_LEFT, EventType.ENABLE),
    "kr": PinballEvent(EventElement.KICKER_RIGHT, EventType.ENABLE),
    "bs": PinballEvent(EventElement.BALLSHOOTER, EventType.ENABLE),
}


def get_event_from_string(event: str) -> Optional[PinballEvent]:
    if event in EVENT_STR_PAIRS.keys():
        return EVENT_STR_PAIRS[event]
    return None
