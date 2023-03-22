from kivy.uix.screenmanager import Screen
from events.gui_events import GuiEventType, GuiEvent
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import time

atlas_file = "atlas://view/media/beer/frame"


class Multiplier(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="MULTIPLIER"))
        self.add_widget(Label(text="000", font_size=100))


class Score(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="SCORE"))
        self.add_widget(Label(text="000000000", font_size=100))


class Balls(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="BALLS"))
        self.add_widget(Label(text="0/0", font_size=100))


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
        self.update_event = Clock.schedule_interval(self.update, 0.02)
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
        elif event.event == GuiEventType.BONUS:
            self.end += 5
        elif event.event == GuiEventType.ALL_PARTS_HIT:
            self.ids["title"]. text = "All parts hit!!!!"
            Clock.unschedule(self.update_event)

    def update_text(self):
        self.ids["bottles"].text = f"{self.bottle_count} collected bottles"
