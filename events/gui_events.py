from dataclasses import dataclass
from enum import Enum, auto
from events.events import PinballEvent

class GuiEventType(Enum):
    LEFT = auto()
    RIGHT = auto()
    RESET = auto()
    PLAY = auto()
    ADD_TO_HIGHSCORE = auto()
    POINTS = auto()
    HARDWARE_LOG = auto()




@dataclass
class GuiEvent:
    event : GuiEventType
    src: PinballEvent  
