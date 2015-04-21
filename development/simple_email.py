#!/usr/bin/env python
# coding: utf-8

# BEGIN --- required only for testing, remove in real world code --- BEGIN
import os
import sys
THISDIR = os.path.dirname(os.path.abspath(__file__))
APPDIR = os.path.abspath(os.path.join(THISDIR, os.path.pardir, os.path.pardir))
sys.path.insert(0, APPDIR)
# END --- required only for testing, remove in real world code --- END


import simplemail


simplemail.Email(
    smtp_server = "smtp.gmail.com:587",
    smtp_user = "xxx@gmail.com",
    smtp_password = "xxx",
    use_tls = True,

    from_address = "xxx@gmail.com",
    to_address = "xxx@xxx.xx",

    subject = u"Really simple example with umlauts (öäüß)",
    message = u"This is the message with umlauts (öäüß)",
).send()

print "Sent"
print
