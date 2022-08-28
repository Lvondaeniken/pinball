from led_handling.led_interface import LedInterface
from led_handling.led_color import LedColor


class DummyStrip(LedInterface):
    def __init__(self):
        print("starting dummy strip")

    def setPixelColor(self, index: int, color: LedColor):
        # print(f'changing color of index {index}')
        pass

    def show(self):
        pass
