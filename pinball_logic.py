#!/usr/bin/env python
import time
import serial
from pinball import PinballApp
import multiprocessing

class PinBallLogic():
    def __init__(self):
        print("let me play")
        self.ser = serial.Serial(port='/dev/ttyS0', baudrate=115200)
        


def gui(queue):
    PinballApp(queue).run()

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=gui, args=[queue])
    process.start()