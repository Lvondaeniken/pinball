from abc import ABC, abstractmethod
from pinball_hardware.pinball_machine import PinballMachine
from game_logic.event import PinballEvent
class Questbase(ABC):
    @abstractmethod
    def register_pinball_machine(self, machine: PinballMachine):
        pass

    @abstractmethod
    def report_event(self, event: PinballEvent):
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass
