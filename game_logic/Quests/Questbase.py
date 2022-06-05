from abc import ABC, abstractmethod
from pinball.pinball_machine_pkg.pinball_machine import PinballMachine


class Questbase(ABC):
    @abstractmethod
    def register_pinball_machine(self, machine: PinballMachine):
        pass

    @abstractmethod
    def report_event(self, event: str):
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass
