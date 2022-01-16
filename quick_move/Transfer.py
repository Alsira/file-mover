import ctypes
import threading

def Transfer(src_dir: str, dest_dir: str, write, lock: threading.Lock) -> int:

    return_value: int

    try:

        src_file  = open(src_dir, 'rb')
        dest_file = open(dest_dir, 'wb')

        buffer = 1024
        data   = src_file.read(buffer)
        while len(data) > 0:
            
            lock.acquire()
            write[0] += dest_file.write(data)
            lock.release()

            data = src_file.read(buffer)

        return_value = write[0]
    
    except:

        return_value = -1
    
    finally:

        src_file.close()
        dest_file.close()
        if lock.locked():
            lock.release()

        return return_value
        