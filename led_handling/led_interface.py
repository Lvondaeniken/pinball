from abc import ABC
from led_handling.led_color import LedColor

class LedInterface(ABC): 
    def setPixelColor(self, index: int, color: LedColor):
        ...

    def show(self):
        ... 