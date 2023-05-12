from kivy.uix.image import Image
from enum import Enum, auto

atlas_file = "atlas://view/media/Beer-Complete-Spritesheet/frame"

FRAMES = 21

MIDDLE_X = -180

class BeerState(Enum):
    MOVE_MIDDLE = auto()
    FILL = auto()
    MOVE_LEFT = auto()
    DONE = auto()


class Beer(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.frame = 1
        self.full = False
        self._update()
        self.y = 215
        self.x = MIDDLE_X + 2000
        self.state = BeerState.MOVE_MIDDLE

    def update(self):
        if self.state == BeerState.MOVE_MIDDLE:
            self.move_left()
            if self.x == -180:
                self.state = BeerState.FILL

        elif self.state == BeerState.FILL:
            self.fill()
            if self.is_full():
                self.state = BeerState.MOVE_LEFT

        elif self.state == BeerState.MOVE_LEFT:
            self.move_left()
            if self.x == MIDDLE_X -2000:
                self.state = BeerState.DONE
        else:
            pass

    def fill(self):
        if self.is_full():
            return
        self.frame = self.frame + 1
        self._update()
        if self.frame == FRAMES:
            self.full = True
        print(self.frame)

    def is_full(self) -> bool:
        return self.full

    def _update(self):
        print("update")
        self.source = atlas_file + str(self.frame)

    def move_left(self):
        self.x -= 50
