from led_manager_pkg.led_event import LedEvent
from led_manager_pkg.led_color import LedColor
from led_manager_pkg.led_group import LedGroup
from led_manager_pkg.led_event import LedAnimations, LedElements
from led_manager_pkg.led_manager import LedManager
#
# LED strip configuration:
import sys,os

if __name__=='__main__':
    sys.path.append(os.getcwd())
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
