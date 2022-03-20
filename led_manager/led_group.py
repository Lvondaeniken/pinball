from led_event import LedEvent
from led_color import LedColor
class LedGroup:
    def __init__(self, led_count):
        self.event_queue = []
        self.led_states = []
        self.led_count = led_count

        for i in range(led_count):
            self.led_states.append(LedColor(0,0,0))

    def add_animation(self, event: LedEvent):
        self.event_queue.append(event)
        
    def get_next_frame(self):
        if not len(self.event_queue) == 0:
            ret = self.event_queue[0].get_next_frame()
            if ret == None:
                self.event_queue.pop(0)
            else:
                self.led_states = ret
        return self.led_states

if __name__=='__main__':
    l = LedGroup(10)
    print(l.get_next_frame())
