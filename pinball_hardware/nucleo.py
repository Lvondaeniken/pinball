from serial.serialwin32 import Serial
from multiprocessing import Process, Queue
from events.events import PinballEvent 
from events.event_factory import get_event_from_string 


class Nucleo(Process):
    def startup(self) -> None:
        self.toNucleo = Queue()
        self.fromNucleo = Queue()
        self.start()

    def sendEvent(self, event: str) -> None:
        self.toNucleo.put(event)

    def getEvent(self) -> PinballEvent:
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
                return
            char = self.ser.read().decode()
            if char == '\r' or char == '\n':
                return True
            else:
                self.incoming_nucleo_msg_buffer += char
                return False

    def resetIncomingMsgBuffer(self) -> None:
        self.incoming_nucleo_msg_buffer = ""


    def run(self):
        self.ser = Serial(port='COM8', baudrate=9600)
        self.incoming_nucleo_msg_buffer = ""
        while True:
            self.transmitPendingMessageToNucleo()
            if self.receiveIncomingMsgFromNucleo():
                self.fromNucleo.put(self.incoming_nucleo_msg_buffer)
                self.resetIncomingMsgBuffer()
                