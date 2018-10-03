from bs4 import BeautifulSoup
import requests
import socket
import sys

def getLiveIP():
	try:
		res = BeautifulSoup(requests.get('https://www.whatsmyip.com').text, 'lxml')
		return str(res.find_all('p')[0].getText())
	except Exception as _:
		print 'Could not get live IP address'

def getPrivateIP():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 80))
		priv_ip = s.getsockname()[0]
		s.close()
		return priv_ip
	except Exception as _:
		print 'Could not get local IP Address'



