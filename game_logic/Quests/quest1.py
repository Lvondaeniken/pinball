from game_logic.Quests.Questbase import Questbase
from pinball_hardware.pinball_machine import PinballMachine


class Quest1(Questbase):
    def register_pinball_machine(self, machine: PinballMachine):
        self.machine = machine 

    def report_event(self, event: str):
        pass

    def is_done(self) -> bool:
        print("currently checking if the quest1 is finished or not...")
        return True

if __name__=='__main__':
    q = Quest1()