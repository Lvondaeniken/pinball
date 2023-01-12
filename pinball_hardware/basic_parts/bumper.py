from led.led_manager import LedManager
from led.led_event import LedElements, LedEvent
from led.animations import LedAnimations
from led.color import LedColor

MAX_LEVEL = 6


class Bumper:
    def __init__(self, led_id: LedElements, led_manager: LedManager):
        self.led_id = led_id
        self.led_manager = led_manager
        self.hit_count = 0

    def reset(self):
        self.hit_counter = 0

    def get_hit_count(self):
        return self.hit_count

    def resolve_event(self):
        if self.hit_count < MAX_LEVEL:
            self.hit_count += 1
        self.led_manager.send_event(
            LedEvent(
                LedAnimations.BLINK,
                self.led_id,
                LedColor(100, 1, 0),
                LedColor(0, 0, 100),
                5,
            )
        )
