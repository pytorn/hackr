#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Any added Modules
from .internet import *

### Anything you want in hacker.generator
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
