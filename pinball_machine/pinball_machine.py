import multiprocessing as mp
import queue
import serial
from bumper import Bumper
from target import Target
from steppers import Stepperdriver
from nucleo import Nucleo
import time
class PinballMachine:
    def __init__(self):
        self.nucleo = Nucleo()
        self.nucleo.startup()
        self.b1 = Bumper('bumper1', [10, 22])
        self.b2 = Bumper('bumper2', [23, 34])
        self.b3 = Bumper('bumper3', [35, 46])
        self._initBumper()
        self.events = {
            'b1' : self.b1.increment_level,
            'b2' : self.b2.increment_level,
            'b3' : self.b3.increment_level,
        }
        #self.steppers = Stepperdriver()

    def _initBumper(self):
        self.b1.reset_level()
        self.b2.reset_level()
        self.b3.reset_level()

    def _initTarget(self):
        self.target = Target('target1', 3, [36, 40])

    def check_events(self):
        event = self.nucleo.getEvent()
        if not event is None:
            print(f'received event -> {event}')
            self.nucleo.sendEvent('ack')
            self.resolve_event(event)
    
    def resolve_event(self, event):
        if event in self.events:
            self.events[event]()



if __name__ == '__main__':
    
    p = PinballMachine()
    while True:
        time.sleep(1)
        p.check_events()