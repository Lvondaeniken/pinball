from kivy.uix.screenmanager import Screen

from events.gui_events import GuiEventType, GuiEvent

MAX_LOG = 10


class EventDisplayer(Screen):
    def __init__(self, *args, **kwargs):
        super(EventDisplayer, self).__init__(*args, **kwargs)
        self.log = []

    def handle_event(self, event: GuiEvent) -> None:
        if event.event != GuiEventType.HARDWARE_LOG:
            return
        print("received event")
        self.log.insert(0, f"{event.event=}\n {event.src=}")
        if len(self.log) > MAX_LOG:
            self.log = self.log[0:MAX_LOG]

        out = ""
        for x in self.log:
            out += x + "\n"
        self.ids["evt"].text = out
