import socket
import cmd
import config.cfg as cfg
import time

RETRY_INTERVAL = 5
ERR_MSG = f"Failed to connect to server,\
    retrying in {RETRY_INTERVAL} seconds..."


class AppInterface:
    def __init__(self):
        self.s = socket.socket()
        self.connect()

    def connect(self) -> None:
        while True:
            try:
                self.s.connect((cfg.HOST, cfg.PORT))
                print("Connected to server successfully!")
                return
            except ConnectionRefusedError:
                print(ERR_MSG)
                time.sleep(RETRY_INTERVAL)

    def send(self, code: str) -> None:
        self.s.send(code.encode())

    def close(self) -> None:
        print("closing testapp")
        self.s.send("exit".encode())
        self.s.close()
        self.stop()


class TestCli(cmd.Cmd):
    prompt: str = "pinball:$ "
    intro: str = "Welcome to pinball harware mock test app"

    def __init__(self):
        super().__init__(self)
        self.host = AppInterface()
        self.host.connect()

    def do_b1(self):
        """Bumper 1 Event"""
        self.host.send("b1")

    def do_b2(self):
        """Bumper 2 Event"""
        self.host.send("b2")

    def do_b3(self):
        """Bumper 3 Event"""
        self.host.send("b3")

    def do_kl(self):
        """Kicker Left Event"""
        self.host.send("kl")

    def do_kr(self):
        """Kicker Right Event"""
        self.host.send("kr")

    def do_bs(self):
        """Ballshooter Event"""
        self.host.send("bs")

    def do_t1(self):
        """Target 1 Event"""
        self.host.send("t1")

    def do_t2(self):
        """Target 2 Event"""
        self.host.send("t2")

    def do_t3(self):
        """Target 3 Event"""
        self.host.send("t3")


if __name__ == "__main__":
    TestCli().cmdloop()
