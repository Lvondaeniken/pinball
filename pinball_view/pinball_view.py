from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import Sound, SoundLoader
from kivy.clock import Clock
from screen_highscore import HighscoreScreen
from screen_start import StartScreen
from screen_settings import SettingsScreen
from screen_play import PlayScreen

import multiprocessing as mp

Builder.load_file('kv_files/settings.kv')
Builder.load_file('kv_files/highscore.kv')
Builder.load_file('kv_files/start.kv')

class PinballView(App):
    def __init__(self, queue):
        super(PinballView, self).__init__()
        self.queue = queue
        #Clock.schedule_interval(self.queue_listener, 0.5)

    def build(self):
        # Create the screen manager
        print("slksjdflskdfj")
        self.sm = ScreenManager()
        self.sm.add_widget(HighscoreScreen(name='highscore'))
        self.sm.add_widget(SettingsScreen(name='settings'))
        self.sm.add_widget(StartScreen(name='start'))
        self.sm.add_widget(PlayScreen(name='play'))
        return self.sm

    def play(self):
        self.sm.current = 'play'
        sound = SoundLoader.load('media/can-open-3.wav').play()
        SoundLoader.load('media/pouring.wav').play()

    def queue_listener(self, dt):
        pass        

if __name__ == '__main__':
    q = mp.Queue()
    p = PinballView(q)
    p.run()
