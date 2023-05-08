from os import walk
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Builder.load_file("view/screens/kv_files/final/final_layout.kv")

kv_files = [
    "balls_widget.kv",
    "multiplier_widget.kv",
    "score_widget.kv",
]

for file in kv_files:
    Builder.load_file(f"view/screens/kv_files/collecting_screen/{file}")


class FinalLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        height = self.ids.img1.texture_size[1]
        self.ids.img1.y = self.ids.img1.y / 2 + height / 2
        self.ids.img2.y = self.ids.img2.y / 2 + height / 2


class Test(App):
    def build(self):
        Config.set("graphics", "width", 1920)  # sets the width to 1920 px
        Config.set("graphics", "height", 1080)  # sets the height to 1080 px
        return FinalLayout()


if __name__ == "__main__":
    Test().run()
