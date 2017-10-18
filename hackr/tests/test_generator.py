import pytest
import hackr
import re

def test_digits():
    assert len(hackr.generator.digits(3, 0)) == 0
    assert len(hackr.generator.digits(3, 4)) == 4
    assert len(hackr.generator.digits(3, -6)) == 0  # should it raise an exception?
    assert all(x <= 3 for x in hackr.generator.digits(3, 100))
    assert all(type(x) == int for x in hackr.generator.digits(3, 100))
    assert all(x == 0 for x in hackr.generator.digits(0, 100))
    with pytest.raises(Exception):
        hackr.generator.digits('3', 4)
    with pytest.raises(Exception):
        hackr.generator.digits(3, '4')
    with pytest.raises(Exception):
        hackr.generator.digits(-1, 4)
    with pytest.raises(Exception):
        hackr.generator.digits(None, 4)
    with pytest.raises(Exception):
        hackr.generator.digits('3', None)


def test_characters():
    assert len(hackr.generator.characters(4)) == 4
    assert all(type(x) == str for x in hackr.generator.characters(4))
    with pytest.raises(Exception):
        hackr.generator.characters('3')
    with pytest.raises(Exception):
        hackr.generator.characters(None)


def test_names():
    assert len(hackr.generator.names(5)) == 5
    assert all(len(x.split(' ')) >= 2 for x in hackr.generator.names(50))
    assert all(x.istitle for x in hackr.generator.names(5))
    with pytest.raises(Exception):
        hackr.generator.names('3')
    with pytest.raises(Exception):
        hackr.generator.names(None)


def test_dates():
    assert len(hackr.generator.dates(5, 0, 2000)) == 5
    assert all(type(x) == str for x in hackr.generator.dates(5, 1, 2000))
    assert all(1 <= int(x.split('-')[0]) <= 2000 for x in hackr.generator.dates(200, 1, 2000))
    assert all(1 <= int(x.split('-')[1]) <= 12 for x in hackr.generator.dates(200, 1, 2000))
    assert all(1 <= int(x.split('-')[2].split(' ')[0]) <= 31 for x in hackr.generator.dates(020, 1, 2000))
    with pytest.raises(Exception):
        hackr.generator.dates(1, 0, 200008898989898900)
    with pytest.raises(Exception):
        hackr.generator.dates(1, 0, None)
    with pytest.raises(Exception):
        hackr.generator.dates(1, None, 2000)
    with pytest.raises(Exception):
        hackr.generator.dates(None, 0, 1500)


def test_address():
    assert all(x.istitle for x in hackr.generator.address(10))
    assert all(type(x) == unicode for x in hackr.generator.address(10))
    assert all(re.search('[1-9]', x) for x in hackr.generator.address(10))


