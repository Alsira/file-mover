# Author : Tyler J.
# Description : This sucker creates a list of the paths to each file in a directory

import os

# This helps out the CreateDirMap
def __CreateDirHelper(init_path: str, search_path: str, dir_list: list) -> None:
    """
    This simply helps the CreateDirMap function.

    This is a recurrsive helper function made to recurrsiviely decend into a directory.

    :param init_path: This is the initial searching path. We use this cause the program needs the beginning '/home' or whatever.
    :type init_path: str
    :param search_path: The path to search
    :type search_path: str
    :param dir_list: This will append names found in relative manner to the search_path
    :type dir_list: list
    """

    # Loop through each path
    for path in os.listdir('/'.join([init_path, search_path])):

        # Ignore current and parent directories
        if path != "." and path != "..":
            
            path = '/'.join([search_path, path])

            # Append the directory or file, then decend if this is a directory
            dir_list.append(path)

            if os.path.isdir('/'.join([init_path, path])):
                __CreateDirHelper(init_path, path, dir_list)


def CreateDirMap(path: str) -> list:
    """
    Will create a list of directories relative to the path given.

    The path names is pretty much appended as this is searching. For example, if we call CreateDirMap('dir'), this function will
    search dir and return a list like ['some.txt', 'dir2/'some2.txt'] and so on. If you call CreateDirMap('/home'), you get
    something like ['username/Documents/homework/naughty.png'].

    :param path: The path to search
    :type path: str
    :return: A list of relative directories without the path name at the beginning.
    :rtype: list
    """

    # List of directories
    dirs = list()
    
    for p in os.listdir(path):
        
        # Add directory to the list, decend if it is a directory
        dirs.append(p)

        if os.path.isdir('/'.join([path, p])):
            __CreateDirHelper(path, p, dirs)
    
    return dirs
    