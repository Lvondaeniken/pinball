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
        self.bumpers = []
        self._initBumper()
        self.steppers = Stepperdriver()

    def _initBumper(self):
        self.bumpers.append(Bumper('bumper1', [10, 22]))
        self.bumpers.append(Bumper('bumper2', [23, 34]))
        self.bumpers.append(Bumper('bumper3', [35, 46]))

    def _initTarget(self):
        self.target = Target('target1', 3, [36, 40])

    def check_events(self):
        print(self.nucleo.getEvent())

if __name__ == '__main__':
    
    p = PinballMachine()
    while True:
        time.sleep(1)
        p.check_events()