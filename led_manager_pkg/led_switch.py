from led_manager_pkg.led_color import LedColor
class LedSwitch:
    def __init__(self, color: LedColor, led_count: int):
        self.color = color
        self.led_count = led_count
        self.done = False
        
    def get_next_frame(self):
        ret = []
        if self.done == False:
            for led in range(self.led_count):
                ret.append(self.color)
            self.done = True
            return ret
        else:
            return None
