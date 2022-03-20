from multiprocessing import Process, Queue
from time import sleep
from led_group import LedGroup
from blinking import BlinkingLight
from rpi_ws281x import PixelStrip, Color
from led_color import LedColor
from led_switch import LedSwitch
from led_event import LedEvent, LedAnimations, LedElements

# LED strip configuration:
LED_COUNT = 36        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


class LedManager(Process):
    def startup(self, timebase_ms):
        self.timebase_ms = timebase_ms
        self.toManager = Queue()
        self.fromManager = Queue()
        self.start()

    def send_event(self, event: LedEvent):
        self.toManager.put(event)


    def run(self):
        self.bumper1 = LedGroup(12)
        self.bumper2 = LedGroup(12) 
        self.bumper3 = LedGroup(12) 
        self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()
    
        while True:
            sleep(self.timebase_ms/1000)
            self.check_new_events()
            self.update_strip()
                
    def update_strip(self):
        next_frame = []
        next_frame.extend(self.bumper1.get_next_frame())
        next_frame.extend(self.bumper2.get_next_frame())
        next_frame.extend(self.bumper3.get_next_frame())
        for i in range(len(next_frame)): 
            c = Color(next_frame[i].red, next_frame[i].green, next_frame[i].blue)
            self.strip.setPixelColor(i, c)
            self.strip.show()

    def check_new_events(self):
        while not self.toManager.empty():
            event = self.toManager.get()
            if event.target == LedElements.BUMPER1:
                if event.animation == LedAnimations.SWITCH:
                    self.bumper1.add_animation(LedSwitch(event.color, 12))
            elif event.target == LedElements.BUMPER2:
                if event.animation == LedAnimations.SWITCH:
                    self.bumper2.add_animation(LedSwitch(event.color, 12))
            elif event.target == LedElements.BUMPER3:
                if event.animation == LedAnimations.SWITCH:
                    self.bumper3.add_animation(LedSwitch(event.color, 12))
                elif event.animation == LedAnimations.BLINK:
                    self.bumper3.add_animation(BlinkingLight(self.timebase_ms, 10, 1, 12, event.color, event.background))

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