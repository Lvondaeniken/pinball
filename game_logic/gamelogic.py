from multiprocessing import Queue
from game_logic.Quests.Questbase import Questbase
from game_logic.Quests.final import Final
from game_logic.Quests.final_menu import FinalMenu
from game_logic.game_quest import MainState
from pinball_hardware.nucleo import Nucleo

QUESTS: dict[MainState, Questbase] = {
    MainState.FINAL_MENU: FinalMenu(),
    MainState.FINAL: Final(),
}


class Game:
    def __init__(self, nucleo: Nucleo, gui: Queue):
        self.nucleo = nucleo
        self.gui = gui
        self.nucleo.startup()
        self.state = MainState.FINAL_MENU
        self.active_quest: Questbase = QUESTS[MainState.FINAL_MENU]
        self.active_quest.register(self.gui)

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
            self.active_quest = QUESTS[MainState.FINAL]
            self.active_quest.register(self.gui)
