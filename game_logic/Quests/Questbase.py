from abc import ABC, abstractmethod
from pinball_hardware.pinball_machine import PinballMachine
from multiprocessing import Queue


class Questbase(ABC):
    @abstractmethod
    def register(self, machine: PinballMachine, gui: Queue):
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass

    @abstractmethod
    def update(event) -> None:
        pass
