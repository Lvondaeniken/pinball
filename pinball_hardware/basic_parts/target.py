from led_handling.led_manager import LedManager
from led_handling.led_event import LedEvent, LedAnimations, LedElements
from led_handling.led_color import LedColor

class Target:
    def __init__(self, id: int, leds: LedManager):
        self.id = id
        self.hit_flag = False
        self.leds = leds 

    def reset(self):
        self.hit_flag = False
    
    def is_hit(self):
        return self.hit_flag

    def resolve_event(self):
        self.hit_flag = True
        self.leds.send_event(LedEvent(LedAnimations.BLINK, LedElements.TARGET1, LedColor(100, 0, 0), LedColor(0,0,0), 2))
