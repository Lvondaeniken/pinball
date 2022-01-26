from queue import Queue
from pinball_machine.pinball_machine import PinballMachine
from statemachine import StateMachine, State

class PinballStatemachine(StateMachine):
    startup = State('Menu', initial=True)
    step1 = State('Sammle Malz')
    step2 = State('Animation Mahlen')
    step3 = State('Mische das Malz')
    step4 = State('Animation Läutern')
    step5 = State('Aktivierung Hopfen')
    step6 = State('Sammle Hopfen')
    step7 = State('Hopfen einfüllen')
    step8 = State('Animation boiling')
    step9 = State('Hefe züchten')
    step10 = State('Hefe beifügen')
    step11 = State('Animation fermentieren')
    step12 = State('final mode')

    start = startup.to(step1)
    s1 = step1.to(step2)
    s2 = step2.to(step3)
    s3 = step3.to(step4)
    s4 = step4.to(step5)
    s5 = step5.to(step6)
    s6 = step6.to(step7)
    s7 = step7.to(step8)
    s8 = step8.to(step9)
    s9 = step9.to(step10)
    s10 = step10.to(step11)
    s11 = step11.to(step12)

    def __init__(self, queue: Queue):
        super().__init__()
        self.pinballmachine = PinballMachine(queue)

    def on_enter_step1(self):
        pass

    def on_enter_step2(self):
        pass
    
    def on_enter_step3(self):
        pass
    def on_enter_step4(self):
        pass
    def on_enter_step5(self):
        pass
    def on_enter_step6(self):
        pass
    def on_enter_step7(self):
        pass
    def on_enter_step8(self):
        pass
    def on_enter_step9(self):
        pass
    def on_enter_step10(self):
        pass
    def on_enter_step11(self):
        pass
    def on_enter_step12(self):
        pass
