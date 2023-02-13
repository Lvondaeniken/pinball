import socket
from typing import Optional
from events.event_factory import get_event_from_string
from events.events import PinballEvent
import config.cfg as cfg


class HardwareListener:
    def __init__(self) -> None:
        self.client_connected: bool = False
        self.s = socket.socket()
        self.s.bind((cfg.HOST, cfg.PORT))
        self.s.listen(5)

    def connect(self) -> None:
        """blocking connection attempt"""
        self.con, addr = self.s.accept()
        print("got connection from addr -> ", addr)

    def send(self, cmd: str):
        self.con.send(cmd.encode())

    def get_event(self) -> Optional[PinballEvent]:
        data = self.con.recv(1024).decode("utf-8")
        event = get_event_from_string(data)
        if event:
            return event
        else:
            return None


if __name__ == "__main__":
    listener = HardwareListener()
    listener.connect()
    while True:
        listener.listen()
