from kivy.app import App
from kivy.lang import Builder
from screen_end_info_1 import EndInfo1Screen

Builder.load_file("kv_files/end_screen_1.kv")


class ShowApp(App):
    def build(self):
        return EndInfo1Screen()


if __name__ == "__main__":
    ShowApp().run()
