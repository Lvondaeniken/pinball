from serial import Serial
from multiprocessing import Process, Queue
class Nucleo(Process):
    def startup(self):
        self.toNucleo = Queue()
        self.fromNucleo = Queue()
        self.start()

    def sendEvent(self, event):
        self.toNucleo.put(event)

    def getEvent(self):
        if not self.fromNucleo.empty():
            return self.fromNucleo.get()
            
    def run(self):
        ser = Serial(port = 'ttyUsb', baudrate=115200)
        line = ""
        while True:
            if not self.toNucleo.empty():
                msg = self.toNucleo.get()
                ser.write(msg)

            length = ser.in_waiting()
            if length > 0:
                char = ser.read().decode()
                line += char
                if char == '\n':
                    self.fromNucleo.put(ser.readline())
                    line = ""

if __name__ == '__main__':
    n = Nucleo()
    n.startup()

    while True:
        event = n.getEvent()
        if not event == None:
            print(f'Received from nucleo -> {n.getEvent()}')