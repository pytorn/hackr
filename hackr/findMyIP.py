from bs4 import BeautifulSoup
import requests
import socket
import sys

try:
	res = BeautifulSoup(requests.get('https://www.whatsmyip.com').text, 'lxml')
	print 'Live IP addr: ', res.find_all('p')[0].getText()
except Exception as _:
	print 'Could not get live IP address'

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 80))
	print 'Local IP on machine: ', s.getsockname()[0]
	s.close()
except Exception as _:
	print 'Could not get local IP Address'

sys.exit(0)

