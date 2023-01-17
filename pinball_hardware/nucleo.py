# from serial.serialwin32 import Serial
from serial import Serial
from multiprocessing import Process, Queue
from events.events import PinballEvent
from events.event_factory import get_event_from_string
from typing import Optional


class Nucleo(Process):
    def startup(self) -> None:
        self.daemon: bool = True
        self.toNucleo = Queue()
        self.fromNucleo = Queue()
        self.start()

    def sendEvent(self, event: str) -> None:
        self.toNucleo.put(event)

    def getEvent(self) -> Optional[PinballEvent]:
        if not self.fromNucleo.empty():
            event_str = self.fromNucleo.get()
            return get_event_from_string(event_str)
        else:
            return None

    def transmitPendingMessageToNucleo(self) -> None:
        if not self.toNucleo.empty():
            msg = self.toNucleo.get()
            self.ser.write(msg.encode())

    def receiveIncomingMsgFromNucleo(self) -> bool:
        if self.ser.in_waiting == 0:
            return False
        char = self.ser.read().decode()
        if char == "\r" or char == "\n":
            return True
        else:
            self.incoming_nucleo_msg_buffer += char
            return False

    def resetIncomingMsgBuffer(self) -> None:
        self.incoming_nucleo_msg_buffer = ""

    def run(self):
        print("nucleo receiving started")
        self.ser = Serial(port="/dev/ttyUSB1", baudrate=9600)
        self.incoming_nucleo_msg_buffer = ""
        self.ser.write("hello".encode())
        while True:
            self.transmitPendingMessageToNucleo()
            if self.receiveIncomingMsgFromNucleo():
                self.fromNucleo.put(self.incoming_nucleo_msg_buffer)
                print(self.incoming_nucleo_msg_buffer)
                self.resetIncomingMsgBuffer()
