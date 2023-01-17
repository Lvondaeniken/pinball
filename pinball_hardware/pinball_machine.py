from pinball_hardware.basic_parts.bumper import Bumper
from pinball_hardware.basic_parts.target import Target

# from pinball_hardware.basic_parts.steppers import Stepperdriver
from led.led_manager import LedManager
from led.led_event import LedElements
from events.events import EventElement, PinballEvent


class PinballMachine:
    def __init__(self, led_manager: LedManager):
        self.led_manager = led_manager

        self.parts = {
            EventElement.BUMPER1: Bumper(LedElements.BUMPER1, self.led_manager),
            EventElement.BUMPER2: Bumper(LedElements.BUMPER2, self.led_manager),
            EventElement.BUMPER3: Bumper(LedElements.BUMPER3, self.led_manager),
            EventElement.TARGET1: Target(LedElements.TARGET1, self.led_manager),
            EventElement.TARGET2: Target(LedElements.TARGET2, self.led_manager),
            EventElement.TARGET3: Target(LedElements.TARGET3, self.led_manager),
        }

    def update(self, event):
        if event:
            print(f"received event -> {event}")
            self.resolve_event(event)

    def resolve_event(self, event: PinballEvent):
        if event.element in self.parts.keys():
            self.parts[event.element].resolve_event()
        else:
            print("sorry not recognized event")
