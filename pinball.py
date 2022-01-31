from pinball_machine.pinball_machine import PinballMachine
from pinball_machine.pinball_fsm import PinballStatemachine
from pinball_view.pinball_view import PinballView 
from multiprocessing import Queue, Process
from time import sleep

class PinballApp:
    def __init__(self):
        # setup view with queue and start in separate process
        self.view_queue = Queue()
        self.view_process = Process(target=setup_view, args=(self.view_queue,))
        # setup pinballmachine and statemachine
        self.fsm = PinballStatemachine(self.view_queue)

    def run(self):
        while True:
            sleep(0.01)
            event = self.fsm.pinballmachine.check_events()
            if not event == False:
                self.fsm.on_enter_step9()
    
def setup_view(queue):
    p = PinballView(queue)
    p.run()
    while True: 
        pass

if __name__ == '__main__': 
    p = PinballApp()
    p.run