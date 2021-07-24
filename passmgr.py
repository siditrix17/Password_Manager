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


#function for string generation
def id_generator(size, chars=string.ascii_lowercase+ string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def filencrypt(infile,outfile,password,bufferSize):
 pyAesCrypt.encryptFile(infile, outfile, password, bufferSize)
# decrypt
def filedecrypt(infile,outfile,password,bufferSize):
 pyAesCrypt.decryptFile(outfile, infile, password, bufferSize)



# encryption/decryption buffer size - 128K
bufferSize = 128 * 1024
infile="passwords.txt"
outfile="passwords.txt.aes"
password="siditrix"


# encrypt

def firsttimepassset(): #first time password generation fucntion
    print("-----setting password for 1st time----")
    print(">>Dont forget this password--- backup feature not added yet!!")
    passw=input(">>enter password:")
    #use csv

    with open('passwords.txt', 'a', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(["user",passw])
    print(">>Writing done!! encrypting and storing password")
    filencrypt(infile,outfile,password,bufferSize)




def genandstorepass(infile,outfile,password,bufferSize): #funcion to generate and store password
    account=input(">>Enter your account for which to generate password [facebook,gmail etc.]:")
    sizze=int(input(">>Enter password's length:\n"))
    print(">>Generating random Password")
    time.sleep(1)
    genpass=id_generator(sizze)

    print("Generated password: "+genpass+"\n")
    print(">>data will be stored and ecrypted in password.txt.aes")
    filedecrypt(infile,outfile,password,bufferSize)
    with open('passwords.txt', 'a', newline='') as file:
     writer = csv.writer(file)
     writer.writerow([account,genpass])

    print(">>Writing done!! encrypting and storing password")
    filencrypt(infile,outfile,password,bufferSize)




def retrivefile(infile,outfile,password,bufferSize): #function for retriving the password
    account=input("enter account for which to retrive password>>")
    filedecrypt(infile,outfile,password,bufferSize)
    with open('passwords.txt', 'r') as file:
     reader = csv.reader(file)
     for row in reader:
         if row[0]==account:
             print("Password:"+row[1])
    filencrypt(infile,outfile,password,bufferSize)

def checkpass():
    filedecrypt(infile,outfile,password,bufferSize)



def showoption():
    toshow="""
    **After installing this script, set first time password [4] for password manager!!--important step

    Operations to do :
    1) Generating and storing passwords
    2) Retriving passwords
    3) Change password for password manager
    4) **first time password set for password manager[only once needed]

    99) quit
    """

    print(toshow)
    op=int(input("Enter option:"))
    if op==1:
        genandstorepass(infile,outfile,password,bufferSize)
        showoption()
    elif op==2:
        retrivefile(infile,outfile,password,bufferSize)
        showoption()
    elif op==3:
        print("change pass")
    elif op==4:
        firsttimepassset()
        showoption()
    elif op==99:
        return








banner="""

######     #                  #     #                         #     #                       #####
#     #   # #    ####   ####  #  #  #  ####  #####  #####     ##   ##   ##   #    #   ##   #     # ###### #####
#     #  #   #  #      #      #  #  # #    # #    # #    #    # # # #  #  #  ##   #  #  #  #       #      #    #
######  #     #  ####   ####  #  #  # #    # #    # #    #    #  #  # #    # # #  # #    # #  #### #####  #    #
#       #######      #      # #  #  # #    # #####  #    #    #     # ###### #  # # ###### #     # #      #####
#       #     # #    # #    # #  #  # #    # #   #  #    #    #     # #    # #   ## #    # #     # #      #   #
#       #     #  ####   ####   ## ##   ####  #    # #####     #     # #    # #    # #    #  #####  ###### #    #
    v-1.0
"""
print(banner+"\n")
showoption()
