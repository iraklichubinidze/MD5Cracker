#!/usr/bin/bash

from hashlib import md5

targetHashLoc = input("Enter the location of target hash file: ")
wordlistLoc = input("Enter the location of wordlist file: ")

def readTargetHash(loc):
    f = open(loc,'r')
    return f.read()

def encryptText(plaintext):
    return md5(plaintext.encode('ascii'))

def compareHashes(targetHash,encryptedText):
    if str(targetHash).strip() == str(encryptedText).strip():
        return True

def readWordlist(loc):
    f = open(loc,'r')
    return f.readlines()


targetHash = readTargetHash(targetHashLoc)
wordlist = readWordlist(wordlistLoc)

for word in wordlist:
    encryptedText = encryptText(word.strip()).hexdigest()
    if compareHashes(targetHash,encryptedText) == True:
        print(f"\n[+] {word.strip()} is correct ({encryptedText})\n")
        break
    else:
        print(f"[-] {word.strip()} is not correct")

