from statemachine import StateMachine, State

class PinballStatemachine(StateMachine):
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

    def on_enter_step1(self):
        ballshooter.trigger()
        bumper.start_collecting_malt()

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
