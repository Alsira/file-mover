# Author : Alsira
# Description : Each node a directory or file in the file system, used for comparisions.

class Node:

    def __init__(self, name="", hash="", is_file = False):

        self.__name = name # Name of node
        self.__hash = hash # Hash (Only if file)
        self.__is_file = is_file # If this node is a file
        self.__searched = False # If the has been searched

        if hash == "":
            self.__hasHash = False
        else:
            self.__hasHash = True

        self.__sub_nodes = list() # A list of sub nodes



    # Getters and setters
    def setName(self, name):
        self.__name = name

    def setHash(self, hash):
        self.__hash = hash
        self.__hasHash = True

    def hasHash(self):
        return self.__hasHash

    def hasBeenSearched(self):
        return __searched

    def Searched(self, value):
        self.__searched = value
    
    def getName(self):
        return self.__name

    def getHash(self):
        return self.__hash

    def addNode(self, node):
        self.__sub_nodes.append(node)

    def getNodes(self):
        return self.__sub_nodes
