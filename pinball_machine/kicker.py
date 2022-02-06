from pinball_machine.nucleo import Nucleo


class Kicker:
    def __init__(self, nucleo: Nucleo):
        self.nucleo = nucleo

    def enable(self):
        print('enabel kicker')
        self.nucleo.sendEvent('kOn')       

    def disable(self):
        print('disable kicker')
        self.nucleo.sendEvent('kOff')