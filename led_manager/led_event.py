from enum import Enum
from led_manager.led_color import LedColor
class LedAnimations(Enum):
    SWITCH = 1
    BLINK = 2
    WALK = 3

class LedElements(Enum):
    BUMPER1 = 1
    BUMPER2 = 2
    BUMPER3 = 3
    BALLSHOOTER = 4
    TARGET1 = 5
    TARGET2 = 6
    TARGET3 = 7

class LedEvent:
    def __init__(self, animation: LedAnimations, target: LedElements, color: LedColor, background: LedColor, duration_s=0):
        self.animation = animation
        self.target = target
        self.color = color
        self.background = background
        self.duration_s = duration_s

