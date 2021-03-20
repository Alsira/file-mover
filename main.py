import hashlib
import pathlib
import os

def hash(fname):
    fhash = hashlib.md5()
    block = 128 ** 2
    with open(fname, 'rb') as file:
        fhash.update(file.read(block))
    return fhash

def createTree(dir):

    p = Path(dir)
    
# Do something here
if __name__ == "__main__":

    hello = "hello"