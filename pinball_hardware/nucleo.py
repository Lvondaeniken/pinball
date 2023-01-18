from serial import Serial
import multiprocessing as mp
from events.events import PinballEvent
from events.event_factory import get_event_from_string
from typing import Optional

SER_PORT = "/dev/ttyUSB1"
BAUD = 9600


def is_endline(char: str) -> bool:
    if char == "\r":
        return True
    elif char == "\n":
        return True
    else:
        return False


class Nucleo(mp.Process):
    def startup(self) -> None:
        self.daemon: bool = True
        self.to_nucleo = mp.Queue()
        self.from_nucleo = mp.Queue()
        self.start()

    def send_event(self, event: str) -> None:
        self.to_nucleo.put(event)

    def get_event(self) -> Optional[PinballEvent]:
        if not self.from_nucleo.empty():
            event_str = self.from_nucleo.get()
            return get_event_from_string(event_str)
        else:
            return None

    def transmit_to_nucleo(self) -> None:
        if not self.to_nucleo.empty():
            msg = self.to_nucleo.get()
            self.ser.write(msg.encode())

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
        self.ser = Serial(port=SER_PORT, baudrate=BAUD)
        self.incoming_msg_buffer: str = ""
        while True:
            self.transmit_to_nucleo()
            if self.receive_from_nucleo():
                self.from_nucleo.put(self.incoming_msg_buffer)
                print(self.incoming_msg_buffer)
                self.reset_buffer()
