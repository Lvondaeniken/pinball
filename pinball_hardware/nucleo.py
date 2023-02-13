from serial import Serial
import config.cfg as cfg
import socket


def is_endline(char: str) -> bool:
    if char == "\r":
        return True
    elif char == "\n":
        return True
    else:
        return False


class Nucleo:
    def __init__(self) -> None:
        self.s = socket.socket()
        self.s.connect((cfg.HOST, cfg.PORT))

    def transmit_to_nucleo(self) -> None:
        data = self.con.recv(1024).decode("utf-8")
        if not data:
            return
        else:
            self.ser.write(data.encode())

    def receive_from_nucleo(self) -> bool:
        if self.ser.in_waiting == 0:
            return False
        char = self.ser.read().decode()
        if not is_endline(char):
            self.incoming_msg_buffer += char
            return False
        else:
            return True

    def reset_buffer(self) -> None:
        self.incoming_msg_buffer = ""

    def run(self):
        print("nucleo receiving started")
        self.ser = Serial(port=cfg.NUCLEO_PORT, baudrate=cfg.NUCLEO_BAUD)
        self.incoming_msg_buffer: str = ""
        while True:
            self.transmit_to_nucleo()
            if self.receive_from_nucleo():
                self.s.send(self.incoming_msg_buffer.encode())
                print(self.incoming_msg_buffer)
                self.reset_buffer()


if __name__ == "__main__":
    Nucleo().run()
