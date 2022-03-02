class LedColor:
    def __init__(self, red, green, blue, brightness=100):
        self.red = red
        self.green = green
        self.blue = blue
        self.brightness = brightness

    def __str__(self):
        return f"{self.red}, {self.green}, {self.blue}, {self.brightness}"