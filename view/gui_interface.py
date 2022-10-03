from multiprocessing import Queue
from events.gui_events import GuiEvent, GuiEventType
class GuiInterface:
    def __init__(self, queue: Queue) -> None:
        self.view_queue = queue
        
    def go_left(self):
        event = GuiEvent(event=GuiEventType.LEFT)
        self.queue.put(event)
        
    def go_right(self):
        event = GuiEvent(event=GuiEventType.RIGHT)
        self.queue.put(event)

    def reset(self):
        event = GuiEvent(event=GuiEventType.RESET)
        self.queue.put(event)