from kivy.uix.image import Image

atlas_file = "atlas://view/media/Beer-Complete-Spritesheet@2x/frame"


class Beer(Image):
    time = 0.0
    rate = 0.1
    frame = 1

    def update(self, dt):
        self.time += dt
        if self.time > self.rate:
            self.time -= self.rate
            self.source = atlas_file + str(self.frame)
            self.frame = self.frame + 1
            if self.frame == 22:
                self.frame = 1

