from game_logic.quests.questbase import Questbase
from events.events import PinballEvent, EventElement
from events.gui_events import GuiEvent, GuiEventType
from led.animations import LedAnimations
from led.elements import LedElements
from led.led_event import LedEvent
from led.led_manager import LedManager
from multiprocessing import Queue
from enum import Enum, auto

COLLECTING = [
    EventElement.BUMPER1,
    EventElement.BUMPER2,
    EventElement.BUMPER3,
    EventElement.TARGET1,
    EventElement.TARGET2,
    EventElement.TARGET3,
]


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
        self._toHit = COLLECTING

    def is_done(self) -> bool:
        return self._done

    def update(self, event: PinballEvent) -> None:
        if self.state == Steps.COLLECTING:
            self.do_collecting(event)

    def do_collecting(self, event: PinballEvent) -> None:
        if event.element in COLLECTING:
            self.gui.put(GuiEvent(GuiEventType.ADD_BOTTLE, None))

        if event.element in self._toHit:
            self.gui.put(GuiEvent(GuiEventType.BONUS, None))
            self._toHit.remove(event.element)
            print(self._toHit)

        if len(self._toHit) == 0:
            self.gui.put(GuiEvent(GuiEventType.ALL_PARTS_HIT, None))


if __name__ == "__main__":
    pass
