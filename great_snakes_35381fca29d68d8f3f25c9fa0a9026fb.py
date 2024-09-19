#!/usr/bin/env python3

import base64
from Crypto.Util.number import *

# import this

char = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

flag = "".join(chr(value) for value in char)
print("Here is your flag:"+flag)

flag2 = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print( "your flag is: " + bytes.fromhex(flag2).decode())

flag3 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
flag3_1 = bytes.fromhex(flag3)
print("your flag is: " + base64.b64encode(flag3_1).decode())

# convert our messages into numbers so that mathematical operations can be applied
flag4 = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
flag4_1 =  long_to_bytes(flag4)
print("The flag is: " + flag4_1.decode())

# Given the string label, XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}.
a = "label"
key = 13
conv = bytes_to_long(a.encode())
flag5 = "".join(chr(ord(char) ^ 13) for char in a)
flag = f"crypto{{{flag5}}}"
print("Here is your flag:"+flag)

#  Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_KEY1_KEY3_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key1_b = bytes.fromhex(KEY1)
key2_1b = bytes.fromhex(KEY2_KEY1)
key2_3b = bytes.fromhex(KEY2_KEY3)
flag_123b = bytes.fromhex(FLAG_KEY1_KEY3_KEY2)

key2_b = bytes(a ^ b for a, b in zip(key2_1b, key1_b))
key3_b = bytes(a ^ b for a, b in zip(key2_3b, key2_b))
flag_b = bytes(a ^ b ^ c ^ d for a, b, c, d in zip(flag_123b, key1_b, key2_b, key3_b))

flag_final = flag_b.decode()
print("Here is your flag: " + flag_final)


