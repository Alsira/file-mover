import threading
import progressbar

async def cli(written, lock: threading.Lock(), max_size: int):

    # Create the progress bar
    widgets = [
        "Transfered ",
        progressbar.Percentage(),
        ' ',
        progressbar.Bar(marker=progressbar.RotatingMarker()),
        ' ',
        progressbar.FileTransferSpeed(),
        ' ',
        progressbar.AdaptiveETA()
    ]

    pbar = progressbar.ProgressBar(widgets=widgets, maxval=max_size)
    
    pbar.start()

    # So we can quickly release the lock
    lock.acquire()
    write_copy = written[0]
    lock.release()

    while write_copy < max_size:

        # Update the bar
        pbar.update(write_copy)

        # Quickly acquire and release the lock
        lock.acquire()
        write_copy = written[0]
        lock.release()
    
    if lock.locked():
        lock.release()
    pbar.finish()




