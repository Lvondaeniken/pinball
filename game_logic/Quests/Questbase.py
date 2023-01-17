from abc import ABC, abstractmethod
from events.events import PinballEvent
from pinball_hardware.pinball_machine import PinballMachine
from multiprocessing import Queue


class Questbase(ABC):
    @abstractmethod
    def register(self, gui: Queue):
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass

    @abstractmethod
    def update(self, event: PinballEvent) -> None:
        pass
