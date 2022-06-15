from pinball_hardware.pinball_machine import PinballMachine
from multiprocessing import Queue
from game_logic.Quests.Questbase import Questbase
from game_quest import MainState
from game_logic.Quests.quest1 import Quest1
QUESTS = {MainState.STARTUP: Quest1}
        
class Game:
    def __init__(self, pinball_machine: PinballMachine, view_event_queue: Queue):
        self.machine =  pinball_machine
        self.active_quest = QUESTS[MainState.STARTUP]

    def start(self):
        while True:
            self.machine.update()
            self.check_active_quest_progress() 

    def check_active_quest_progress(self):
        if self.active_quest.is_done():
            self.active_quest = get_next_quest()
        
def get_next_quest() -> Questbase:
    return QUESTS[MainState.STARTUP]
