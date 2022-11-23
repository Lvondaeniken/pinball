
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class EndInfo1Screen(Screen):
    def __init__(self, *args, **kwargs):
        super(EndInfo1Screen, self).__init__(*args, **kwargs)
        for l in self.ids.items():
            id, label = l 
            if id == 'lb0':
                label.text ="hello"




