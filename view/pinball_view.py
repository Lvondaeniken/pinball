from kivy.app import App

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import Sound, SoundLoader
from kivy.clock import Clock
from view.screen_highscore import HighscoreScreen
from view.screen_start import StartScreen
from view.screen_settings import SettingsScreen
from view.screen_play import PlayScreen

import multiprocessing as mp
import time

Builder.load_file('view/kv_files/settings.kv')
Builder.load_file('view/kv_files/highscore.kv')
Builder.load_file('view/kv_files/start.kv')
Builder.load_file('view/kv_files/play.kv')

class PinballView(App):
    def __init__(self, queue: mp.Queue):
        super(PinballView, self).__init__()
        self.queue = queue 

    def build(self):
        # Create the screen manager
        self.sm = ScreenManager()
        self.screens = [HighscoreScreen(name='highscore'), SettingsScreen(name='settings'), StartScreen(name='start'), PlayScreen(name='play')]
        for screen in self.screens:
            self.sm.add_widget(screen)
        Clock.schedule_interval(self.queue_listener, 0.02)
        self.sm.switch_to(self.screens[0])
        return self.sm

    def play(self):
        sound = SoundLoader.load('media/can-open-3.wav').play()
        SoundLoader.load('media/pouring.wav').play()

    def queue_listener(self, dt):
        if not self.queue.empty():
            input = self.queue.get(False)
            if input == 'go_left':
                self.go_right()    
            elif input == 'go_right':
                self.go_right()

    def go_left(self):
        current = self.sm.current
        if current == 'highscore':
            self.sm.switch_to(self.screens[2])
        elif current == 'settings':
            self.sm.switch_to(self.screens[0])            
        elif current == 'start':
            self.sm.switch_to(self.screens[1])            

    def go_right(self):
        current = self.sm.current
        if current == 'highscore':
            self.sm.switch_to(self.screens[1])
        elif current == 'settings':
            self.sm.switch_to(self.screens[2])            
        elif current == 'start':
            self.sm.switch_to(self.screens[0])

    def iterate_menu(self):
        pass


if __name__ == '__main__':
    p = PinballView(mp.Queue())
    p.run()