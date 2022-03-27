from led_manager.led_manager import LedManager
from led_manager.led_event import LedEvent
class Bumper:
    def __init__(self, identifier: str, leds: list):
        self.id = identifier  
        self.leds = leds

    def share_led_manager(led_manager: LedManager):
        self.led_manager = led_manager
        
    def increment_level(self):
        self.current_level += 1
        print(f'increment level of {self.id}')

    def reset_level(self):
        self.current_level = 0
