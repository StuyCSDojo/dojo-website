#!/usr/bin/env python

from getpass import getpass
from hashlib import sha1, sha256, sha512

def getPassword():
    password = getpass('Enter your password: ')
    confirmationPassword = getpass('Enter your password for confirmation: ')
    if password == confirmationPassword:
        return password
    print "Your passwords do not match, please try again!\n"
    return getPassword()

def getHashedPassword(hashAlgorithm, password):
    hashObject = hashAlgorithm()
    hashObject.update(password)
    return hashObject.hexdigest()

def main():
    print "Warning!! You will not be able to see your password when you enter it..."
    result = ""
    password = getPassword()
    result += "Sha1: " + getHashedPassword(sha1, password) + '\n'
    result += "Sha256: " + getHashedPassword(sha256, password) + '\n'
    result += "Sha512: " + getHashedPassword(sha512, password) + '\n'
    with open('hashedPassword.txt', 'w') as file_:
        file_.write(result)
    print "Success!  Please email the 'hashedPassword.txt' file in the current directory to pchan1@stuy.edu.  Thank you!"

if __name__ == '__main__':
    main()
