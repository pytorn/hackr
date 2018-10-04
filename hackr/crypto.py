import hashlib
import os

class Encrypt:

    def __init__(self, plain_text):
        self.plain_text = plain_text

    def sha1(self):
        encrypted = hashlib.sha1(self.plain_text).hexdigest()
        print encrypted

    def md5(self):
        encrypted = hashlib.md5(self.plain_text).hexdigest()
        print encrypted

class Decrypt:

    def __init__(self, hash, worldlist):
        self.hash = hash
        self.wordlist = worldlist

    def sha1(self):
        checker = True
        if os.path.isfile(self.wordlist) and os.access(self.wordlist, os.R_OK):
            f = open(self.wordlist, "r")
            for i in f:
                plain_text = i.rstrip('\n')
                encrypted = hashlib.sha1(plain_text).hexdigest()

                if encrypted == self.hash:
                    print plain_text
                    checker = False
            if checker:
                print "Can not found this encrypted hash"

    def md5(self, encrypted):
        checker = True
        if os.path.isfile(self.wordlist) and os.access(self.wordlist, os.R_OK):
            f = open(self.wordlist, "r")
            for i in f:
                plain_text = i.rstrip('\n')
                encrypted = hashlib.md5(plain_text).hexdigest()

                if encrypted == self.hash:
                    print plain_text
                    checker = False
            if checker:
                print "Can not found this encrypted hash"


