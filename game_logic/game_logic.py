from game_logic.pinball_statemachine import PinballStatemachine
from pinball_machine.pinball_machine import PinballMachine
from multiprocessing import Queue

class GameLogic:
    def __init__(self, view_event_queue: Queue):
        self.machine = PinballMachine(view_event_queue, True) 
        self.fsm = PinballStatemachine(self.machine) 

    def run(self):
        self.fsm.start() 
        while True:
            self.machine.check_events()
            self.check()

    def check(self):
        while True:
            if self.fsm.is_startup:
                self.handle_startup()
            elif self.fsm.is_step1:
                self.handle_step1()
            elif self.fsm.is_step2:
                self.handle_step2()
            elif self.fsm.is_step3:
                self.handle_step3()
            elif self.fsm.is_step4:
                self.handle_step4()
            elif self.fsm.is_step5:
                self.handle_step5()
            elif self.fsm.is_step6:
                self.handle_step6()
            elif self.fsm.is_step7:
                self.handle_step7()
            elif self.fsm.is_step8:
                self.handle_step8()
            elif self.fsm.is_step9:
                self.handle_step9()
            elif self.fsm.is_step10:
                self.handle_step10()
            elif self.fsm.is_step11:
                self.handle_step11()
            elif self.fsm.is_step12:
                self.handle_step12()
            else:
                print('unknown state')

    def handle_startup(self):
        pass

    def handle_step1(self):
        """ Malz sammeln"""
        for state in self.machine.get_bumper_states():
            if state < 6:
               return 
        self.fsm.s2()

    def handle_step2(self):
        """ Animation Mahlen""" 
        pass

    def handle_step3(self):
        """ Mische das Malz """
        pass

    def handle_step4(self):
        pass

    def handle_step5(self):
        pass

    def handle_step6(self):
        pass

    def handle_step7(self):
        pass

    def handle_step8(self):
        pass

    def handle_step9(self):
        pass
        
    def handle_step10(self):
        pass

    def handle_step11(self):
        pass

    def handle_step12(self):
        pass

if __name__=='__main__':
    gl = GameLogic()
    gl.start()
    gl.check()

