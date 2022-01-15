import os
import sys
import DirList
import Hash

# Do something here
if __name__ == '__main__':

    argv = sys.argv
    argc = len(argv)

    print(argv)

    # Need at least two directories or files
    if (argc < 3):
        sys.stderr.write('ERROR : Not enough arguments\n')
        sys.exit(-1)
    
    # Add on the \
    source = argv[1] if argv[1][len(argv[1]) - 1] == '\\' else argv[1] + '\\'
    dest   = argv[2] if argv[2][len(argv[2]) - 1] == '\\' else argv[2] + '\\'

    # Create the lists (relative paths)
    print('Searching ' + source[:len(source) - 1])
    src_dir_list  = DirList.CreateDirMap(source) 
    
    print('Searching ' + dest[:len(dest) - 1])
    dest_dir_list = DirList.CreateDirMap(dest)

    print(src_dir_list)
    print(dest_dir_list)

    # Iterate through each path
    for src_path in src_dir_list:

        # If both paths exists
        if src_path in dest_dir_list:
            
            abs_src_path  = source + src_path
            abs_dest_path = dest + src_path 

            # If this is a file
            if os.path.isfile(abs_src_path):
                
                h1 = Hash.hashFile(abs_src_path)
                h2 = Hash.hashFile(abs_dest_path)

                # Update file if they are different
                if h1 != h2:
                    
                    src_file  = open(abs_src_path, 'rb')
                    dest_file = open(abs_dest_path, 'wb')
                    
                    buf_size = 1024
                    buf = src_file.read(buf_size)
                    while buf > 0:
                    
                        dest_file.write(buf)
                        buf = src_file.read(buf_size)

                    src_file.close()
                    dest_file.close()
        
        # If path does not exist
        else:

            # Create directory or file or whatever the thing is
            if os.path.isdir(source + src_path):
                os.mkdir(dest + src_path)
            else:
                os.open(dest + src_path, 'wb').close()