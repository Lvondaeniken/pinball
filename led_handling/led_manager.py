from multiprocessing import Process, Queue
from led_handling.led_event import LedAnimations, LedElements
from time import sleep
#from rpi_ws281x import PixelStrip, Color
from led_handling.dummy_strip import DummyStrip, Color
from led_handling.led_event import LedEvent
from led_handling.led_group import LedGroup
from led_handling.led_color import LedColor
from led_handling.led_switch import LedSwitch
from led_handling.blinking import BlinkingLight
# LED strip configuration:
import sys
import os


class LedManager(Process):
    def startup(self, timebase_ms, debug: bool = False):
        self.debug = debug
        self.led_count = 36  # Number of LED pixels.
        self.led_pin = 18  # GPIO pin connected to the pixels (18 uses PWM!).
        # LED signal frequency in hertz (usually 800khz)
        self.led_freq_hz = 800000
        self.led_dma = 10  # DMA channel to use for generating signal (try 10)
        self.led_brightness = 255  # Set to 0 for darkest and 255 for brightest
        # True to invert the signal (when using NPN transistor level shift)
        self.led_invert = False
        self.led_channel = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        self.timebase_ms = timebase_ms
        self.toManager = Queue()
        self.fromManager = Queue()
        self.start()

    def send_event(self, event: LedEvent):
        self.toManager.put(event)

    def run(self):
        self.led_groups = {
            LedElements.BUMPER1: LedGroup(12),
            LedElements.BUMPER2: LedGroup(12),
            LedElements.BUMPER3: LedGroup(12),
            LedElements.BALLSHOOTER: LedGroup(5),
            LedElements.TARGET1: LedGroup(3),
            LedElements.TARGET2: LedGroup(3),
            LedElements.TARGET3: LedGroup(3)
        }
        if self.debug:
            self.strip = DummyStrip()
        else:
            self.strip = PixelStrip(self.led_count, self.led_pin, self.led_freq_hz,
                                    self.led_dma, self.led_invert, self.led_brightness, self.led_channel)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

        while True:
            sleep(self.timebase_ms/1000)
            self.check_new_events()
            self.update_strip()

    def update_strip(self):
        next_frame = []
        for group in self.led_groups.values():
            next_frame.extend(group.get_next_frame())
        for i in range(len(next_frame)):
            c = Color(next_frame[i].red,
                      next_frame[i].green, next_frame[i].blue)
            self.strip.setPixelColor(i, c)
            self.strip.show()

    def check_new_events(self):
        while not self.toManager.empty():
            event = self.toManager.get()
            if event.animation == LedAnimations.SWITCH:
                self.led_groups[event.target].add_animation(
                    LedSwitch(event.color, 12))
            elif event.animation == LedAnimations.BLINK:
                self.led_groups[event.target].add_animation(BlinkingLight(
                    self.timebase_ms, 10, 1, 12, event.color, event.background))


if __name__ == '__main__':
    sys.path.append(os.getcwd())
    l = LedEvent(LedAnimations.SWITCH, LedElements.BUMPER1,
                 LedColor(1, 1, 1), LedColor(0, 0, 0))
    manager = LedManager()
    manager.startup(50)

    while True:
        c = input()
        if c == '1':
            manager.send_event(LedEvent(LedAnimations.SWITCH, LedElements.BUMPER1, LedColor(
                255, 1, 1), LedColor(0, 0, 0)))
        elif c == '2':
            manager.send_event(LedEvent(
                LedAnimations.SWITCH, LedElements.BUMPER1, LedColor(0, 0, 0), LedColor(0, 0, 0)))
        elif c == '3':
            manager.send_event(LedEvent(LedAnimations.SWITCH, LedElements.BUMPER2, LedColor(
                255, 1, 1), LedColor(0, 0, 0)))
        elif c == '4':
            manager.send_event(LedEvent(
                LedAnimations.SWITCH, LedElements.BUMPER2, LedColor(0, 0, 0), LedColor(0, 0, 0)))
        elif c == '5':
            manager.send_event(LedEvent(LedAnimations.SWITCH, LedElements.BUMPER3, LedColor(
                255, 1, 1), LedColor(0, 0, 0)))
        elif c == '6':
            manager.send_event(LedEvent(
                LedAnimations.SWITCH, LedElements.BUMPER3, LedColor(0, 0, 0), LedColor(0, 0, 0)))
        elif c == '7':
            manager.send_event(LedEvent(LedAnimations.BLINK, LedElements.BUMPER3, LedColor(
                0, 255, 0), LedColor(255, 0, 0)))
