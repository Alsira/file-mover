import sys
import DirList

# Do something here
if __name__ == "__main__":

    argv = sys.argv
    argc = len(argv)

    # Need at least two directories or files
    if (argv < 3):

        sys.stderr.write("ERROR : Not enough arguments\n")
    
    # Kinda assuming the positions here
    source = argv[1]
    dest   = argv[2]

    # Create the lists
    src_dir_list = DirList.CreateDirMap(source) 
    dest_dir_list = DirList.CreateDirMap(dest)

    # Iterate through each path
    for src_path in src_dir_list:

        # If the src_path is in the dest
        if src_path in dest_dir_list:

            


