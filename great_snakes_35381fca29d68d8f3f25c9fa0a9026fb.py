#!/usr/bin/env python3
import sys
import base64
# import this
if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

char = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

flag = "".join(chr(value) for value in char)
print("Here is your flag:"+flag)

flag2 = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print( "your flag is: " + bytes.fromhex(flag2).decode())

flag3 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
flag3_1 = bytes.fromhex(flag3)
print("your flag is: " + base64.b64encode(flag3_1).decode())

