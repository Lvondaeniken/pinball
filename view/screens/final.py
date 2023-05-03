from os import walk
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

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


class Test(App):
    def build(self):
        return FinalLayout()


if __name__ == "__main__":
    Test().run()
