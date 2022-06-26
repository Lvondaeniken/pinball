from serial.serialwin32 import Serial
from multiprocessing import Process, Queue


class Nucleo(Process):
    def startup(self) -> None:
        self.toNucleo = Queue()
        self.fromNucleo = Queue()
        self.start()

    def sendEvent(self, event: str) -> None:
        self.toNucleo.put(event)

    def getEvent(self) -> str:
        if not self.fromNucleo.empty():
            return self.fromNucleo.get()
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
            self.incoming_nucleo_msg_buffer += char
            if char == '\r':
                self.incoming_nucleo_msg_buffer.rstrip('\r').rstrip('\n')
                return True
            else:
                return False

    def resetIncomingMsgBuffer(self) -> None:
        self.incoming_nucleo_msg_buffer = ""


    def run(self):
        self.ser = Serial(port='COM3', baudrate=9600)
        self.incoming_nucleo_msg_buffer = ""
        while True:
            self.transmitPendingMessageToNucleo()
            if self.receiveIncomingMsgFromNucleo():
                self.fromNucleo.put(self.incoming_nucleo_msg_buffer)
                self.resetIncomingMsgBuffer()


if __name__ == '__main__':
    n = Nucleo()
    n.startup()
    s = "start".encode()
    n.sendEvent(s)
    while True:

        event = n.getEvent()
        if not event == None:
            print(f'Received from nucleo -> {event}')
