# Author : Alsira
# Description : Handle the Node class and organizses and compares different
#               DirectoryTree classes

import Node
import os

class DirectoryTree:

    def __init__(self, dir=""):
        self.__nodes = list()

        # If a directory was given
        if dir != "":
            self.createTree(dir)

    # Create Tree
    def createTree(self, path):

        
