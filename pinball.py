# from game_logic.gamelogic import Game
from pinball_view.pinball_view import PinballView 
from multiprocessing import Queue, Process
from time import sleep

class PinballApp:
    def __init__(self):
        # setup view with queue and start in separate process
        self.view_queue = Queue()
        self.view_process = Process(target=setup_view, args=(self.view_queue,))
        # setup pinballmachine and statemachine
        self.game = Game(self.view_queue)

    def run(self):
        self.game.check()

def setup_view(queue):
    #disable for now because raspi no display
    #p = PinballView(queue)
    #p.run()
    while True: 
        pass

if __name__ == '__main__': 
    p = PinballApp()
    p.run()
