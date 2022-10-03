from dataclasses import dataclass
from enum import Enum, auto

class GuiEventType(Enum):
    LEFT = auto()
    RIGHT = auto()
    RESET = auto()
    PLAY = auto()
    ADD_TO_HIGHSCORE = auto()



@dataclass
class GuiEvent:
    event : GuiEventType

    