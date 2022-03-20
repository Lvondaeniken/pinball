from multiprocessing import Process, Queue
from enum import Enum
from time import sleep

from led_manager.led_color import LedColor
from led_manager.led_on_off import LedSwitch

class LedAnimations(Enum):
    ON = 1
    OFF = 2
    BLINK = 3
    WALK = 4

class LedElements(Enum):
    BUMPER1 = 1
    BUMPER2 = 2
    BUMPER3 = 3
    BALLSHOOTER = 4

class LedEvent:
    def __init__(self, animation: LedAnimations, target: LedElements, color: LedColor, background: LedColor, duration_s=0):
        self.animation = animation
        self.target = target
        self.color = color
        self.background = color
        self.duration_s = duration_s

class LedManager(Process):
    def startup(self, timebase_ms):
        self.timebase_ms = timebase_ms
        self.toManager = Queue()
        self.fromManager = Queue()
        self.led_index = {
            LedElements.BUMPER1: [0, 9],
            LedElements.BUMPER2: [10, 19],
            LedElements.BUMPER3: [20, 29],
            LedElements.BALLSHOOTER: [30, 39]
        }
        self.start()

    def send_event(self, event: LedEvent):
        self.toManager.put(event)


    def run(self):
        self.bumper1_events = []
        self.bumper2_events = []
        self.bumper3_events = []
        self.ballshooter_events = []
        self.next_led_states = []
        for i in range(40):
            self.next_led_states.append(LedColor(0,0,0))

        while True:
            sleep(self.timebase_ms/1000)
            self.check_queue()
                
    def update_bumper1(self):
        if not len(self.bumper1_events) == 0:
            ret = self.bumper1_events[0].get_next_frame()
            if ret == None:
                self.bumper1_events.pop(0)
            else:
                start_index, end_index = self.led_index[LedElements.BUMPER1]
                for i in range(len(ret)):
                    self.next_led_states[start_index+i]=ret[i] 


    def check_queue(self):
        while not self.toManager.empty():
            event = self.toManager.get()
            if event.target == LedElements.BUMPER1:
                if event.animation == LedAnimations.ON:
                    self.bumper1_events.append(LedSwitch(event.color, 10))
            elif event.target == LedElements.BUMPER2:
                self.bumper2_events.append(event)
            elif event.target == LedElements.BUMPER3:
                self.bumper3_events.append(event)
            elif event.target == LedElements.BALLSHOOTER:
                self.ballshooter_events.append(event)


if __name__=='__main__':
    l = LedManager(20)
    l.startup()
    l.send_event(LedEvent(LedAnimations.ON, LedElements.BUMPER1, LedColor(100,0,0), LedColor(0,0,0)))
