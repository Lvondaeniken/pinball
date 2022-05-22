import multiprocessing as mp
import queue
from pinball_machine_pkg.basic_elements.kicker import Kicker
import serial
from pinball_machine_pkg.basic_elements.bumper import Bumper
from pinball_machine_pkg.basic_elements.target import Target
from pinball_machine_pkg.basic_elements.steppers import Stepperdriver
from pinball_machine_pkg.nucleo import Nucleo
from led_manager_pkg.led_manager import LedManager
from led_manager_pkg.led_event import LedElements
import time

class PinballMachine:
    def __init__(self, view, debug: bool=False):
        self.debug = debug
        self.view_queue = view
        # init nucleo asap because other members need it.
        self.led_manager = LedManager()
        self.nucleo = Nucleo()
        self.nucleo.startup(self.debug)
        self.initBumper()
        self.initTarget()
        self.initKicker()
        self.events = {
            'b1' : self.b1.register_hit,
            'b2' : self.b2.register_hit,
            'b3' : self.b3.register_hit,
            't1' : self.t1.update,
            't2' : self.t2.update,
            't3' : self.t3.update,
        }
        TIMEBASE_MS = 10
        self.led_manager.startup(TIMEBASE_MS, self.debug)
        #self.steppers = Stepperdriver()

    def initBumper(self):
        self.b1 = Bumper(LedElements.BUMPER1, self.led_manager)
        self.b2 = Bumper(LedElements.BUMPER2, self.led_manager)
        self.b3 = Bumper(LedElements.BUMPER3, self.led_manager)

    def initTarget(self):
        self.t1 = Target('target1', [36, 40])
        self.t2 = Target('target2', [50, 60])
        self.t3 = Target('target3', [30, 59])

    def initKicker(self):
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

    def get_bumper_states(self):
        return [self.b1.get_hit_count(), self.b2.get_hit_count(), self.b3.get_hit_count()]



if __name__ == '__main__':
    q = mp.Queue()
    p = PinballMachine(q)
    while True:
        time.sleep(1)
        p.check_events()
