
from rpi_ws281x import PixelStrip, Color
TIMEBASE_MS = 200

class LedTest:
    def startup(self):
        self.led_count = 18  # Number of LED pixels.
        self.led_pin = 18  # GPIO pin connected to the pixels (18 uses PWM!).
        # LED signal frequency in hertz (usually 800khz)
        self.led_freq_hz = 800000
        self.led_dma = 10  # DMA channel to use for generating signal (try 10)
        self.led_brightness = 250  # Set to 0 for darkest and 255 for brightest
        # True to invert the signal (when using NPN transistor level shift)
        self.led_invert = False
        self.led_channel = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        self.strip = PixelStrip(self.led_count, self.led_pin, self.led_freq_hz,
                                    self.led_dma, self.led_invert, self.led_brightness, self.led_channel)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

    def run(self):
        for i in range(15):
            self.strip.setPixelColor(i, Color(100, 100, 100))
        self.strip.show()
        while True:
            pass

if __name__=="__main__":
    l = LedTest()
    l.startup()
    l.run()