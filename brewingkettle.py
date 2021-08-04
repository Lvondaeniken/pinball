import serial
import time

#ser.write("G21G91G1Y10F25\r\n")
#ser.write("G90 G21\r\n")
#grbl_out = ser.readline() # Wait for response
#print grbl_out
#raw_input("  Press <Enter> to exit and disable grbl.")
#ser.close()


# Achtung zuerst "$X" schicken um Alarm Zustand zu verlassen.

class BrewingKettle:
    def __init__(self):
        self.ser = serial.Serial(port='/dev/tty.usbmodem14201', baudrate=115200)        
        self.ser.write("\r\n\r\n".encode())
        time.sleep(2) # Wait for grbl to initializer
        self.ser.flushInput() # Flush startup text in serial input
        self.ser.write("$X\r\n".encode())

    def moveUp(self):
        print("moving brewing kettle up...")
        # move up until limitswitch is triggered
        self.ser.write("G21G91G1X-3.7F200\r\n".encode())
        self.ser.write("G90 G21\r\n".encode())

    def moveDown(self):
        print("moving brewing kettle down...")
        self.ser.write("G21G91G1X3.7F200\r\n".encode())
        self.ser.write("G90 G21\r\n".encode())

    def getCurrentPosition(self):
        print("get current position of brewing kettle")

if __name__ == '__main__':
    b = BrewingKettle()
    b.moveUp()
    time.sleep(2)
    b.moveDown()


