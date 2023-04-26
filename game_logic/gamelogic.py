from multiprocessing import Queue
from game_logic.quests.Questbase import Questbase
from game_logic.quests.final import Final
from game_logic.quests.final_menu import FinalMenu
from game_logic.game_quest import MainState
from pinball_hardware.hardware_listener import HardwareListener
from led.led_manager import LedManager

QUESTS: dict[MainState, Questbase] = {
    MainState.FINAL_MENU: FinalMenu,
    MainState.FINAL: Final,
}


class Game:
    def __init__(
        self,
        nucleo: HardwareListener,
        logic_to_gui: Queue,
        gui_to_logic: Queue,
        led: LedManager,
    ):
        self.nucleo = nucleo
        self.logic_to_gui = logic_to_gui
        self.gui_to_logic = gui_to_logic
        self.led = led
        self.state = MainState.FINAL_MENU
        self.active_quest: Questbase = QUESTS[MainState.FINAL_MENU](self.logic_to_gui, self.led)

    def run(self):
        while True:
            event = self.nucleo.get_event()
            if event is None:
                continue
            if event == "exit":
                self.led.terminate()
                return
            self.active_quest.update(event)

            if not self.gui_to_logic.empty():
                event = self.gui_to_logic.get()
                if event is not None:
                    self.active_quest.update(event)

            if self.active_quest.is_done():
                self._get_next_quest()

    def _get_next_quest(self):
        if self.state is MainState.FINAL_MENU:
            self.state = MainState.FINAL
            self.active_quest = QUESTS[MainState.FINAL](self.logic_to_gui, self.led)
