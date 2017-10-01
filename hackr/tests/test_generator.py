import pytest
import hackr


def test_digits():
    assert len(hackr.generator.digits(3, 0)) == 0
    assert len(hackr.generator.digits(3, 4)) == 4
    assert len(hackr.generator.digits(3, -6)) == 0  # should it raise an exception?
    assert all(x <= 3 for x in hackr.generator.digits(3, 100))
    assert all(x == 0 for x in hackr.generator.digits(0, 100))
    with pytest.raises(Exception):
        hackr.generator.digits('3', 4)
    with pytest.raises(Exception):
        hackr.generator.digits(3, '4')
    with pytest.raises(Exception):
        hackr.generator.digits(-1, 4)

