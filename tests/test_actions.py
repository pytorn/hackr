from io import StringIO
from unittest import mock

import smtplib
import pytest

from hackr.actions import email


@mock.patch('smtplib.SMTP')
def test_email(mock_smtp):
    message = 'Mail message'
    params = {
        'email': 'mail@test.com',
        'password': 'password',
        'to': 'test@mail.com',
        'subject': 'Test',
    }
    mock_smtp = mock.Mock()

    response = email(message, **params)

    assert response == 'Mail Sent Successfully'


@mock.patch('smtplib.SMTP')
def test_email_exception(mock_smtp):
    message = 'Mail message'
    params = {
        'email': 'mail@test.com',
        'password': 'password',
        'to': 'test@mail.com',
        'subject': 'Test',
    }

    instance = mock_smtp.return_value
    instance.ehlo.side_effect = smtplib.SMTPRecipientsRefused('Failed to sent mail.')
    response = email(message, **params)

    assert not response
