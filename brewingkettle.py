import serial
import time

#ser.write("G21G91G1Y10F25\r\n")
#ser.write("G90 G21\r\n")
#grbl_out = ser.readline() # Wait for response
#print grbl_out
#raw_input("  Press <Enter> to exit and disable grbl.")
#ser.close()

class BrewingKettle:
    def __init__(self):
        self.ser = serial.Serial(port='', baudrate=115200)        
        self.ser.write("\r\n\r\n")
        time.sleep(2) # Wait for grbl to initializeR
        ser.flushInput() # Flush startup text in serial input

    def moveUp(self):
        print("moving brewing kettle up...")
        # move up until limitswitch is triggered
        #self.ser("")

    def moveDown(self):
        print("moving brewing kettle down...")
        # move down until limitswitch is triggered

    def getCurrentPosition(self):
        print("get current position of brewing kettle")

ser = serial.Serial(port='/dev/ttyACM0',
                    baudrate= 115200)


if __name__ == '__main__':
    b = BrewingKettle()
    if b.getCurrentPosition() == 1:
        b.moveUp()
    else:
        b.moveDown()


