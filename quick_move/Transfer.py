import threading
from math import ceil

from . import Copy

def transfer(copy_dirs: list, queues: int, bytes: list, lock: threading.Lock) -> None:

    count = 0 # This is the current index of the start of the slice
    per_thread_dir = ceil(len(copy_dirs) / queues) if int(len(copy_dirs) / queues) else 1 # The number of dirs per copy thread

    dir_size = len(copy_dirs)

    threads = list()

    # Loop and load threads
    for _ in range(queues):

        end_range = count + per_thread_dir if count + per_thread_dir <= dir_size else dir_size 

        # Start the thread
        t = threading.Thread(target=Copy.copy_dir, args=(copy_dirs[count:end_range], bytes, lock))
        t.setDaemon(True)
        t.start()

        threads.append(t)

        count += per_thread_dir

    # wait for each thread to join
    for thread in threads:
        thread.join()
    
        