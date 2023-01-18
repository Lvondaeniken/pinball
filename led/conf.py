from led.led_event import LedElements
from led.led_group import LedGroup

TIMEBASE_MS = 20

LED_GROUPS = {
    LedElements.BALLSHOOTER: LedGroup(10, TIMEBASE_MS),
    LedElements.PIPES: LedGroup(12, TIMEBASE_MS),
    LedElements.BOTTLE: LedGroup(1, TIMEBASE_MS),
    LedElements.BUMPER1: LedGroup(3, TIMEBASE_MS),
    LedElements.BUMPER2: LedGroup(3, TIMEBASE_MS),
    LedElements.BUMPER3: LedGroup(3, TIMEBASE_MS),
    LedElements.TARGET1: LedGroup(3, TIMEBASE_MS),
    LedElements.TARGET2: LedGroup(3, TIMEBASE_MS),
    LedElements.TARGET3: LedGroup(3, TIMEBASE_MS),
}
