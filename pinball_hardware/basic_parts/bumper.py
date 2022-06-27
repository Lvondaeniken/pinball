from led_handling.led_manager import LedManager
from led_handling.led_event import LedElements 
    
MAX_LEVEL = 6
class Bumper:
    def __init__(self, led_id: LedElements, led_manager: LedManager):
        self.led_id = led_id 
        self.led_manager = led_manager
        self.hit_counter = 0

    def reset_hit_count(self):
        self.hit_counter = 0

    def resolve_event(self):
        if self.hit_counter < MAX_LEVEL:
            self.hit_counter += 1

    def get_hit_count(self):
        return self.hit_counter

