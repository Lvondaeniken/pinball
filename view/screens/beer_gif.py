from kivy.uix.image import Image

atlas_file = "atlas://view/media/beer/frame"


class Beer(Image):
    time = 0.0
    rate = 0.1
    frame = 25

    def update(self, dt):
        self.time += dt
        if self.time > self.rate:
            self.time -= self.rate
            self.source = atlas_file + str(self.frame)
            self.frame = self.frame - 1
            if self.frame == 0:
                self.frame = 25

