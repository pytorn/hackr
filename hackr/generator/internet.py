# internet.py
# Implementation of the faker.provider.internet methods
from faker import Faker

fake = Faker()

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
