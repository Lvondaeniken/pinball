from kivy.app import App
import socket
import config.cfg as cfg
import time

# set the time interval between connection attempts (in seconds)
RETRY_INTERVAL = 5


class TestApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.s = socket.socket()
        self.connect()

    def connect(self) -> None:
        while True:
            try:
                self.s.connect((cfg.HOST, cfg.PORT))
                print('Connected to server successfully!')
                return
            except ConnectionRefusedError:
                # if the connection was refused, wait for a bit before trying again
                print('Failed to connect to server, retrying in {} seconds...'.format(RETRY_INTERVAL))
                time.sleep(RETRY_INTERVAL)

    def send(self, code: str) -> None:
        self.s.send(code.encode())

    def close(self) -> None:
        print("closing testapp")
        self.s.send("exit".encode())
        self.s.close()
        self.stop()


if __name__ == "__main__":
    TestApp().run()
