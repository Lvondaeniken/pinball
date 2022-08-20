from game_logic.Quests.Questbase import Questbase
from pinball_hardware.pinball_machine import PinballMachine

class Quest1(Questbase):
    def register_pinball_machine(self, machine: PinballMachine):
        self.machine = machine 

    def is_done(self) -> bool:
        #if self.machine.parts['b1'].get_hit_count() == 3:
            #print("currently checking if the quest1 is finished or not...")
            #return True
        #else:
        #    return False
        return False

if __name__=='__main__':
    q = Quest1()