from pinball_hardware.pinball_machine import PinballMachine
from multiprocessing import Queue
from game_logic.Quests.Questbase import Questbase
from game_logic.Quests.final import Final
from game_logic.game_quest import MainState
from pinball_hardware.nucleo import Nucleo

QUESTS: list[Questbase] = {MainState.FINAL: Final}


class Game:
    def __init__(
        self, nucleo: Nucleo, pinball_machine: PinballMachine, view_event_queue: Queue
    ):
        self.machine = pinball_machine
        self.nucleo = nucleo
        self.view_queue = view_event_queue
        self.nucleo.startup()
        self.active_quest: Questbase = QUESTS[MainState.FINAL]()
        self.active_quest.register(self.machine, view_event_queue)

    def start(self):
        while True:
            event = self.nucleo.getEvent()
            if event == None:
                continue
            self.active_quest.update(event)
            if self.active_quest.is_done():
                print("Final Quest done")
                raise Exception("RIP DONE")


def get_next_quest() -> Questbase:
    return QUESTS[MainState.STARTUP]
