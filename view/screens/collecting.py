from events.events import EventElement, PinballEvent, EventType
from kivy.uix.screenmanager import Screen
from events.gui_events import GuiEventType, GuiEvent
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from view.screens.beer_gif import Beer
from kivy.lang import Builder
import multiprocessing as mp
import time
import multiprocessing as mp
from kivy.lang import Builder


kv_files = [
    "collecting.kv",
    "balls_widget.kv",
    "multiplier_widget.kv",
    "score_widget.kv",
]

for file in kv_files:
    Builder.load_file(f"view/screens/kv_files/collecting_screen/{file}")
atlas_file = "atlas://view/media/beer/frame"


class Collecting(Screen):
    beer1 = ObjectProperty(None)
    beer2 = ObjectProperty(None)

    def __init__(self, to_logic: mp.Queue, *args, **kwargs):
        super(Collecting, self).__init__(*args, **kwargs)
        self.bottle_count = 0
        self.update_event = Clock.schedule_interval(self.update, 0.02)
        self.end = time.time() + 30
        self.to_logic = to_logic
        self.score = 0
        self.multiplier = 1

    def update(self, dt):
        self.beer1.update(dt)
        self.beer2.update(dt)
        time_left = round(self.end - time.time())
        if time_left == 0:
            print("GUI -> put timeover event")
            self.to_logic.put(
                PinballEvent(element=EventElement.GUI, type=EventType.TIME_OVER)
            )
            Clock.unschedule(self.update_event)
            self.ids.title.text = "TIME OVER"
        else:
            self.ids["title"].text = (
                f"Brew as much as you can!\n" f"{time_left} seconds left"
            )

    def handle_event(self, event: GuiEvent) -> None:
        print("bottle collected ")
        if event.event == GuiEventType.ADD_BOTTLE:
            self.bottle_count += event.src
            self.update_text()
        elif event.event == GuiEventType.BONUS_TIME:
            self.end += event.src
        elif event.event == GuiEventType.ALL_BOTTLES_COLLECTED:
            self.ids["title"].text = "All parts hit!!!!"
            Clock.unschedule(self.update_event)
        elif event.event == GuiEventType.NOT_ENOUGH_BOTTLES:
            self.ids["title"].text = "TIME OVER MISSION FAILED"
            Clock.unschedule(self.update_event)

    def update_text(self):
        self.ids["bottles"].text = f"{self.bottle_count} collected bottles"
        self.set_score()
        self.set_multiplier()

    def set_score(self):
        self.ids.score_widget.ids.label.text = str(self.score)

    def set_multiplier(self):
        self.ids.multiplier_widget.ids.label.text = str(self.multiplier)
