from multiprocessing import Process, Queue
from time import sleep
from led.led_event import LedElements, LedEvent
from led.led_group import LedGroup
from led.color import LedColor

# from led_handling.ws2812 import WS2812
from led.dummy_strip import DummyStrip

TIMEBASE_MS = 20


class LedManager(Process):
    def startup(self, debug: bool = False):
        self.debug = debug
        self.deamon = True
        self.toManager = Queue()
        self.fromManager = Queue()
        self.start()

    def send_event(self, event: LedEvent):
        self.toManager.put(event)

    def run(self):
        self.led_groups = {
            LedElements.BUMPER1: LedGroup(3, TIMEBASE_MS),
            LedElements.BUMPER2: LedGroup(3, TIMEBASE_MS),
            LedElements.BUMPER3: LedGroup(3, TIMEBASE_MS),
            LedElements.TARGET1: LedGroup(3, TIMEBASE_MS),
            LedElements.TARGET2: LedGroup(3, TIMEBASE_MS),
            LedElements.TARGET3: LedGroup(3, TIMEBASE_MS),
        }
        # self.leds = WS2812()
        self.leds = DummyStrip()

        while True:
            sleep(TIMEBASE_MS / 1000)
            self.check_new_events()
            self.update_leds()

    def update_leds(self):
        next_frame: list[LedColor] = []
        for group in self.led_groups.values():
            next_frame.extend(group.get_next_frame())
        for i in range(len(next_frame)):
            self.leds.setPixelColor(i, next_frame[i])
        self.leds.show()

    def check_new_events(self):
        while not self.toManager.empty():
            event: LedEvent = self.toManager.get()
            self.led_groups[event.target].add_event(event)
