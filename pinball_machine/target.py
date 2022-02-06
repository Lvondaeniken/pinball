class Target:
    def __init__(self, id: int, leds: list):
        self.id = id
        self.state = False
        self.leds = leds

    def reset(self):
        self.state = False

    def update(self):
        self.state = not self.state

if __name__=='__main__':
    t = Target(1, 3)
    print(t.state)
    t.update(0)
    print(t.state)

    