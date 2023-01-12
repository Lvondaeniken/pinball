import serial
import time

# Achtung zuerst "$X" schicken um Alarm Zustand zu verlassen.


class Stepperdriver:
    def __init__(self):
        self.ser = serial.Serial(port="/dev/tty.usbmodem14201", baudrate=115200)
        self.ser.write("\r\n\r\n".encode())
        time.sleep(2)  # Wait for grbl to initializer
        self.ser.flushInput()  # Flush startup text in serial input
        self.ser.write("$X\r\n".encode())

    def moveBrewingKettleUp(self):
        print("moving brewing kettle up...")
        # move up until limitswitch is triggered
        self.ser.write("G21G91G1X-3.7F200\r\n".encode())
        self.ser.write("G90 G21\r\n".encode())

    def moveBrewingKettleDown(self):
        print("moving brewing kettle down...")
        self.ser.write("G21G91G1X3.7F200\r\n".encode())
        self.ser.write("G90 G21\r\n".encode())

    def openRailDiverter(self):
        print("opening rail diverter...")
        self.ser.write("G21G91G1Y-0.12F20\r\n".encode())
        self.ser.write("G90 G21\r\n".encode())

    def closeRailDiverter(self):
        print("closing rail diverter...")
        self.ser.write("G21G91G1Y0.12F20\r\n".encode())
        self.ser.write("G90 G21\r\n".encode())

    def getCurrentPosition(self):
        print("get current position of brewing kettle")


if __name__ == "__main__":
    b = Stepperdriver()
    b.moveBrewingKettleUp()
    time.sleep(2)
    b.moveBrewingKettleDown()
