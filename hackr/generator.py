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
    for i in range(count):
        year = random.randint(start_year, end_year)
        month = random.randint(1, 12)
        if month != 2:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 28)
        dataset.append(str(datetime(year, month, day)))
    return dataset  # Currently it doesn't include 31st and 29th Feb


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
