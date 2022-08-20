import multiprocessing as mp
import queue
from pinball_hardware.basic_parts.bumper import Bumper
from pinball_hardware.basic_parts.target import Target
from pinball_hardware.basic_parts.steppers import Stepperdriver
from pinball_hardware.nucleo import Nucleo
from led_handling.led_manager import LedManager
from led_handling.led_event import LedElements
import time
from events.events import EventElement, PinballEvent

TIMEBASE_MS = 10

class PinballMachine:
    def __init__(self, nucleo: Nucleo, led_manager: LedManager, view, debug: bool=False):
        self.nucleo = nucleo
        self.led_manager = led_manager
        self.debug = debug
        self.view_queue = view
        # init nucleo asap because other members need it.
        self.nucleo.startup()
        #self.led_manager.startup(TIMEBASE_MS, self.debug)
        self.parts = {
            EventElement.BUMPER1: Bumper(LedElements.BUMPER1, self.led_manager),
            EventElement.BUMPER2: Bumper(LedElements.BUMPER2, self.led_manager), 
            EventElement.BUMPER3: Bumper(LedElements.BUMPER3, self.led_manager),
            EventElement.TARGET1: Target(LedElements.TARGET1, self.led_manager),
            EventElement.TARGET2: Target(LedElements.TARGET2, self.led_manager),
            EventElement.TARGET3: Target(LedElements.TARGET3, self.led_manager),
        }

    def update(self):
        event = self.nucleo.getEvent() 
        if event:
            print(f'received event -> {event}')
            self.nucleo.sendEvent('ack')
            self.resolve_event(event)
    
    def resolve_event(self, event: PinballEvent):
        if event.element in self.parts.keys():
            self.parts[event.element].resolve_event()
        else:
            print("sorry not recognized event")