from game_logic.Quests.Questbase import Questbase
from events.events import PinballEvent, EventElement
from events.gui_events import GuiEvent, GuiEventType
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
    def register(self, gui: Queue):
        self.gui = gui
        self.state = Steps.COLLECTING
        self.gui.put(GuiEvent(GuiEventType.START_FINAL_MODE, None))
        self._done = False

    def is_done(self) -> bool:
        return self._done

    def update(self, event: PinballEvent) -> None:
        if self.state == Steps.COLLECTING:
            self.do_collecting(event)

    def do_collecting(self, event: PinballEvent) -> None:
        if event.element in COLLECTING:
            self.gui.put(GuiEvent(GuiEventType.ADD_BOTTLE, None))


if __name__ == "__main__":
    pass
