from serial import Serial
import socket
import re

NUCLEO_PORT = "/dev/ttyACM0"
NUCLEO_BAUD = "9600"

STEPPER_PORT = "/dev/ttyUSBX"
STEPPER_BAUD = "115200"

PORT = 1234
HOST = "127.0.0.1"


def is_endline(char: str) -> bool:
    if char == "\r":
        return True
    elif char == "\n":
        return True
    elif char == "":
        return True
    else:
        return False


class Nucleo:
    def __init__(self) -> None:
        self.s = socket.socket()
        self.s.connect((HOST, PORT))

    def transmit_to_nucleo(self) -> None:
        data = self.s.recv(1024).decode("utf-8")
        if not data:
            return
        else:
            self.ser.write(data.encode("utf-8"))

    def receive_from_nucleo(self) -> bool:
        if self.ser.in_waiting == 0:
            return False
        read = self.ser.read()
        print(f"compare {read} to {bytes([0x00])}")
        if read == bytes([0x00]):
            print("skip this")
            return False
        print(read)
        char = read.decode("ascii")
        if not is_endline(char):
            self.incoming_msg_buffer += char
            print(f"recieved char: {char}")
            return False
        else:
            return True

    def reset_buffer(self) -> None:
        self.incoming_msg_buffer = ""

    def run(self):
        print("nucleo receiving started")
        self.ser = Serial(NUCLEO_PORT, baudrate=NUCLEO_BAUD)
        self.incoming_msg_buffer: str = ""
        while True:
            #self.transmit_to_nucleo()
            if self.receive_from_nucleo():
                tx = self.incoming_msg_buffer.replace("\n", "").replace(" ", "")
                self.s.send(tx.encode("utf-8"))
                print(tx)
                self.reset_buffer()


if __name__ == "__main__":
    Nucleo().run()
