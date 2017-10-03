#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
from datetime import datetime

from faker import Faker

fake = Faker()


def digits(end, count):
    dataset = []
    for i in range(count):
        dataset.append(random.randint(0, end))
    return dataset


def characters(count):
    dataset = []
    for i in range(count):
        dataset.append(random.choice(string.letters))
    return dataset


def dates(count, start_year, end_year):
    dataset = []
    leap_year = False
    for i in range(count):
        year = random.randint(start_year, end_year)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_year = True
        month = random.randint(1, 12)
        if month == 2 and leap_year:
            day = random.randint(1, 29)
        elif month == 2 and not leap_year:
            day = random.randint(1, 28)
        elif month == 9 or month == 4 or month == 6 or month == 11:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)
        dataset.append(str(datetime(year, month, day)))
    return dataset


def names(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.name())
    return dataset


def address(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.address())
    return dataset


# From faker.providers.internet
def user_name(count, *args, **kwargs):
    dataset = []
    for i in range(count):
        dataset.append(fake.user_name(*args, **kwargs))
    return dataset


def domain_word(count, *args, **kwargs):
    dataset = []
    for i in range(count):
        dataset.append(fake.domain_word(*args, **kwargs))
    return dataset


def email(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.email())
    return dataset


def url(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.url())
    return dataset


def ipv4(count, network=False):
    dataset = []
    for i in range(count):
        dataset.append(fake.ipv4(network=network))
    return dataset


def free_email_domain(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.free_email_domain())
    return dataset


def uri_path(count, deep=None):
    dataset = []
    for i in range(count):
        dataset.append(fake.uri_path(deep=deep))
    return dataset


def uri(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.uri())
    return dataset


def mac_address(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.mac_address())
    return dataset


def domain_name(count, levels=1):
    dataset = []
    for i in range(count):
        dataset.append(fake.domain_name(levels=levels))
    return dataset


def free_email(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.free_email())
    return dataset


def uri_page(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.uri_page())
    return dataset


def safe_email(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.safe_email())
    return dataset


def slug(count, *args, **kwargs):
    dataset = []
    for i in range(count):
        dataset.append(fake.slug(*args, **kwargs))
    return dataset


def company_email(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.company_email())
    return dataset


def image_url(count, width=None, height=None):
    dataset = []
    for i in range(count):
        dataset.append(fake.image_url(width=width, height=height))
    return dataset


def tld(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.tld())
    return dataset


def ipv6(count, network=False):
    dataset = []
    for i in range(count):
        dataset.append(fake.ipv6(network=network))
    return dataset


def uri_extension(count):
    dataset = []
    for i in range(count):
        dataset.append(fake.uri_extension())
    return dataset

# end faker.providers.internet
