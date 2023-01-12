from led.led_manager import LedManager
from led.led_event import LedEvent, LedAnimations, LedElements
from led.color import LedColor


class Target:
    def __init__(self, led_id: LedElements, led_manager: LedManager):
        self.led_id: LedElements = led_id
        self.led_manager: LedManager = led_manager
        self.hit_flag = False

    def reset(self):
        self.hit_flag = False

    def is_hit(self):
        return self.hit_flag

    def resolve_event(self):
        self.hit_flag = True
        self.led_manager.send_event(
            LedEvent(
                LedAnimations.BLINK,
                self.led_id,
                LedColor(100, 0, 0),
                LedColor(0, 100, 0),
                2,
            )
        )
