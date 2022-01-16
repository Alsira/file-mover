import threading
from math import pow

def Transfer(src_dir: str, dest_dir: str, write: list, lock: threading.Lock) -> int:

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
        