import serial
class BallShooter:
    def __init__(self, ser: serial.Serial):
        self.ser = ser
        pass

    def trigger(self):
        self.ser.write()