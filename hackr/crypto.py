import hashlib
import os
import bcrypt
import whirlpool
import requests

class Encrypt:

    def __init__(self, plain_text):
        self.plain_text = plain_text

    def sha1(self):
        encrypted = hashlib.sha1(self.plain_text).hexdigest()
        return encrypted

    def md5(self):
        encrypted = hashlib.md5(self.plain_text).hexdigest()
        return encrypted

    def bcrypt(self):
        encrypted = bcrypt.hashpw(self.plain_text, bcrypt.gensalt())
        return encrypted

    def whirlpool(self):
        encrypted = whirlpool.new(self.plain_text).hexdigest()
        return encrypted


class Decrypt:

    def __init__(self, hash, worldlist):
        self.hash = hash
        self.wordlist = worldlist

    def sha1(self):
        if os.path.isfile(self.wordlist) and os.access(self.wordlist, os.R_OK):
            f = open(self.wordlist, "r")
            for i in f:
                plain_text = i.rstrip('\n')
                encrypted = hashlib.sha1(plain_text).hexdigest()

                if encrypted == self.hash:
                    return plain_text
            return "Can not found this encrypted hash"
        return "Wordlist not accessible"

    def md5(self):
        if os.path.isfile(self.wordlist) and os.access(self.wordlist, os.R_OK):
            f = open(self.wordlist, "r")
            for i in f:
                plain_text = i.rstrip('\n')
                encrypted = hashlib.md5(plain_text).hexdigest()

                if encrypted == self.hash:
                    return plain_text
                    checker = False
            return "Can not found this encrypted hash"
        return "Wordlist not accessible"

    def bcrypt(self):
        if os.path.isfile(self.wordlist) and os.access(self.wordlist, os.R_OK):
            f = open(self.wordlist, "r")
            for i in f:
                plain_text = i.rstrip('\n')
                if bcrypt.checkpw(plain_text, self.hash):
                    return plain_text
            return "Can not found this encrypted hash"
        return "Wordlist not accessible"

    def whirlpool(self):
        if os.path.isfile(self.wordlist) and os.access(self.wordlist, os.R_OK):
            f = open(self.wordlist, "r")
            for i in f:
                plain_text = i.rstrip('\n')
                encrypted =  whirlpool.new(plain_text).hexdigest()

                if encrypted == self.hash:
                    return plain_text
            return "Can not found this encrypted hash"
        return "Wordlist not accessible"


class Currency:

    def __init__(self, value, coin = None):
        self.value = value
        self.coin = coin

    def convert(self, from_coin, to_coin):
        params = {'fsym' : from_coin.upper(), 'tsyms' : to_coin.upper()}
        response = requests.get('https://min-api.cryptocompare.com/data/price', params = params)

        if 'Message' in response.json().keys():
            return response.json()['Message']
        return response.json()[to_coin.upper()] * self.value

    def to(self, to_coin):
        if self.coin is not None:
            return self.convert(self.coin, to_coin)
        return 'Currency not defined'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def coin(self):
        return self._coin

    @coin.setter
    def coin(self, coin):
        self._coin = coin
