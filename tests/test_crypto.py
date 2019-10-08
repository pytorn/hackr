import mock
import pytest
import requests

import hackr


def test_currency_api_connection():
    params = {'fsym': 'BTC', 'tsyms': 'BTC'};
    req = requests.get('https://min-api.cryptocompare.com/data/price', params=params)

    assert req.ok == True
    with pytest.raises(Exception):
        req.json()['Response']


@mock.patch('requests.Response.json', return_value={'TEST': 2, 'TEST1': 3})
def test_currency(get):
    coin_test = hackr.crypto.Currency(2, 'TEST')

    assert coin_test.convert('TEST', 'TEST') == 4
    assert coin_test.convert('TEST', 'TEST1') == 6

    assert type(hackr.crypto.Currency(2).to('TEST')) is str
    coin_test.coin = 'TEST'
    coin_test.value = 1

    assert coin_test.to('TEST') == 2
    assert coin_test.to('TEST1') == 3
