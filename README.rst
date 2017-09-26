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
    >>> a = hackr.generator.names(5)
    >>> print a
    [u'Mr. Thomas Wolf MD', u'Valerie Turner', u'Maria Knight', u'Raymond Shelton', u'Erica Glenn']

Generate Random dates

    >>> import hackr
    >>> a= hackr.generator.dates(5,1995,2017)
    >>> print a
    ['1998-08-17 00:00:00', '2007-03-25 00:00:00', '2003-01-27 00:00:00', '2014-10-13 00:00:00', '1995-02-10 00:00:00']

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