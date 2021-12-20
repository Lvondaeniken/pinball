from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.image import Image

from kivy.clock import Clock
from kivy.core.audio import Sound, SoundLoader
import multiprocessing
import time

class MyMenu(BoxLayout):
    def add_queue(self, queue):
        self.queue = queue
        self.sound = SoundLoader.load('shotgun.wav')
        self.points = 0
        print("pipe is added")
        Clock.schedule_interval(self.check_inputs, 0.5)
        
    def test(self):
        self.ids.image1.source= "bier.jpg"  
        self.ids.image2.source= "bier.jpg"  
        self.ids.image3.source= "bier.jpg"  
        self.ids.image4.source= "bier.jpg"  
        self.ids.image5.source= "bier.jpg"  
        self.ids.image6.source= "bier.jpg"  
        self.ids.image7.source= "bier.jpg"  
        self.ids.image8.source= "bier.jpg"  
        self.ids.image9.source= "bier.jpg"  
        print("loading-....")
        self.sound = SoundLoader.load('can-open-3.wav')
        self.sound.play()
        self.sound = SoundLoader.load('pouring.wav')
        print("Sound found at %s" % self.sound.source)
        print("Sound is %.3f seconds" % self.sound.length)
        self.sound.play() 

    def update(self):
        self.toggle_image()
        self.points = 0

    def check_inputs(self, dt):
        if not self.queue.empty():
            self.points += int(self.queue.get())
            print("katisching")

        self.ids.score.text = f'score: {self.points}'
        

class PinballApp(App):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def build(self):
        m = MyMenu()
        m.add_queue(self.queue)
        return m

def gui(queue):
    PinballApp(queue).run()

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=gui, args=[queue])
    process.start()
    while True:
        queue.put(input("->"))

