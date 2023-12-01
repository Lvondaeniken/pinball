from multiprocessing import Queue
from game_logic.quests.Questbase import Questbase
from events.gui_events import GuiEvent, GuiEventType
from events.events import EventElement, PinballEvent
from led.led_manager import LedManager
from enum import auto, Enum


class Steps(Enum):
    INTRO_1 = auto()
    INTRO_2 = auto()
    INTRO_3 = auto()


class FinalMenu(Questbase):
    def __init__(self, gui: Queue, led: LedManager):
        self.gui = gui
        self.led = led
        self.state = Steps.INTRO_1
        self.gui.put(GuiEvent(GuiEventType.SHOW_FINAL_INFO_1, None))
        self.done = False

    def is_done(self) -> bool:
        return self.done

    def update(self, event: PinballEvent) -> None:
        print(f"current state: {self.state}, incoming event: {event}")
        if self.state == Steps.INTRO_1:
            self.do_intro_1(event)
        elif self.state == Steps.INTRO_2:
            self.do_intro_2(event)
        elif self.state == Steps.INTRO_3:
            self.do_intro_3(event)

    def do_intro_1(self, event: PinballEvent) -> None:
        if event.element == EventElement.BALLSHOOTER:
            self.gui.put(GuiEvent(GuiEventType.SHOW_FINAL_INFO_2, None))
            self.led.send_event()
            self.state = Steps.INTRO_2

    def do_intro_2(self, event: PinballEvent) -> None:
        if event.element == EventElement.BALLSHOOTER:
            self.gui.put(GuiEvent(GuiEventType.SHOW_FINAL_INFO_3, None))
            self.state = Steps.INTRO_3

    def do_intro_3(self, event: PinballEvent) -> None:
        if event.element == EventElement.BALLSHOOTER:
            self.gui.put(GuiEvent(GuiEventType.START_FINAL_MODE, None))
            self.done = True
