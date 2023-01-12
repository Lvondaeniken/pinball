from game_logic.Quests.Questbase import Questbase
from pinball_hardware.pinball_machine import PinballMachine
from events.events import PinballEvent, EventElement
from events.gui_events import GuiEvent, GuiEventType
from multiprocessing import Queue
from game_logic.Quests.Final.states import Steps

COLLECTING = [
    EventElement.BUMPER1,
    EventElement.BUMPER2,
    EventElement.BUMPER3,
    EventElement.TARGET1,
    EventElement.TARGET2,
    EventElement.TARGET3,
]


class Final(Questbase):
    def register(self, machine: PinballMachine, gui: Queue):
        self.machine = machine
        self.gui = gui
        self.state = Steps.INTRO_1
        self.gui.put(GuiEvent(GuiEventType.SHOW_FINAL_INFO_1, None))

    def is_done(self) -> bool:
        return False

    def update(self, event: PinballEvent) -> None:
        print(f"{event=}")
        if self.state == Steps.INTRO_1:
            self.do_intro_1(event)
        elif self.state == Steps.INTRO_2:
            self.do_intro_2(event)
        elif self.state == Steps.INTRO_3:
            self.do_intro_3(event)
        elif self.state == Steps.COLLECTING:
            self.do_collecting(event)

    def do_intro_1(self, event: PinballEvent) -> None:
        if event.element == EventElement.BALLSHOOTER:
            self.gui.put(GuiEvent(GuiEventType.SHOW_FINAL_INFO_2, None))
            self.state = Steps.INTRO_2

    def do_intro_2(self, event: PinballEvent) -> None:
        if event.element == EventElement.BALLSHOOTER:
            self.gui.put(GuiEvent(GuiEventType.SHOW_FINAL_INFO_3, None))
            self.state = Steps.INTRO_3

    def do_intro_3(self, event: PinballEvent) -> None:
        if event.element == EventElement.BALLSHOOTER:
            self.gui.put(GuiEvent(GuiEventType.START_FINAL_MODE, None))
            self.state = Steps.COLLECTING

    def do_collecting(self, event: PinballEvent) -> None:
        if event.element in COLLECTING:
            self.gui.put(GuiEvent(GuiEventType.ADD_BOTTLE, None))


if __name__ == "__main__":
    pass
