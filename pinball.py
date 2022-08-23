from game_logic.gamelogic import Game
from pinball_hardware.nucleo import Nucleo
from pinball_hardware.pinball_machine import PinballMachine
# from view.pinball_view import PinballView 
from led_handling.led_manager import LedManager
from multiprocessing import Queue, Process
from time import sleep

class PinballApp:
    def __init__(self):
        # setup view with queue and start in separate process
        view_queue = Queue()
        nucleo = Nucleo()
        led_manager = LedManager()
        pinball_hw = PinballMachine(nucleo, led_manager, view_queue, False)

        # self.gui_proc = Process(target=setup_view, args=(view_queue,))
        self.game = Game(pinball_hw, view_queue)

    def run(self):
        #self.gui_proc.start()
        self.game.start()

# def setup_view(queue):
#     #disable for now because raspi no display
#     p = PinballView(queue)
#     p.run()
#     while True: 
#         pass

if __name__ == '__main__': 
    p = PinballApp()
    p.run()
