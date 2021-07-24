print("Random password Manager:---")
"""
hellos sidi
this code will work for linux and windows
Random password generator --version--1.0
"""
import string
import random
import pyAesCrypt
import time
import os
import csv
import sys

import hashlib





#function for password generation
def pass_generator(size, chars=string.ascii_lowercase+ string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


#encrypt
def filencrypt(infile,outfile,password,bufferSize):
 pyAesCrypt.encryptFile(infile, outfile, password, bufferSize)


# decrypt
def filedecrypt(infile,outfile,password,bufferSize):
 pyAesCrypt.decryptFile(outfile, infile, password, bufferSize)




# encryption/decryption buffer size - 128K
bufferSize = 128 * 1024
infile="accounts.txt"
outfile="accounts.txt.aes"


def globalpassword():
	print("Welcome to password setup\n")
	print("Use this password to access the password manager\n")
	passwd= input("Password:")
	result = hashlib.sha256(passwd.encode())
  
     	# printing the equivalent hexadecimal value.
	print("The hexadecimal equivalent of SHA256 is : ")
	print(result.hexdigest())
  
globalpassword()
	



















