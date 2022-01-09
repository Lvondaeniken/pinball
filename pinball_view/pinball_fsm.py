from statemachine import StateMachine, State

class PinballStatemachine(StateMachine):
    step1 = State('step1', init=True)
    step2 = State('step2')
    step3 = State('step3')
    step4 = State('step4')
    step5 = State('step5')
    step6 = State('step6')
    step7 = State('step7')
    step8 = State('step8')