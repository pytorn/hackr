#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

'''

A function to send emails using SMTP (GMAIL)
Sample usage: hackr.actions.email("Hey there",
email="foo@bar.com", password="foobar", to="bar@foo.com", subject="Foo Bar")

'''

SMTP_PORT = 587
SMTP_URL = "smtp.gmail.com"


def email(message, **kwargs):

    mail_id = kwargs['email']
    mail_password = kwargs['password']
    to_mail = kwargs['to']
    mail_subject = kwargs['subject']
    mail_content = 'Subject: {}\n\n{}'.format(mail_subject, message)
    try:
        server = smtplib.SMTP(SMTP_URL, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(mail_id, mail_password)
        server.sendmail(mail_id, to_mail, mail_content)
        server.close()
        return 'Mail Sent Successfully'
    except Exception as e:
        print(e)
