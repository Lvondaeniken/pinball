from statemachine import StateMachine, State

class TrafficLightMachine(StateMachine):
    "A traffic light machine"
    green = State('Green', initial=True)
    yellow = State('Yellow')
    red = State('Reg')

    cycle = green.to(yellow)|yellow.to(red)|red.to(green)

    def on_enter_green(self):
        print('entered green')

    def on_enter_yellow(self):
        print('entered yellow')

    def on_enter_red(self):
        print('entered red')

if __name__=='__main__':
    t = TrafficLightMachine()
    t.cycle()
