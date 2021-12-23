# Author : Tyler J.
# Description : This sucker creates a list of the paths to each file in a directory

import os

# This helps out the CreateDirMap
def __CreateDirHelper(search_path: str, dir_list: list) -> None:

    # Loop through each path
    for path in os.listdir(search_path):
        
        # Ignore current and parent directories
        if path != "." and path != "..":
            
            # Append the directory or file, then decend if this is a directory
            dir_list.append(path)

            if os.path.isdir(path):
                __CreateDirHelper(path, dir_list)

# Uses recursion in the helper to find files
def CreateDirMap(path: str) -> list:

    # List of directories
    dirs = list()
    
    for p in os.listdir(path):

        # Add directory to the list, decend if it is a directory
        dirs.append(p)

        if os.path.isdir(p):
            __CreateDirHelper(p, dirs)
        
    return dirs