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
        else:
            return None
            
    def run(self):
        ser = Serial(port = '/dev/ttyAMA0', baudrate=9600)
        line = ""
        while True:
            if not self.toNucleo.empty():
                msg = self.toNucleo.get()
                ser.write(msg.encode())

            length = ser.in_waiting
            if length > 0:
                char = ser.read()
                line += char.decode()
                if char == '\r'.encode():
                    self.fromNucleo.put(line)
                    line = ""

if __name__ == '__main__':
    n = Nucleo()
    n.startup()
    s = "start".encode()
    n.sendEvent(s)
    while True:
        
        event = n.getEvent()
        if not event == None:
            print(f'Received from nucleo -> {event}')
