from led.led_event import LedEvent
from led.color import LedColor
from led.led_event import LedAnimations, LedElements
from led.led_manager import LedManager

#
# LED strip configuration:

if __name__ == "__main__":
    manager = LedManager()
    manager.startup(False)

    while True:
        c = input()
        if c == "1":
            manager.send_event(
                LedEvent(
                    LedAnimations.SWITCH,
                    LedElements.BALLSHOOTER,
                    LedColor(0, 1, 255),
                    LedColor(0, 0, 0),
                    1000,
                )
            )
        elif c == "2":
            manager.send_event(
                LedEvent(
                    LedAnimations.SWITCH,
                    LedElements.PIPES,
                    LedColor(0, 0, 255),
                    LedColor(0, 0, 0),
                    1000,
                )
            )
        elif c == "3":
            manager.send_event(
                LedEvent(
                    LedAnimations.SWITCH,
                    LedElements.BOTTLE,
                    LedColor(0, 1, 255),
                    LedColor(0, 0, 0),
                    1000,
                )
            )
        elif c == "4":
            manager.send_event(
                LedEvent(
                    LedAnimations.SWITCH,
                    LedElements.BUMPER1,
                    LedColor(199, 190, 190),
                    LedColor(0, 0, 0),
                    1000,
                )
            )
        elif c == "5":
            manager.send_event(
                LedEvent(
                    LedAnimations.SWITCH,
                    LedElements.BUMPER2,
                    LedColor(199, 190, 190),
                    LedColor(0, 0, 0),
                    1000,
                )
            )
        elif c == "6":
            manager.send_event(
                LedEvent(
                    LedAnimations.SWITCH,
                    LedElements.BUMPER3,
                    LedColor(199, 190, 190),
                    LedColor(0, 0, 0),
                    1000,
                )
            )
        elif c == "7":
            manager.send_event(
                LedEvent(
                    LedAnimations.BLINK,
                    LedElements.BUMPER3,
                    LedColor(0, 255, 0),
                    LedColor(255, 0, 0),
                    10,
                )
            )
