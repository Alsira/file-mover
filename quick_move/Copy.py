import threading
from math import pow

def copy_dir(dirs: list, write: list, lock: threading.Lock) -> list:

    # These are the files that failed the copy
    failed_copy = list()

    for item in dirs:
        result = copy(item[0], item[1], write, lock)
        
        # if the amount written was 0 or less
        if result <= 0:
            failed_copy.append(item[0])

    return failed_copy

def copy(src_dir: str, dest_dir: str, write: list, lock: threading.Lock) -> int:

    try:

        src_file  = open(src_dir, 'rb')
        dest_file = open(dest_dir, 'wb')

        buffer = int(pow(1024, 2) * 50)
        data   = src_file.read(buffer)
        while len(data) > 0:
            
            lock.acquire()
            write[0] += dest_file.write(data)
            lock.release()

            data = src_file.read(buffer)
            
        src_file.close()
        dest_file.close()
        
        return write[0]
    
    except IOError:

        return -1
        