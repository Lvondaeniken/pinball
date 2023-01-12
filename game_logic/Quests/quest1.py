from events.events import EventElement, PinballEvent
from game_logic.Quests.Questbase import Questbase
from pinball_hardware.pinball_machine import PinballMachine


class Quest1(Questbase):
    def register(self, machine: PinballMachine):
        self.machine = machine

    def is_done(self) -> bool:
        if self.machine.parts[EventElement.BUMPER1].get_hit_count() == 3:
            # print("currently checking if the quest1 is finished or not...")
            print("Quest 1 finished.")
            return True
        else:
            return False

    def update(self, event: PinballEvent):
        self.event = event
        pass


if __name__ == "__main__":
    q = Quest1()

