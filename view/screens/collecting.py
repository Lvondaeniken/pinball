from kivy.uix.screenmanager import Screen
from events.gui_events import GuiEventType, GuiEvent
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from view.screens.beer_gif import Beer
from kivy.lang import Builder
import time

kv_files = ["collecting.kv", "balls_widget.kv", "multiplier_widget.kv", "score_widget.kv"]

for file in kv_files:
    Builder.load_file(f"view/screens/kv_files/collecting_screen/{file}")


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
