from pinball_hardware.pinball_machine import PinballMachine
from multiprocessing import Queue
from game_logic.Quests.Questbase import Questbase
from game_logic.game_quest import MainState
from game_logic.Quests.quest1 import Quest1
QUESTS: list[Questbase] = {MainState.STARTUP: Quest1}
        
class Game:
    def __init__(self, pinball_machine: PinballMachine, view_event_queue: Queue):
        self.machine =  pinball_machine
        self.active_quest: Questbase = QUESTS[MainState.STARTUP]()
        self.active_quest.register_pinball_machine(self.machine)

    def start(self):
        while True:
            self.machine.update()
            if not self.check_active_quest_progress():
                return
                

    def check_active_quest_progress(self)-> bool:
        if self.active_quest.is_done():
            return False
        return True
        
def get_next_quest() -> Questbase:
    return QUESTS[MainState.STARTUP]
