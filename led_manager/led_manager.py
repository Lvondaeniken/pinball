from multiprocessing import Process, Queue
from time import sleep

class LedManager(Process):
    def startup(self, timebase_ms: int):
        self.event_queue = Queue()
        self.timebase_ms = timebase_ms

    def add_animation(animation):
        self.event_queue.put(animation)

    def run(self):
        active = []
        while True:
            sleep(self.timebase_ms/1000)
            if not self.event_queue.empty():
                new = elf.event_queue.get()
                active.append(new)
            for i in range(len(active)):
                led_states = active[i].getNextFrame()
                
                
