import socket
from cmd import Cmd
import config.cfg as cfg


class PinballTester(Cmd):
    intro = "Welcome to Pinball Tester"
    prompt = ">>"

    def do_connect(self, _):
        self.s = socket.socket()
        self.s.connect((cfg.HOST, cfg.PORT))

    def do_close(self, _):
        self.s.close()

    def do_b1(self, _):
        self.s.send("b1".encode())

    def do_b2(self, _):
        self.s.send("b2".encode())

    def do_b3(self, _):
        self.s.send("b3".encode())

    def do_t1(self, _):
        self.s.send("t1".encode())

    def do_t2(self, _):
        self.s.send("t2".encode())

    def do_t3(self, _):
        self.s.send("t3".encode())

    def do_kl(self, _):
        self.s.send("kl".encode())

    def do_kr(self, _):
        self.s.send("kr".encode())

    def do_bs(self, _):
        self.s.send("bs".encode())


if __name__ == "__main__":
    PinballTester().cmdloop()
