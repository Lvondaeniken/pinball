import serial
from pinball_view.pinball_fsm import PinballStatemachine

class PinballMachine:
    def __init__(self, port):
        self.serial = serial.Serial(port='/dev/tty.usbmodem14201', baudrate=115200) 
        self.fsm = PinballStatemachine(self.serial)

    def listen_serial(self, command: str):
        while True:
            self.fsm.send_command(self.serial.readline())

if __name__=='__main__':
    p = PinballMachine('/dev/tty.usbmodem14201')
    p.listen_serial()
    input("press Enter to stop...")

