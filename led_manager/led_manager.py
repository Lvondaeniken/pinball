from multiprocessing import Process, Queue
from typing import List
import time

class LedEvent():
    ON=1
    OFF=2
    PATTERN=3
    
    def __init__(self, leds, color_rgb, pattern, timebase_ms):
        self.leds = leds
        self.color = color_rgb
        self.pattern = pattern
        self.timebase_ms = timebase_ms

class LedManager(Process):
    def startup(self):
        self.toManager = Queue()
        self.fromManager = Queue()
        self.start()

    def turn_on(self, leds, color_rgb):
        self._sendEvent(LedEvent(leds, color_rgb, LedEvent.ON))

    def _sendEvent(self, event: LedEvent):
       self.toManager.put(event.color)

    def _getEvent(self):
        if not self.fromManager.empty():
            return self.toManager.get()
        else:
            return None

    def run(self):
        active_led_events = []
        next_led_states = []
        while True:
            time.sleep(timebase_ms)
            if not self.toManager.empty():
                print(self.toManager.get())


if __name__=='__main__':
    l = LedManager()
    l.startup()

    l.turn_on([5, 10], [10, 255, 255])
