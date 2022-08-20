from led_handling.led_event import LedEvent
from led_handling.led_color import LedColor
from led_handling.led_group import LedGroup
from led_handling.led_event import LedAnimations, LedElements
from led_handling.led_manager import LedManager
#
# LED strip configuration:
import sys,os

if __name__=='__main__':
    l = LedEvent(LedAnimations.SWITCH, LedElements.BUMPER1, LedColor(1,1,1), LedColor(0,0,0))
    manager = LedManager()
    manager.startup(50)

    while True:
        c = input()
        if c == '1':
            manager.send_event(LedEvent(LedAnimations.SWITCH, LedElements.BUMPER1, LedColor(255,1,1), LedColor(0,0,0)))
        elif c=='2':
            manager.send_event(LedEvent(LedAnimations.SWITCH, LedElements.BUMPER1, LedColor(0,0,0), LedColor(0,0,0)))
        elif c=='3':
            manager.send_event(LedEvent(LedAnimations.SWITCH, LedElements.BUMPER2, LedColor(255,1,1), LedColor(0,0,0)))
        elif c=='4':
            manager.send_event(LedEvent(LedAnimations.SWITCH, LedElements.BUMPER2, LedColor(0,0,0), LedColor(0,0,0)))
        elif c=='5':
            manager.send_event(LedEvent(LedAnimations.SWITCH, LedElements.BUMPER3, LedColor(255,1,1), LedColor(0,0,0)))
        elif c=='6':
            manager.send_event(LedEvent(LedAnimations.SWITCH, LedElements.BUMPER3, LedColor(0,0,0), LedColor(0,0,0)))
        elif c=='7':
            manager.send_event(LedEvent(LedAnimations.BLINK, LedElements.BUMPER3, LedColor(0,255,0), LedColor(255,0,0)))
