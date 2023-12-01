from game_logic.quests.Questbase import Questbase
from events.events import EventType, PinballEvent, EventElement
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

MAX_BOTTLES = 200


class Steps(Enum):
    COLLECTING = auto()
    TIME_OVER = auto()


class HitList:
    def __init__(self) -> None:
        self.reset()

    def already_hit(self, element: EventElement) -> bool:
        if element in self._list:
            return False
        return True

    def remove(self, element: EventElement):
        self._list.remove(element)

    def empty(self) -> bool:
        if len(self._list) == 0:
            return True
        return False

    def reset(self):
        self._list = COLLECTING.copy()


class Final(Questbase):
    def __init__(self, gui: Queue, led: LedManager):
        self.gui = gui
        self.led = led
        self.state = Steps.COLLECTING
        self.gui.put(GuiEvent(GuiEventType.START_FINAL_MODE, None))
        self._done = False
        self._to_hit = HitList()
        self._bottles = 0

    def is_done(self) -> bool:
        return self._done

    def update(self, event: PinballEvent) -> None:
        if self.state == Steps.COLLECTING:
            self.do_collecting(event)

    def do_collecting(self, event: PinballEvent) -> None:
        print(f"LOGIC -> event {event} received")
        e = event.element
        if e not in COLLECTING:
            return

        if not self._to_hit.already_hit(e):
            self._to_hit.remove(e)
            self.led.send_event(LedEvent(LedAnimations.SWITCH, LedElements.))

        if self._to_hit.empty():
            self._to_hit.reset()
            self._add_bottles(20)
            self.gui.put(GuiEvent(GuiEventType.BONUS_TIME, 5))
        else:
            self._add_bottles(1)

        if self._bottles >= MAX_BOTTLES:
            self.gui.put(GuiEvent(GuiEventType.ALL_BOTTLES_COLLECTED))

        if e != EventElement.GUI:
            return
        if event.type != EventType.TIME_OVER:
            return
        print(f"LOGIC -> received TIMEOVER {self._bottles} collected")
        if self._bottles >= MAX_BOTTLES:
            self.gui.put(GuiEvent(GuiEventType.NOT_ENOUGH_BOTTLES))

    def _add_bottles(self, count: int):
        self._bottles += count
        self.gui.put(GuiEvent(GuiEventType.ADD_BOTTLE, count))


if __name__ == "__main__":
    pass
