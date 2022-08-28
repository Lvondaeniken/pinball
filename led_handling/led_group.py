from led_handling.animations import AnimationInterface
from led_handling.blinking import BlinkingLight
from led_handling.led_animations import LedAnimations
from led_handling.led_event import LedEvent
from led_handling.led_color import LedColor
from led_handling.led_switch import LedSwitch

class LedGroup:
    def __init__(self, led_count, timebase_ms: int):
        self.event_queue : list[AnimationInterface] = []
        self.led_states : list[LedColor] = []
        self.led_count : int = led_count
        self.timebase_ms = timebase_ms
        for i in range(self.led_count):
            self.led_states.append(LedColor(0,0,0))
        self.set_all_off()
             
    def get_led_count(self)->int:
        return self.led_count 

    def add_event(self, event: LedEvent):
        if event.animation == LedAnimations.BLINK:
            self.event_queue.append(BlinkingLight(self.timebase_ms, event.duration, 1, self.led_count, event.color, event.background))
        elif event.animation == LedAnimations.SWITCH:
            self.event_queue.append(LedSwitch(event.color, self.led_count))
        else:
            pass

    def force_event(self, event: LedEvent):
        self.event_queue.insert(0, LedSwitch(event.color, self.led_count))

    def get_next_frame(self) -> list[LedColor]:
        if len(self.event_queue) == 0:
            self.set_all_off()
        else:
            ret = self.event_queue[0].get_next_frame()
            if ret == None:
                print("event finished")
                # delete animation if finished
                self.event_queue.pop(0)
                self.set_all_off()
            else:
                if len(ret) == self.led_count:
                    self.led_states = ret
                else:
                    self.set_all_off()
        return self.led_states

    def set_all_off(self):
        for i in range(self.led_count):
            self.led_states[i] =LedColor(0,0,0)
