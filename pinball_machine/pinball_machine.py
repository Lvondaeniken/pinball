import multiprocessing as mp
import queue
from pinball_machine.kicker import Kicker
import serial
from pinball_machine.bumper import Bumper
from pinball_machine.target import Target
from pinball_machine.steppers import Stepperdriver
from pinball_machine.nucleo import Nucleo
import time
class PinballMachine:
    def __init__(self, view):
        self.view_queue = view
        # init nucleo asap because other members need it.
        self.nucleo = Nucleo()
        self.nucleo.startup()
        self._initBumper()
        self._initTarget()
        self._initKicker()
        self.events = {
            'b1' : self.b1.increment_level,
            'b2' : self.b2.increment_level,
            'b3' : self.b3.increment_level,
            't1' : self.t1.update,
            't2' : self.t2.update,
            't3' : self.t3.update,
        }
        #self.steppers = Stepperdriver()

    def _initBumper(self):
        self.b1 = Bumper('bumper1', [10, 22])
        self.b2 = Bumper('bumper2', [23, 34])
        self.b3 = Bumper('bumper3', [35, 46])
        self.b1.reset_level()
        self.b2.reset_level()
        self.b3.reset_level()

    def _initTarget(self):
        self.t1 = Target('target1', [36, 40])
        self.t2 = Target('target2', [50, 60])
        self.t3 = Target('target3', [30, 59])

    def _initKicker(self):
        self.k = Kicker(self.nucleo)
        self.k.enable()

    def check_events(self):
        event = self.nucleo.getEvent()
        if not event is None:
            print(f'received event -> {event}')
            self.nucleo.sendEvent('ack')
            self.resolve_event(event)
    
    def resolve_event(self, event):
        if event in self.events:
            self.events[event]()
        else:
            print("sorry not recognized event")



if __name__ == '__main__':
    q = mp.Queue()
    p = PinballMachine(q)
    while True:
        time.sleep(1)
        p.check_events()