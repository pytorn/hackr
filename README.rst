hackr: Unicorn library for Hackathons
=====================================

An All-in-one library, safe for hackathon consumption.

You can perform each and every task using a single library.

Features
--------

hackr currently supports the following features:

- Generate random names
- Generate random address
- Generate random dates
- Generate random digits
- Generate random characters
- Scrape any webpage
- Send web requests (GET, POST, PUT)
- Parse data in JSON
- Send Emails

hackr officially supports Python 2.7 currently.

Usage
-----

Generate Random names

    >>> import hackr
    >>> hackr.generator.names(5)
    [u'Mr. Thomas Wolf MD', u'Valerie Turner', u'Maria Knight', u'Raymond Shelton', u'Erica Glenn']

Generate random address

    >>> import hackr
    >>> hackr.generator.address(2)
    [u'10046 Samantha Mission\nRodriguezfurt, PW 24665-0184']

Generate Random dates

    >>> import hackr
    >>> hackr.generator.dates(3, 1995, 2017)
    ['1999-07-03 00:00:00', '2001-04-17 00:00:00', '2016-09-16 00:00:00']

Generate Random digits
    
    >>> hackr.generator.digits(3, 5)
    [0, 1, 2, 3, 2]
    >>> hackr.generator.digits(1, 10)
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 0]

Generate random characters

    >>> hackr.generator.characters(10)
    ['p', 'q', 'M', 'm', 'R', 'b', 'b', 'N', 'a', 'E']

Generate Random json data

    >>> import hackr
    >>> hackr.object_generator.generate_json(4, name='names', address='address')
    '[{"name": "Jeffery Russell", "address": "USNV Bradley\\nFPO AA 49483-3369"}, {"name": "Caitlin Wong", "address": "4622 Richard Summit Apt. 325\\nHollow
    aystad, OH 88464"}, {"name": "Adrian Pugh", "address": "977 Hill Meadows Suite 944\\nVictoriaton, PR 58653-2191"}, {"name": "Christopher Schaefer", "add
    ress": "62215 Charles Cape Apt. 039\\nHaleymouth, ND 82518-8938"}]'

Scrape a webpage

    >>> import hackr
    >>> a= hackr.web.scrape("https://api.github.com/users/ashwini0529")

Make Web Requests

    >>> import hackr
    >>> #If you want the response as a string
    >>> a= hackr.web.request("http://httpbin.org/post", method="post", params={'a':'b'})
    >>> If you want the response as JSON
    >>> a= hackr.web.request("http://httpbin.org/post", method="post", params={'a':'b'}, type="JSON")

Send Emails

    >>> import hackr
    >>> #Enter your GMAIL email address and password in the parameters email, and password.
    >>> hackr.actions.email("Hey there", email="foo@bar.com", password="foobar", to="bar@foo.com", subject="Foo Bar")

    
Contribution Guidelines
-----------------------

- Fork the repository
- Find an issue or create one
- Create a branch(we prefer to name it patch)
- Inform everyone that you're working on the issue
- Send a pull request with proper explaination of what you did
- Wait for getting it reviewed.
- We'd be glad to merge your PR

Made with ♥ by: `PyTorn <https://github.com/pytorn>`_ | `Ashwini Purohit <https://github.com/ashwini0529>`_