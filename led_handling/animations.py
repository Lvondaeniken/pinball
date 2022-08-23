from abc import ABC
from led_handling.led_color import LedColor

class AnimationInterface(ABC): 
    def get_next_frame() -> list[LedColor]:
        ...
    
