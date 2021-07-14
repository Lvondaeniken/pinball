import serial
import time

ser = serial.Serial(port='/dev/ttyACM0',
                    baudrate= 115200)

ser.write("\r\n\r\n")
time.sleep(2)   # Wait for grbl to initializeR
ser.flushInput()  # Flush startup text in serial input

ser.write("G21G91G1Y10F25\r\n")
ser.write("G90 G21\r\n")
grbl_out = ser.readline() # Wait for response
print grbl_out
raw_input("  Press <Enter> to exit and disable grbl.")
ser.close()