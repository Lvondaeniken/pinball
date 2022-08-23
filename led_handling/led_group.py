from led_handling.animations import AnimationInterface
from led_handling.blinking import BlinkingLight
from led_handling.led_animations import LedAnimations
from led_handling.led_event import LedEvent
from led_handling.led_color import LedColor
from led_handling.led_switch import LedSwitch

TIMEBASE_MS = 10
class LedGroup:
    def __init__(self, led_count):
        self.event_queue : list[AnimationInterface] = []
        self.led_states : list[LedColor] = []
        self.led_count : int = led_count

        for i in range(led_count):
            self.led_states.append(LedColor(0,0,0))
             
    def get_led_count(self)->int:
        return self.led_count 

    def add_event(self, event: LedEvent):
        if event.animation == LedAnimations.BLINK:
            self.event_queue.append(BlinkingLight(TIMEBASE_MS, event.duration, 1, self.led_count, event.color, event.background))
        elif event.animation == LedAnimations.SWITCH:
            self.event_queue.append(LedSwitch(event.color, self.led_count))
        else:
            pass

    def force_event(self, event: LedEvent):
        self.event_queue.insert(0, LedSwitch(event.color, self.led_count))

    def get_next_frame(self) -> list[LedColor]:
        if len(self.event_queue) == 0:
            return []
        ret = self.event_queue[0].get_next_frame()
        if ret == None:
            # delete animation if finished
            self.event_queue.pop(0)
        else:
            self.led_states = ret
        return self.led_states
