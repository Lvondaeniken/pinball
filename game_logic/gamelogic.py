from pinball_machine_pkg.pinball_machine import PinballMachine
from multiprocessing import Queue
from game_logic.game_quests import MainState
from game_logic.Quests.quest1 import Quest1
QUESTS = {MainState.STARTUP: Quest1()}
class Game:
    def __init__(self, view_event_queue: Queue):
        self.machine = PinballMachine(view_event_queue, True) 
        self.active_quest = QUESTS[MainState.STARTUP]

    def start(self):
        self.active_quest.is_done()
if __name__=='__main__':
    #g = Game()
    #g.start()
    pass

