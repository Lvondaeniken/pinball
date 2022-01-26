import multiprocessing as mp
import queue
import serial
from bumper import Bumper
from target import Target
from steppers import Stepperdriver

class PinballMachine:
    def __init__(self, queue):
        self.view_queue = queue
        self.nucleo = mp.Queue()
        self.p = mp.Process(target=nucleo, args=(self.nucleo,))
        self.p.daemon = True
        self.p.start()
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
        if not self.nucleo.empty():
            try:
                return self.nucleo.get_nowait()
            except:
                return False
                
def nucleo(queue: mp.Queue):
    ser = serial.Serial(port='/dev/tty.usbmodem14201', baudrate=115200)    
    while True:
        s = ser.readline()
        queue.put(s)


if __name__ == '__main__':
    q = mp.Queue()
    p = PinballMachine(q)
