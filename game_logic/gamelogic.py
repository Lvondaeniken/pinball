from multiprocessing import Queue
from game_logic.quests.questbase import Questbase
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
    def __init__(self, nucleo: HardwareListener, gui: Queue, led: LedManager):
        self.nucleo = nucleo
        self.gui = gui
        self.led = led
        self.state = MainState.FINAL_MENU
        self.active_quest: Questbase = QUESTS[MainState.FINAL_MENU](self.gui, self.led)

    def start(self):
        while True:
            event = self.nucleo.get_event()
            if event is None:
                continue
            self.active_quest.update(event)
            if self.active_quest.is_done():
                self._get_next_quest()

    def _get_next_quest(self):
        if self.state is MainState.FINAL_MENU:
            self.state = MainState.FINAL
            self.active_quest = QUESTS[MainState.FINAL](self.gui, self.led)
