from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from events.gui_events import GuiEventType, GuiEvent
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.clock import Clock
import time

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


class Collecting(Screen):
    beer1 = ObjectProperty(None)
    beer2 = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(Collecting, self).__init__(*args, **kwargs)
        self.bottle_count = 0
        Clock.schedule_interval(self.update, 0.02)
        self.end = time.time() + 30

    def update(self, dt):
        self.beer1.update(dt)
        self.beer2.update(dt)
        self.ids["title"].text = (
            f"Brew as much as you can!\n" f"{round(self.end -time.time())} seconds left"
        )

    def handle_event(self, event: GuiEvent) -> None:
        print("bottle collected ")
        if event.event == GuiEventType.ADD_BOTTLE:
            self.bottle_count += 1
            self.update_text()

    def update_text(self):
        self.ids["bottles"].text = f"{self.bottle_count} collected bottles"
