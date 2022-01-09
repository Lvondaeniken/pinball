import multiprocessing as mp
import time
def pinball_listener(queue):
    while True:
        queue.put('highscore')
        time.sleep(3)
        queue.put('settings')
        time.sleep(3)
        queue.put('start')
        time.sleep(3)
        queue.put('play')
        time.sleep(3)

if __name__ == '__main__':
    queue = mp.Queue()
    pinball_listener(queue)