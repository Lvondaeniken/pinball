from cmd import Cmd
from serial.serialwin32 import Serial

class cli(Cmd):
    def do_connect(self, arg):
        """open serial connection"""
        self.ser = Serial(port='COM10', baudrate=9600)

    def do_disconnect(self, arg):
        """close serial connection"""
        self.ser.close()

    def do_b1(self, arg):
        """bumper 1 hit event"""
        self.send_serial("b1")

    def do_b2(self, arg):
        """bumper 2 hit event"""
        self.send_serial("b2")
    
    def do_b3(self, arg):
        """bumper 3 hit event"""
        self.send_serial("b3")
    
    def do_t1(self, arg):
        """target 1 hit event"""
        self.send_serial("t1")

    def do_t2(self, arg):
        """target 2 hit event"""
        self.send_serial("t2")    

    def do_t3(self, arg):
        """target 3 hit event"""
        self.send_serial("t3")    
    
    def send_serial(self, msg:str):
        msg+= "\n\r"
        self.ser.write(msg.encode())


if __name__=='__main__':
    c = cli()
    c.cmdloop()
    