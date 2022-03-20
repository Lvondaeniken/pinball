from multiprocessing import Process, Queue
from time import sleep
from led_group import LedGroup

from led_color import LedColor
from led_switch import LedSwitch
from led_event import LedEvent, LedAnimations, LedElements


class LedManager(Process):
    def startup(self, timebase_ms):
        self.timebase_ms = timebase_ms
        self.toManager = Queue()
        self.fromManager = Queue()
        self.start()

    def send_event(self, event: LedEvent):
        self.toManager.put(event)


    def run(self):
        self.bumper1 = LedGroup(12)
        self.bumper2 = LedGroup(12) 
        self.bumper3 = LedGroup(12) 

        while True:
            sleep(self.timebase_ms/10)
            print('hello')
            self.check_new_events()
            self.update_strip()
                
    def update_strip(self):
        next_frame = []
        next_frame.extend(self.bumper1.get_next_frame())
        next_frame.extend(self.bumper2.get_next_frame())
        next_frame.extend(self.bumper3.get_next_frame())
        for i in next_frame: 
            print(i, end=', ')

    def check_new_events(self):
        while not self.toManager.empty():
            event = self.toManager.get()
            if event.target == LedElements.BUMPER1:
                if event.animation == LedAnimations.SWITCH:
                    self.bumper1.add_animation(LedSwitch(event.color, 12))
            elif event.target == LedElements.BUMPER2:
                if event.animation == LedAnimations.SWITCH:
                    self.bumper2.add_animation(LedSwitch(event.color, 12))
            elif event.target == LedElements.BUMPER3:
                if event.animation == LedAnimations.SWITCH:
                    self.bumper3.add_animation(LedSwitch(event.color, 12))

if __name__=='__main__':
    l = LedEvent(LedAnimations.SWITCH, LedElements.BUMPER1, LedColor(1,1,1), LedColor(0,0,0))
    manager = LedManager()
    manager.startup(10)
    sleep(1)
    manager.send_event(l)
    while True:
        pass
