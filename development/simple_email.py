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
    smtp_server = "smtp.a1.net:25",
    smtp_user = "xxx",
    smtp_password = "xxx",
    use_tls = False,

    from_address = "xxx",
    to_address = "xxx",

    subject = u"Really simple test with umlauts (öäüß)",
    message = u"This is the message with umlauts (öäüß)",
).send()

print "Sent"
print
