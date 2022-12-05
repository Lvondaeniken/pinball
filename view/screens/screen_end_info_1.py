from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from events.gui_events import GuiEventType, GuiEvent

text1 = (
    "Das Bier ist bereit abgezapft zu werden.\n"
    "Treffe möglichst viele beliebige Elemente\n"
    "bevor die Zeit abläuft um das Ziel von 200\n"
    "Flaschen zu erreichen!"
)

text2 = (
    "Diese Spielelemente geben dir folgende Flaschen:\n"
    "- Kessel - 1 Flasche\n"
    "- Ramp - 3 Flaschen\n"
    "- Bumper - 1 Flasche\n"
    "- Target - 2 Flaschen\n"
    "- Kickhole - 5 Flaschen\n"
    "Zusätzliche 20 Flaschen\n"
    "wenn alle Elemente 1x getroffen wurden.\n"
    "+ 5 Sek. Zeit auf Countdown."
)
text3 = "OKAY LET'S GO"
txt = [text1, text2, text3]


class EndInfo1Screen(Screen):
    def __init__(self, *args, **kwargs):
        super(EndInfo1Screen, self).__init__(*args, **kwargs)
        self.txt_index = 0
        for l in self.ids.items():
            id, label = l
            if id == "lb0":
                label.text = txt[self.txt_index]
            if id == "btn0":
                label.bind(on_press=self.cb)
                label.text = "Für weiter, Balltaste am unteren Tischrand betätigen"

    def cb(self, i):
        self.txt_index += 1
        if self.txt_index == len(txt):
            self.txt_index = 0
        self.ids["lb0"].text = txt[self.txt_index]

    def handleEvent(self, event: GuiEvent) -> None:
        print("received event")
        if event.event == GuiEventType.SHOW_FINAL_INFO_1:
            self.ids["lb0"].text = txt[0]
        elif event.event == GuiEventType.SHOW_FINAL_INFO_2:
            self.ids["lb0"].text = txt[1]
        elif event.event == GuiEventType.SHOW_FINAL_INFO_3:
            self.ids["lb0"].text = txt[2]
