# Author : Tyler J.
# Description : Functions that hashes files or data

import hashlib
import random
import math

def hashFile(file: str) -> str:

    hash_list = hashlib.algorithms_available
    hash_to_use: str

    # Check for avalible algorithms (has a priority)
    if not "blake2s" in hash_list:
        if not "md5" in hash_list:
            if not "md4" in hash_list:
                if not "sha128" in hash_list:
                    if not "sha256" in hash_list:
                        # If none of the nice algorithms exist, pick a random one
                        random_index = math.floor(random.random() * len(hash_list))
                        hash_to_use = hash_list[random_index]
                    else:
                        hash_to_use = "sha265"
                else:
                    hash_to_use = "sha128"
            else:
                hash_to_use = "md4"
        else:
            hash_to_use = "md5"
    else:
        hash_to_use = "blake2s"

    hasher = hashlib.new(hash_to_use)
    CHUNKSIZE = 65536 # Bytes to read from file

    # Open and start hashing
    with open(file, "rb") as f:
        buffer = f.read(CHUNKSIZE)
        while len(buffer) > 0:
            hasher.update(f.read(CHUNKSIZE))
            buffer = f.read(CHUNKSIZE)

    return hasher.hexdigest()
