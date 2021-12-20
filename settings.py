from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file('settings.kv')

# Declare both screens
class HighscoreScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class StartScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(HighscoreScreen(name='highscore'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(StartScreen(name='start'))

        return sm

if __name__ == '__main__':
    TestApp().run()