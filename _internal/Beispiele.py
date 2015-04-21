
def test():

    # Einfaches Beispiel
    from simplemail import Email

    print "Einfaches Beispiel"
    print "------------------"
    Email(
        from_address = "server@gps.gp",
        smtp_server = "gps.gp",
        to_address = "gerold@gps.gp",
        subject = "Einfaches Beispiel (öäüß)",
        message = "Das ist der Nachrichtentext mit Umlauten (öäüß)",
    ).send()
    print "Fertig"
    print

    # Einfaches Beispiel nur mit CC-Adresse
    from simplemail import Email

    print "Einfaches Beispiel mit CC-Adresse"
    print "---------------------------------"
    email = Email(
        from_address = "server@gps.gp",
        smtp_server = "gps.gp",
        subject = "Einfaches Beispiel mit CC-Adresse (öäüß)",
        message = "Das ist der Nachrichtentext mit Umlauten (öäüß)"
    )
    email.cc_recipients.add("gerold@gps.gp", "Gerold")
    email.send()
    print "Fertig"
    print

    # Einfaches Beispiel nur mit BCC-Adresse
    from simplemail import Email

    print "Einfaches Beispiel mit BCC-Adresse"
    print "---------------------------------"
    email = Email(
        from_address = "server@gps.gp",
        smtp_server = "gps.gp",
        subject = "Einfaches Beispiel mit BCC-Adresse (öäüß)",
        message = "Das ist der Nachrichtentext mit Umlauten (öäüß)"
    )
    email.bcc_recipients.add("gerold@gps.gp", "Gerold Penz")
    email.send()
    print "Fertig"
    print

    # Komplexeres Beispiel mit Umlauten und Anhaengen
    from simplemail import Email

    print "Komplexeres Beispiel mit Umlauten und Anhaengen"
    print "-----------------------------------------------"
    email = Email(
        smtp_server = "gps.gp"
    )

    # Absender
    email.from_address = "server@gps.gp"
    email.from_caption = "Gerolds Server"

    # Antwort an
    email.reply_to_address = "gerold@gps.gp"
    email.reply_to_caption = "Gerold Penz (Antwortadresse)"

    # Empfaenger
    email.recipients.add("gerold@gps.gp", "Gerold Penz (lokal)")
    # Zum Testen wird hier eine unbekannte Adresse eingeschoben.
    email.recipients.add("unbekannte-adresse@gps.gp", "UNBEKANNT")

    # Betreff
    email.subject = "Komplexeres Beispiel"

    # Nachricht
    email.message = (
        "Das ist ein etwas komplexeres Beispiel\n"
        "\n"
        "Hier steht normaler Text mit Umlauten (öäüß).\n"
        "Groß kann man sie auch schreiben -- ÖÄÜ.\n"
        "\n"
        "mfg\n"
        "Gerold\n"
        ":-)"
    )

    # Anhaenge (die Pfade sind an meine Testsysteme angepasst)
    if sys.platform.startswith("win"):
        filename1 = r"H:\GEROLD\Bilder und Videos\Blumencorso Seefeld 2006\000013.JPG"
        filename2 = r"H:\GEROLD\Bilder und Videos\Blumencorso Seefeld 2006\000018.JPG"
    else:
        filename1 = "/home/gerold/GEROLD/Bilder und Videos/Blumencorso Seefeld 2006/000013.JPG"
        filename2 = "/home/gerold/GEROLD/Bilder und Videos/Blumencorso Seefeld 2006/000018.JPG"
    if os.path.isfile(filename1):
        email.attachments.add_filename(filename1)
        email.attachments.add_filename(filename2)

    # Senden und Statusmeldungen anzeigen
    if email.send():
        if email.recipients.count() == 1:
            print "Die Nachricht wurde erfolgreich an den Empfaenger versendet."
        else:
            if email.statusdict:
                print \
                    "Die Nachricht wurde mindestens an einen der Empfaenger " + \
                    "versendet.\nEs sind aber auch Fehler aufgetreten:"
                for item in email.statusdict:
                    print "  Adresse:", item, "Fehler:", email.statusdict[item]
            else:
                print \
                    "Die Nachricht wurde an alle Empfaenger " + \
                    "erfolgreich versendet."
    else:
        print "Die Nachricht wurde nicht versendet."

    print "Fertig"
    print

    # HTML-Email
    from simplemail import Email

    print "HTML-Email"
    print "----------"
    email = Email(
        from_address = "server@gps.gp",
        smtp_server = "gps.gp",
        to_address = "gerold@gps.gp",
        header = {"Reply-To": "gerold@gps.gp"},
    )
    email.subject = "Das ist ein HTML-Email"
    email.content_subtype = "html"
    email.message = \
        "<h1>Das ist die Überschrift</h1>\n" + \
        "<p>\n" + \
        "  Das ist ein <b>kleiner</b><br />\n" + \
        "  Absatz.\n" + \
        "</p>\n" + \
        "<p>\n" + \
        "  Das ist noch ein <i>Absatz</i>.\n" + \
        "</p>\n" + \
        "<p>\n" + \
        "  mfg<br />\n" + \
        "  Gerold<br />\n" + \
        "  :-)\n" + \
        "</p>"
    if email.send():
        print "Die Nachricht wurde gesendet."
    else:
        print "Die Nachricht wurde nicht versendet."

    print "Fertig"
    print

    ## Googlemail-Email-Beispielcode
    #from simplemail import Email
    #
    #Email(
    #    from_address = "EMAILNAME@gmail.com",
    #    to_address = "EMPFAENGER@domain.xx",
    #    subject = "Googlemail Test",
    #    message = "Das ist ein Googlemail Test.",
    #    smtp_server = "smtp.googlemail.com:587",
    #    smtp_user = "EMAILNAME", # Emailadresse ohne "@gmail.com"
    #    smtp_password = "PASSWORT",
    #    use_tls = True # Muss auf True gesetzt sein
    #).send()


if __name__ == "__main__":
    # Wenn dieses Modul mit dem Parameter "test" aufgerufen wird,
    # dann werden Test-Emails gesendet.
    if "test" in sys.argv[1:]:
        test()

