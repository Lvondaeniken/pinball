import led.elements
import events.events

EVENT_ELEMENT_TO_LED_ELEMENT = {
    events.EventElement.BUMPER1: elements.LedElements.BUMPER1,
    events.EventElement.BUMPER2: elements.LedElements.Bumper2,
    events.EventElement.BUMPER3: elements.LedElements.Bumper3,
    events.EventElement.TARGET1: elements.LedElements.TARGET1,
    events.EventElement.TARGET2: elements.LedElements.TARGET2,
    events.EventElement.TARGET3: elements.LedElements.TARGET3,
}

def led_on_event(target):
    if target in EVENT_ELEMENT_TO_LED_ELEMENT.keys():
        return led.LedEvent(t)
