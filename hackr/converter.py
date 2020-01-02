import requests
import json

"""

Provides Pricing information on a crypto pair or currency pair, such as USD, BTC, ETH EUR

"""
def cryptoPricePair(coinA, coinB):
	try:
		res = json.loads(requests.get('https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s'%(coinA.upper(),coinB.upper())).text)
		return str(res[coinB.upper()])
	except Exception as _:
		print 'Could not get live IP address'
