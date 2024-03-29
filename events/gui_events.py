from dataclasses import dataclass
from enum import Enum, auto
from events.events import PinballEvent
from typing import Optional


class GuiEventType(Enum):
    HARDWARE_LOG = auto()
    SHOW_FINAL_INFO_1 = auto()
    SHOW_FINAL_INFO_2 = auto()
    SHOW_FINAL_INFO_3 = auto()
    START_FINAL_MODE = auto()
    ADD_BOTTLE = auto()
    BONUS_TIME = auto()
    ALL_PARTS_HIT = auto()
    TIME_OVER = auto()
    ALL_BOTTLES_COLLECTED = auto()
    SHOW_RESULT = auto()
    NOT_ENOUGH_BOTTLES = auto()


@dataclass
class GuiEvent:
    event: GuiEventType
    src: Optional[PinballEvent]
