import multiprocessing as mp
import time
def pinball_listener(queue):
    pass
    while True:
        time.sleep(1)
        queue.put("show highscore")
        time.sleep(2)
        queue.put("show start")
        
if __name__ == '__main__':
    queue = mp.Queue()
    pinball_listener(queue)