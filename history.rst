#################
Python-Simplemail
#################


=============
Version 2.0.0
=============

2015-04-21

- Added to Github


=============
Version 1.0.0
=============

28.05.2012

- Import in das neue Subversion-Repository bei Google-Code.
  http://code.google.com/p/python-simplemail/

- Ein bereits seit langem existierender Umbau von *iso-8859-15* nach *utf-8* wurde
  jetzt in das Repository eingepflegt.

- Das ehemalige Modul *simplemail.py* wurde zur leichteren Verknüpfung mit anderen
  Subversion-Repositories in ein Paket umgewandelt. Das Paket besteht aus dem
  Ordner *simplemail* und dem darin enthaltenen *__init__.py*-Modul.


=============
Version 0.3.1
=============

- Any of the old german descriptions deleted. In the future, the docstrings 
  should be in english. (I will try it.)

- Now, the new exception names are without underlines.
  For backward compatibility, I let the old class names, too.

- New UserAgent-Header: "SimpleMail Python/%s (http://www.python-forum.de/post-18144.html)"

- New parameter to add additional header fields.
  
  ::

    :param header: (optional) Additional header fields as dictionary.
        You can use this parameter to add additional header fields.
        Allready (internal) used header fields are: "From", "Reply-To", "To", 
        "Cc", "Date", "User-Agent" and "Subject". (case sensitive)
        The items of this dictionary replace internal used header fields.


=============
Version 0.2.3
=============

- simplemail kann jetzt mit Googlemail (Gmail)::

    #!/usr/bin/env python
    # -*- coding: iso-8859-1 -*-
    
    import simplemail
    
    simplemail.Email(
        from_address = "EMAILNAME@gmail.com", 
        to_address = "EMPFAENGER@domain.xx",
        subject = "Googlemail Test",
        message = "Das ist ein Googlemail Test.",
        smtp_server = "smtp.googlemail.com:587",
        smtp_user = "EMAILNAME", # Emailadresse ohne "@gmail.com"
        smtp_password = "PASSWORT", 
        use_tls = True # Muss auf True gesetzt sein
    ).send()


=============
Version 0.2.2
=============

- Den Login erst nach ``starttls`` ausführen.

- Überflüssige #------- entfernt

- Neuer Parameter: "use_tls"; gibt an ob die Verbindung mit TLS
  verschlüsselt werden soll. (Ob es funktioniert kann ich nicht testen!)


=============
Version 0.2.1
=============

- Dummy für die Hilfe hinzugefügt und sonstige Kleinigkeiten
  vorbereitet.

- Erstimport in das öffentliche SVN-Repository.
  Die Babyzeit dieses Modules ist sicher vorbei. Deshalb wird
  die Versionisierung mit 0.2.1 begonnen.


==================
Version 2007-05-02
==================

- Überflüssige #------- entfernt

- Neuer Parameter: "use_tls"; gibt an ob die Verbindung mit TLS
  verschlüsselt werden soll. (Ob es funktioniert kann ich nicht testen!)


==================
Version 2006-06-08
==================

- Fehlerklassen von **SimpleMail_Exception** abgeleitet. Damit wird
  bei einem Fehler jetzt auch eine aussagekräftigere Fehlermeldung 
  ausgegeben. Dabei habe ich auch die vertauschten Fehlermeldungen
  ausgetauscht. (Rebecca, danke für die Meldung.)

- Da die Klassen **CCRecipients** und **BCCRecipients** sowiso von
  **Recipients** abgeleitet wurden, kann ich mir das Überschreiben
  der Initialisierung (__init__) und die Angabe der Slots sparen.


==================
Version 2006-05-28
==================

- Wortlaut des Headers "User-Agent" geändert.

- Da nicht jeder SMTP-Server das Datum automatisch zum Header hinzufügt, 
  wird ab jetzt das Datum beim Senden hinzugefügt. 
  (Karl, danke für den wichtigen Hinweis.)


==================
Version 2006-03-30
==================

- Reply-to (Antwort an) kann jetzt auch angegeben werden.


==================
Version 2006-03-22
==================

- Klassen fuer CC-Empfaenger und BCC-Empfaenger hinzugefuegt.
  Ab jetzt können Emails auch an CC und BCC gesendet werden.
  Wie das funktioniert sieht man in der Funktion ``testen()``


==================
Version 2005-12-10
==================

- Schlampigkeitsfehler ausgebessert. Es wurde ein Fehler gemeldet, wenn
  man beim Initialisieren der Klasse Email auch den Dateinamen eines
  Attachments übergeben hatte. Es war ein Unterstrich zu viel, der 
  Entfernt wurde.


==================
Version 2005-11-11
==================

- Fixed: Das Versenden von Emails funktioniert jetzt auch wenn man
  sich am SMTP-Server mit Benutzername und Passwort anmelden muss.
  ChrisSek, danke für den Hinweis.

- Es war, glaube ich, recht lästig, dass Testemails gesendet wurden, 
  wenn man dieses Modul ausführte. Ich habe es so geändert, dass die
  Testemails nur mehr dann gesendet werden, wenn man dieses Modul mit
  dem Parameter "test" aufruft. Z.B. ``python simplemail.py test``


==================
Version 2005-09-29
==================

- Das Format der Hilfe geaendert.

- Ab jetzt wird auch der "User-Agent" im Header mitgesendet.
  Jens, danke für die Idee.


==================
Version 2005-09-28
==================

- Die Rückgabe des Befehls "sendmail()" wird in das Attribut "statusdict"
  der Instanz der Klasse "Email" geschrieben. So ist es jetzt auch moeglich,
  beim Versenden an mehrere Emailadressen, eine exakte Rueckmeldung ueber
  den Versandstatus zu erhalten. Das Format der Rueckgabe wird unter
  der Url http://www.python.org/doc/current/lib/SMTP-objects.html#l2h-3493
  genau erklaert.

  Hier ein Auszug aus dieser Erklaerung:
  This method will return normally if the mail is accepted for at least 
  one recipient. Otherwise it will throw an exception. That is, if this 
  method does not throw an exception, then someone should get your mail. 
  If this method does not throw an exception, it returns a dictionary, 
  with one entry for each recipient that was refused. Each entry contains 
  a tuple of the SMTP error code and the accompanying error message sent 
  by the server.


==================
Version 2005-08-20
==================

- Das Versenden von Anhaengen ermoeglicht


==================
Version 2004-04-25
==================

- Kleine Ausbesserungen in den Beschreibungen vorgenommen

- Einfaches Beispiel in den Beschreibungstext integriert


==================
Version 2004-03-13
==================

- Umlaute in den Beschreibungen ausgebessert

- Schreibweise der Kommentare wurde so umgesetzt dass auf einfache
  Art und Weise eine Uebersetzung stattfinden kann.
  Erklaerung: "de" steht fuer "deutsch" und "en" steht fuer "englisch"



