#!/usr/bin/env python

from getpass import getpass
from hashlib import sha1, sha256, sha512

def getPassword():
    pw = getpass('Enter your password: ')
    pw2 = getpass('Enter your password for confirmation: ')
    if pw == pw2:
        return pw
    print "Your passwords do not match, please try again!\n"
    getPassword()

if __name__ == '__main__':
    print "Warning!! You will not be able to see your password when you enter it..."
    result = ""
    password = getPassword()
    hashObject = sha1()
    hashObject.update(password)
    result += "Sha1: " + hashObject.hexdigest() + '\n'
    hashObject = sha256()
    hashObject.update(password)
    result += "Sha256: " + hashObject.hexdigest() + '\n'
    hashObject = sha512()
    hashObject.update(password)
    result += "Sha512: " + hashObject.hexdigest() + '\n'
    with open('hashedPassword.txt', 'w') as file_:
        file_.write(result)
    print "Success!  Please email the 'hashedPassword.txt' file in the current directory to pchan1@stuy.edu.  Thank you!"
    
        
