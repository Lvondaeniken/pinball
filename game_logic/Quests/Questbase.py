from abc import ABC, abstractmethod
from pinball_hardware.pinball_machine import PinballMachine
class Questbase(ABC):
    @abstractmethod
    def register_pinball_machine(self, machine: PinballMachine):
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass
