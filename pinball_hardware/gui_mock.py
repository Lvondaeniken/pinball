from kivy.app import App
import socket
import config.cfg as cfg


class TestApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.s = socket.socket()
        self.s.connect((cfg.HOST, cfg.PORT))

    def send(self, code: str) -> None:
        self.s.send(code.encode())

    def close(self) -> None:
        self.s.close()
        self.stop()


if __name__ == "__main__":
    TestApp().run()
