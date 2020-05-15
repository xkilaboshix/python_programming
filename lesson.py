import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(d, lock):
    with lock:
        i = d['x']
        time.sleep(2)
        d['x'] = i + 1
    logging.debug(d)

def worker2(d, lock):
    with lock:
        i = d['x']
        time.sleep(2)
        d['x'] = i + 1
    logging.debug(d)

if __name__ == '__main__':
    d = {'x': 0}
    lock = multiprocessing.Lock()
    t1 = multiprocessing.Process(target=worker1, args=(d, lock))
    t2 = multiprocessing.Process(target=worker1, args=(d, lock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    logging.debug(d)
    # with multiprocessing.Pool(3) as p:
    #     r = p.imap(worker1, [100, 200])
    #     logging.debug('executed')
    #     for i in r:
    #         logging.debug(i)

        # p1 = p.apply_async(worker1, (100, ))
        # p2 = p.apply_async(worker1, (100, ))
        # logging.debug('executed')
        # logging.debug(p1.get())
        # logging.debug(p2.get())


