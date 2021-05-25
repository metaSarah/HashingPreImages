import hashlib
import os

""" hash_preimage(target_string)  takes a single input(a string of bits). 

The function returns a single variable x such that the trailing bits 
of SHA256(x) matches the target string (not the hash of the target string).

Your algorithm should be randomized, i.e., hash_preimage(target_string) 
should not always return the same partial preimage.
"""


def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    
    
    x = None
    
    while x == None:
        
        x_test = os.urandom(len(target_string))
        x_sha = hashlib.sha256(x_test).hexdigest()
        x_shaSlice = x_sha[-(len(target_string)):]
        
        # print("x_shaSlice", x_shaSlice)
        # print("Type of x_shaSlice: ", type(x_shaSlice))
        
        numBits = len(target_string)
        
        # binaryX = bin(int(x_sha,16))[2:].zfill(numBits)
        binaryX = bin(int(x_sha,16))[2:]
        
        binaryX = bin(int(x_sha,16))[-(len(target_string)):]
        
        strBinaryX = str(binaryX)
        
        # print("strBinaryX: ", strBinaryX)
        # print("Type of strBinaryX: ", type(strBinaryX))
        # print("Is there a match?", strBinaryX == target_string)
    
        if strBinaryX == target_string:
            x = x_test
            break
        
        
    # nonce = b'\x00'

    return( x )


# x = hash_preimage("1011111")
# print(x)
# y = hashlib.sha256(x).hexdigest()
# y = bin(int(y,16))[2:]
# print(y)

