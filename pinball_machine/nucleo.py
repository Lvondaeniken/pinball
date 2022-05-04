from serial import Serial
from multiprocessing import Process, Queue
class Nucleo(Process):
    def startup(self, debug=False):
        self.toNucleo = Queue()
        self.fromNucleo = Queue()
        self.debug = debug
        self.start()

    def sendEvent(self, event):
        self.toNucleo.put(event)

    def getEvent(self):
        if not self.fromNucleo.empty():
            return self.fromNucleo.get()
        else:
            return None
            
    def run(self):
        if self.debug == False:
            ser = Serial(port = '/dev/ttyAMA0', baudrate=9600)
        else: 
            #ser = Serial(port='/dev/ttys001') 
            pass
        line = ""
        while True:
            if self.debug == False:
                if not self.toNucleo.empty():
                    msg = self.toNucleo.get()
                    ser.write(msg.encode())

                length = ser.in_waiting
                if length > 0:
                    char = ser.read()
                    line += char.decode()
                    if char == '\r'.encode():
                        self.fromNucleo.put(line.rstrip('\r').rstrip('\n'))
                        line = ""
            else:
                if self.toNucleo.empty():
                    msg = self.toNucleo.get()
                    print(msg)
                try:
                    s = input()
                    self.fromNucleo.put(s)
                except:
                    pass
                    
if __name__ == '__main__':
    n = Nucleo()
    n.startup()
    s = "start".encode()
    n.sendEvent(s)
    while True:
        
        event = n.getEvent()
        if not event == None:
            print(f'Received from nucleo -> {event}')
