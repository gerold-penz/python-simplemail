#################################################################
Python-Simplemail - Simple SMTP Client Library For Sending Emails
#################################################################

Python-Simplemail sends emails with and without attachments


============
Installation
============

::

    pip install python-simplemail


=======
Example
=======


.. code:: python

    import simplemail
    simplemail.Email(
        smtp_server = "localhost",
        smtp_user = "my_username",
        smtp_password = "my_password",
        from_address = u"sender@domain.at",
        to_address = u"recipient@domain.at",
        subject = u"This is the subject with umlauts (ÖÄÜß)",
        message = u"This is the short message body with umlauts (ÖÄÜß)."
    ).send()

Find examples in the German Python-Forum: http://www.python-forum.de/viewtopic.php?f=11&t=3158


========
Licenses
========

- GNU Library or Lesser General Public License (LGPL)
- MIT License

