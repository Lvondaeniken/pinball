from led_manager.led_color import LedColor
from led_manager.led_animations import LedAnimations
from led_manager.led_elements import LedElements

from dataclasses import dataclass

@dataclass
class LedEvent:
    animation: LedAnimations
    target: LedElements
    color: LedColor
    background: LedColor
    duration: int

    def get_target(self) -> LedElements:
        return self.target

    def get_color(self) -> LedColor:
        return self.color


if __name__=='__main__':
    l = LedEvent(LedAnimations.BLINK, LedElements.BALLSHOOTER, LedColor(255, 255, 255), LedColor(0,0,0), 10)
    