from pinball_hardware.nucleo import Nucleo
import serial
class BallShooter:
    def __init__(self, ser: Nucleo) -> None:
        self.ser = ser

    def trigger(self):
        self.ser.write()