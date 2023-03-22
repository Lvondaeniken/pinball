from game_logic.gamelogic import Game
from pinball_hardware.hardware_listener import HardwareListener

# from pinball_hardware.pinball_machine import PinballMachine
from view.pinball_view import PinballView
from led.led_manager import LedManager
from multiprocessing import Queue, Process


class PinballApp:
    def __init__(self):
        # setup view with queue and start in separate process
        view_queue = Queue()
        self.hw_listener = HardwareListener()
        self.hw_listener.connect()
        led_manager = LedManager()
        led_manager.startup(debug=True)
        self.gui_proc = Process(target=setup_proc, args=(view_queue,))
        self.game = Game(self.hw_listener, view_queue, led_manager)

    def run(self):
        self.gui_proc.start()
        self.game.start()


def setup_proc(queue):
    p = PinballView(queue)
    p.run()
    while True:
        pass


if __name__ == "__main__":
    p = PinballApp()
    p.run()
