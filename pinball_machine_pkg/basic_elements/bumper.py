from led_manager.led_manager import LedManager
from led_manager.led_event import LedElements 
class Bumper:
    MAX_LEVEL = 6
    def __init__(self, led_id: LedElements, led_manager: LedManager):
        self.led_id = led_id 
        self.led_manager = led_manager
        self.hit_counter = 0

    def reset_hit_count(self):
        self.hit_counter = 0

    def register_hit(self):
        if self.hit_counter < MAX_LEVEL:
            self.hit_counter += 1

    def get_hit_count(self):
        return self.hit_counter

