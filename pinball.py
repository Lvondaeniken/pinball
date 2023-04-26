from game_logic.gamelogic import Game
from pinball_hardware.hardware_listener import HardwareListener

# from pinball_hardware.pinball_machine import PinballMachine
from view.pinball_view import PinballView
from led.led_manager import LedManager
from multiprocessing import Queue, Process

import subprocess


class PinballApp:
    def __init__(self):
        # setup view with queue and start in separate process
        logic_to_gui = Queue()
        gui_to_logic = Queue()
        self.hw_listener = HardwareListener()
        self.hw_listener.connect()
        led_manager = LedManager()
        led_manager.startup(debug=True)
        self.gui_proc = Process(target=setup_proc, args=(logic_to_gui, gui_to_logic, ))
        self.game = Game(self.hw_listener, logic_to_gui, gui_to_logic, led_manager)

    def run(self):
        self.gui_proc.start()
        self.game.run()
        self.gui_proc.terminate()


def setup_proc(logic_to_gui, gui_to_logic):
    p = PinballView(logic_to_gui, gui_to_logic)
    p.run()


if __name__ == "__main__":
    subprocess.Popen("python pinball_hardware/hardware_mock.py", shell=True)
    p = PinballApp()
    p.run()
