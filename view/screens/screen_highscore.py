from view.highscore_db import Highscore
from kivy.uix.screenmanager import Screen


class HighscoreScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(HighscoreScreen, self).__init__(*args, **kwargs)
        self.highscoreData = Highscore()
        self.update_highscorelist()
        print("hello")

    def update_highscorelist(self):
        i = 0
        print("lets update")
        for id in self.ids.items():
            _, label = id
            if len(self.highscoreData.get()) > i:
                label.text = f"{self.highscoreData.get()[i].name} : {self.highscoreData.get()[i].score}"
            i += 1

    def do_something(self):
        print("im doing something")
