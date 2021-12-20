import multiprocessing
import time

def worker(conn):
    print(conn.recv())
    conn.send("sent from child process")
    time.sleep(1)
    conn.send("sent from child process")
    time.sleep(1)
    conn.send("sent from child process")
    
if __name__=='__main__':
    conn1, conn2 = multiprocessing.Pipe()
    process = multiprocessing.Process(target=worker, args=[conn2])
    process.start()

    conn1.send("sent from main process")
    while True:
        print(conn1.recv())

