from kivy.app import App

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import Sound, SoundLoader
from kivy.clock import Clock
from events.gui_events import GuiEventType
from view.screens.screen_end_info_1 import *
from view.screens.event_displayer import *
from view.screens.collecting import Collecting

import multiprocessing as mp
import time

Builder.load_file("view/screens/kv_files/end_screen_1.kv")
Builder.load_file("view/screens/kv_files/event_displayer.kv")
Builder.load_file("view/screens/kv_files/collecting.kv")
# Builder.load_file('view/kv_files/settings.kv')
# Builder.load_file('view/kv_files/highscore.kv')
# Builder.load_file('view/kv_files/start.kv')
# Builder.load_file('view/kv_files/play.kv')


class PinballView(App):
    def __init__(self, queue: mp.Queue):
        super(PinballView, self).__init__()
        self.queue = queue

    def build(self):
        # Create the screen manager
        self.sm = ScreenManager()
        self.screens = {
            "end": EndInfo1Screen(name="end"),
            "info": EventDisplayer(name="info"),
            "collecting": Collecting(name="collecting"),
        }

        for screen in self.screens.values():
            self.sm.add_widget(screen)
        Clock.schedule_interval(self.queue_listener, 0.02)
        self.sm.switch_to(self.screens["end"])
        return self.sm

    def play(self):
        sound = SoundLoader.load("media/can-open-3.wav").play()
        SoundLoader.load("media/pouring.wav").play()

    def queue_listener(self, dt):
        if self.queue.empty():
            return
        event: GuiEvent = self.queue.get(False)

        if event.event == GuiEventType.START_FINAL_MODE:
            self.sm.switch_to(self.screens["collecting"])
        else:
            self.screens[self.sm.current].handleEvent(event)


if __name__ == "__main__":
    p = PinballView(mp.Queue())
    p.run()
