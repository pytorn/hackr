# `hackr.generator.internet`

`hackr.generator.internet` exposes the members of the `internet` provider from `faker`.

## Methods
Methods can be called with:

```python
>>> print(hackr.generator.internet.ipv4(3, network=True))
['25.154.130.192/26', '136.0.0.0/6', '207.123.44.182/32']
```

All functions require a count and return that number of items in the list (even if this means that there are duplicates). All other function arguments are optional and have default values set already.

All methods given below have an example included afterwards, with any arguments specified. Unless otherwise noted, `count=1`

- `user_name(count, *args, **kwargs)`: Returns user names (['watersjamie'])
- `domain_word(count, *args, **kwargs)`: Returns domain words (`['hunt-wolf']`)
- `email(count)`: Returns  emails (`['douglas34@hotmail.com']`)
- `url(count)`: Returns `count` urls (`['http://koch.com/']`)
- `ipv4(count, network=False)`: Returns IP version 4 addresses. If `network` is `True`, a network prefix is added (`['48.38.136.10']`)
- `free_email_domain(count)`: Returns domains with free email services (`['gmail.com']`) 
- `uri_path(count, deep=None)`: Returns Uniform Resource Identifier paths with a specified depth. (`deep=5`, `['app/list/tag/list/app']`)
- `uri(count)`: Returns whole uri (domain included). The depth of the uri is not configurable. (`['https://www.james.com/tag/wp-content/app/register/']`)
- `mac_address(count)`: Returns Media Access Control (MAC) addresses
- `domain_name(count, levels=1)`: Returns domain names with the specified depth (`levels=3`, `['lin.chaney.olson.org']`)
- `free_email(count)`: Returns emails from the free email list (`['morgangregory@hotmail.com']`)
- `uri_page(count)`: Returns a uri to a page (`count=3`, `['terms', 'privacy', 'login']`)
- `safe_email(count)`: Returns emails that are garunteed to have no real world conflict (`['odavis@example.net']`)
- `slug(count, *args, **kwargs)`: Returns `count` slugs (`count=3`, `['sequi-beatae', 'distinctio-corporis', 'nostrum-placeat']`)
- `company_email(count)`: Returns emails that resemble coorporate emails (`['aellison@holmes.com']`)
- `image_url(count, width=None, height=None)`: Returns a link to a placeholder of width and height (random by default). This link will actually go to an image (`http://www.lorempixel.com/1017/463`)
- `tld(count)`: Returns [top level domains](https://en.wikipedia.org/wiki/Top-level_domain) (`count=5`, `['biz', 'com', 'com', 'net', 'com']`)
- `ipv6(count, network=False)`: Returns IP version 6 addresses (`['853b:a026:23d:884f:47da:da72:5ab0:4d7c']`)
- `uri_extension(count)`: Returns common URI extensions (`['.htm', '.asp', '.html']`)
