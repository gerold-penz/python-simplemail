#################
Python-Simplemail
#################

Python-Simplemail ist ein Python-Paket zum Versenden von Emails mit Anhängen.

--------------

ACHTUNG! Ich bin mitten in der Umstellung von SVN nach Git und die Integration
ins PyPi ist auch noch am Laufen. Bitte gönnt mir noch ein wenig Zeit um die
Umstellungen durchzuführen. :-)

--------------

Aus Kompatibilitätsgründen wird die Weiterentwicklung von Simplemail im Ordner
*simplemail2* stattfinden. *simplemail2* wird in Teilen nicht mehr abwärtskompatibel
sein.

*simplemail2* ist im Moment noch nicht einsatzbereit. Bitte verwende so lange 
noch das altbewährte *simplemail*.

Beispiel:

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

Anwendungsbeispiele findest du im Python-Forum: http://www.python-forum.de/viewtopic.php?f=11&t=3158

mfg
Gerold
:-)
