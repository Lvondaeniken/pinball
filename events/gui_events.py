from dataclasses import dataclass
from enum import Enum, auto
from events.events import PinballEvent


class GuiEventType(Enum):
    HARDWARE_LOG = auto()
    SHOW_FINAL_INFO_1 = auto()
    SHOW_FINAL_INFO_2 = auto()
    SHOW_FINAL_INFO_3 = auto()
    START_FINAL_MODE = auto()
    ADD_BOTTLE = auto()


@dataclass
class GuiEvent:
    event: GuiEventType
    src: PinballEvent
