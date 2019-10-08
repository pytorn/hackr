#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import shutil
from xml.etree.ElementTree import tostring

import requests
from bs4 import BeautifulSoup
from xmljson import badgerfish as bf

"""
Defining this function as of now. Will come back to this later.
Need to have a generic function for all the scrape related actions.
"""


def scrape_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    folder_name = url.split('/')[2]
    if not os.path.exists(folder_name + "/images"):
        os.makedirs(folder_name + "/images")
    num = "0"
    imgs = soup.findAll("img", {"src": True})
    for img in imgs:
        num = str(num)
        img_url = img["src"]
        img_data = requests.get(img_url, stream=True)
        if img_data.status_code == 200:
            img_data.raw.decode_content = True
            f = open(folder_name + "/images/Image" + num + "." + img_url[-3:], "wb")
            shutil.copyfileobj(img_data.raw, f)
            f.close()
            num = int(num) + 1


def scrape(url, **kwargs):
    scraped_webpage = requests.get(url)
    return_type = kwargs['type'].lower()
    get_images = kwargs.get('images', False)
    if return_type == "json" and get_images:
        try:
            scrape_images(url)
            return scraped_webpage.json()
        except ValueError:
            return 'No JSON object could be decoded'
    elif return_type == "xml" and get_images:
        try:
            scrape_images(url)
            json_data = json.loads(scraped_webpage.content)
            xml_data = ""
            for element in bf.etree(json_data):
                xml_data += tostring(element)
            return xml_data
        except ValueError:
            return 'No XML could be decoded'
    else:
        return scraped_webpage.text


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
