class Target:
    def __init__(self, id: int, size: int, leds: list):
        self.id = id
        self.state = []
        self.size = size
        self.leds = leds
        self.reset()

    def reset(self):
        for i in range(self.size):
            self.state.append(False)

    def update(self, i: int):
        self.state[i] = not self.state[i]


if __name__=='__main__':
    t = Target(1, 3)
    print(t.state)
    t.update(0)
    print(t.state)

    