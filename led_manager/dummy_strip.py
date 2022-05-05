class DummyStrip():
    def begin(self):
        print("it begins ;)")

    def setPixelColor(self, index, color):
        print(f'changing color of index {index}')

    def show(self):
        pass

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.b = b
        self.g = g


