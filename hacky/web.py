#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

"""
Defining this function as of now. Will come back to this later.
Need to have a generic function for all the scrape related actions.
"""


def scrape(url):  # type can be JSON as of now
    scraped_webpage = requests.get(url)
    if type != "JSON":
        return scraped_webpage.text
    try:
        return scraped_webpage.json()
    except ValueError:
        return 'No JSON object could be decoded'


def request(url, **kwargs):
    if kwargs is not None:
        try:
            payload = kwargs['params']
        except KeyError:
            payload = None
            return 'It only supports optional argument: method, params and type'
        try:
            method = kwargs['method']
        except KeyError:
            print('Please mention the method: get, post, put')
            return

        try:
            return_type = kwargs['type']
        except KeyError:
            return_type = None

        if method.lower() == "get":
            r = requests.get(url, params=payload)
        elif method.lower() == "post":
            r = requests.post(url, params=payload)
        elif method.lower() == "put":
            r = requests.put(url, params=payload)
        else:
            return 'Method not allowed'

        if return_type == "JSON":
            return r.json()
        else:
            return r.text
