from abc import ABC, abstractmethod
from events.events import PinballEvent
from led.led_manager import LedManager
from multiprocessing import Queue


class Questbase(ABC):
    @abstractmethod
    def __init__(self, gui: Queue, led: LedManager):
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass

    @abstractmethod
    def update(self, event: PinballEvent) -> None:
        pass
