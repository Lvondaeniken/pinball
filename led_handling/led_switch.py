from led_handling.animations import AnimationInterface
from led_handling.led_color import LedColor
class LedSwitch(AnimationInterface):
    def __init__(self, color: LedColor, led_count: int):
        self.color = color
        self.led_count = led_count
        self.done = False
        
    def get_next_frame(self) -> list[LedColor]:
        ret = []
        if self.done == False:
            for led in range(self.led_count):
                ret.append(self.color)
            self.done = True
            return ret
        else:
            return None
