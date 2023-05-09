from game_logic.quests.Questbase import Questbase
from events.events import EventType, PinballEvent, EventElement
from events.gui_events import GuiEvent, GuiEventType
from led.animations import LedAnimations
from led.elements import LedElements
from led.led_event import LedEvent
from led.led_manager import LedManager
from multiprocessing import Queue
from enum import Enum, auto
import time

COLLECTING = [
    EventElement.BUMPER1,
    EventElement.BUMPER2,
    EventElement.BUMPER3,
    EventElement.TARGET1,
    EventElement.TARGET2,
    EventElement.TARGET3,
]

MAX_BOTTLES = 200


class Steps(Enum):
    COLLECTING = auto()
    TIME_OVER = auto()


class Final(Questbase):
    def __init__(self, gui: Queue, led: LedManager):
        self.gui = gui
        self.led = led
        self.state = Steps.COLLECTING
        self.gui.put(GuiEvent(GuiEventType.START_FINAL_MODE, None))
        self._done = False
        self._to_hit = COLLECTING.copy()
        self._bottles = 0

    def is_done(self) -> bool:
        return self._done

    def update(self, event: PinballEvent) -> None:
        if self.state == Steps.COLLECTING:
            self.do_collecting(event)

    def do_collecting(self, event: PinballEvent) -> None:
        if event.element not in COLLECTING:
            return

        if event.element in self._to_hit:
            self._to_hit.remove(event.element)

        if len(self._to_hit) == 0:
            self._to_hit = COLLECTING.copy()
            print(self._to_hit)
            self.gui.put(GuiEvent(GuiEventType.ADD_BOTTLE, 20))
            self.gui.put(GuiEvent(GuiEventType.BONUS_TIME, 5))
            self._bottles += 20
        else:
            self.gui.put(GuiEvent(GuiEventType.ADD_BOTTLE, 1))
            self._bottles += 1

        if event.element == EventElement.GUI:
            if event.type == EventType.TIME_OVER:
                if self._bottles >= MAX_BOTTLES:
                    self.gui.put(GuiEvent(GuiEventType.ALL_BOTTLES_COLLECTED))
                else:
                    self.gui.put(GuiEvent(GuiEventType.NOT_ENOUGH_BOTTLES))


if __name__ == "__main__":
    pass
