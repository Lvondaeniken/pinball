from led_handling.led_manager import LedManager
from led_handling.led_event import LedEvent, LedAnimations, LedElements
from led_handling.led_color import LedColor

class Target:
    def __init__(self, id: int, leds: LedManager):
        self.id = id
        self.state = False
        self.leds = leds 

    def reset(self):
        self.state = False

    def resolve_event(self):
        self.state = not self.state
        self.leds.send_event(LedEvent(LedAnimations.BLINK, LedElements.TARGET1, LedColor(100, 0, 0), LedColor(0,0,0), 2))

if __name__=='__main__':
    t = Target(1, 3)
    print(t.state)
    t.report_event(0)
    print(t.state)

    
