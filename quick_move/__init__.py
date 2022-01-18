import os
import sys
import threading
from math import pow


# Local
from . import DirList
from . import cli
from . import Hash
from . import Transfer

def Calcualate_Size(bytes: int) -> str:

    if bytes < 1024:
        return ' '.join([str(bytes), 'B'])
    
    elif bytes < pow(1024, 2):
        return ' '.join([str(bytes // 1024), 'KB'])
    
    elif bytes < pow(1024, 3):
        return ' '.join([str(bytes // pow(1024, 2)), 'MB'])
    
    elif bytes < pow(1024, 4):
        return ' '.join([str(bytes // pow(1024, 3)), 'GB'])
    
    elif bytes < pow(1024, 5):
        return ' '.join([str(bytes // pow(1024, 4)), 'PB'])

    else:
        return "A LOT OF DATA!" 



# Do something here
def program():

    argv = sys.argv
    argc = len(argv)

    # Need at least two directories or files
    if (argc < 3):
        sys.stderr.write('ERROR : Not enough arguments\n')
        sys.exit(-1)
    
    source = argv[1]
    dest   = argv[2]

    # Stuff here is used for UI
    # Number of bytes
    bytes_written = [0]
    byte_lock     = threading.Lock()

    # These are the source directories to write and where to write as tuples (src, dest)
    files_to_write = list()

    if os.path.isfile(source):

        # File doesn't exist, so write
        if not os.path.exists(dest):
            files_to_write.append((source, dest))
        
        else:
            
            h1 = Hash.hashFile(source)
            h2 = Hash.hashFile(dest)

            if h1 != h2:
                files_to_write.append((source, dest))

    elif os.path.isdir(source):
        
        # Create the lists (relative paths)
        print('Searching ' + source + '...')
        src_dir_list  = DirList.CreateDirMap(source) 
        dest_dir_list = list()

        # Handle Dest Directory
        if os.path.exists(dest):
            print('Searching ' + dest + '...')
            dest_dir_list = DirList.CreateDirMap(dest)

        else:
            os.mkdir(dest)
            print('Created directory ' + dest)

        # Remove the beginning directory
        src_dir_list = [dir[len(source) + 1:] for dir in src_dir_list]
        dest_dir_list = [dir[len(dest) + 1:] for dir in dest_dir_list]

        print("Finding modified files...")
        
        # Iterate through each path and detect files that need to be replaced (Also create the nessary folders)
        for src_path in src_dir_list:

            # Paths with directory at the front
            abs_src_path  = '/'.join([source, src_path])
            abs_dest_path = '/'.join([dest, src_path]) 

            # If both paths exists (This is why the top directory is removed from the list)
            if src_path in dest_dir_list:

                # If this is a file
                if os.path.isfile(abs_src_path):
                    
                    h1 = Hash.hashFile(abs_src_path)
                    h2 = Hash.hashFile(abs_dest_path)

                    # If files is different
                    if h1 != h2:
                        files_to_write.append((abs_src_path, abs_dest_path))

                # If it is an already existing file
                else:
                    pass

            # If path does not exist
            else:

                # Create directory or file or whatever the thing is
                if os.path.isdir(abs_src_path):
                    os.mkdir(abs_dest_path)
                
                # else if this is a file that doesn't exist, transfer it
                else:
                    
                    files_to_write.append((abs_src_path, abs_dest_path))
                    
    if len(files_to_write) == 0:
        print("Nothing to write.")
        sys.exit(0)

    # Start transfering files
    print("Calculating size to write...")
    total_bytes = sum([os.path.getsize(item[0]) for item in files_to_write])

    # Start the UI
    if total_bytes > 0:
        
        print("Moving " + Calcualate_Size(total_bytes))
        cli_task = threading.Thread(target=cli.cli, args=(bytes_written, byte_lock, total_bytes))
        cli_task.setDaemon(True)
        cli_task.start()

        # Now we start to write the data
        Transfer.transfer(files_to_write, 4, bytes_written, byte_lock)
         
        # This will wait for the cli to finish
        cli_task.join()

    sys.exit(0)
                