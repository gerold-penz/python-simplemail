#!/usr/bin/env python
# coding: utf-8
"""
Python-Simplemail sends emails with and without attachments

By Gerold - http://halvar.at/

Example::

    from simplemail import Email
    Email(
        from_address = "sender@domain.at",
        to_address = "recipient@domain.at",
        subject = "This is the subject",
        message = "This is the short message body."
    ).send()
"""

import os.path
import sys
import time
import smtplib
import mimetypes
import email
import email.header
from email.message import Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage


# Exceptions
class SimpleMailException(Exception):
    """SimpleMail Base-Exception"""
    def __str__(self):
        return self.__doc__


class NoFromAddressException(SimpleMailException):
    """No sender address"""
    pass


class NoToAddressException(SimpleMailException):
    """No recipient address"""
    pass


class NoSubjectException(SimpleMailException):
    """No subject"""
    pass


class AttachmentNotFoundException(SimpleMailException):
    """Attachment not found"""
    def __init__(self, filename = None):
        if filename:
            self.__doc__ = 'Attachment not found: "%s"' % filename


# UTF-8 encoded emails should not be Base64-coded. Quoted-printable is a better choice.
email.charset.add_charset("utf-8", email.charset.QP, email.charset.QP, "utf-8")


class Attachments(object):
    """Email attachments"""

    def __init__(self):
        self._attachments = []


    def add_filename(self, filename = ''):
        """Adds a new attachment"""
        
        self._attachments.append(filename)


    def count(self):
        """Returns the number of attachments"""
        
        return len(self._attachments)


    def get_list(self):
        """Returns the attachments, as list"""
        
        return self._attachments


class Recipients(object):
    """Email recipients"""

    def __init__(self):
        self._recipients = []


    def add(self, address, caption = u""):
        """
        Adds a new address to the list of recipients

        :param address: email address of the recipient
        :param caption: caption (name) of the recipient
        """

        # ToDo: Die Umwandlung sollte später mal, nicht mehr hier, sondern erst
        # beim Verwenden des Empfängers umgewandelt werden. Dann weiß man
        # das gewünschte Encoding. Das Encoding muss ich hier leider fest
        # im Quellcode verankern. :-(
        if isinstance(caption, unicode):
            caption = str(email.header.Header(caption, charset = "utf-8"))
        self._recipients.append(email.utils.formataddr((caption, address)))


    def count(self):
        """Returns the quantity of recipients"""

        return len(self._recipients)


    def __repr__(self):
        """Returns the list of recipients, as string"""

        return str(self._recipients)


    def get_list(self):
        """Returns the list of recipients, as list"""

        return self._recipients


class CCRecipients(Recipients):
    """Carbon copy recipients"""
    pass


class BCCRecipients(Recipients):
    """Blind carbon copy recipients"""
    pass


class Email(object):
    """One email, which can sent with the 'send'-method"""

    def __init__(
        self,
        from_address = "",
        from_caption = "",
        to_address = "",
        to_caption = "",
        subject = "",
        message = "",
        smtp_server = "localhost",
        smtp_user = "",
        smtp_password = "",
        attachment_file = "",
        user_agent = "",
        reply_to_address = "",
        reply_to_caption = "",
        use_tls = False,
        header = None,
    ):
        """
        Initializes the email object

        :param from_address: the email address of the sender
        :param from_caption: the caption (name) of the sender
        :param to_address: the email address of the recipient
        :param to_caption: the caption (name) of the recipient
        :param subject: the subject of the email message
        :param message: the body text of the email message
        :param smtp_server: the ip-address or the name of the SMTP-server
        :param smtp_user: (optional) Login name for the SMTP-Server
        :param smtp_password: (optional) Password for the SMTP-Server
        :param user_agent: (optional) program identification
        :param reply_to_address: (optional) Reply-to email address
        :param reply_to_caption: (optional) Reply-to caption (name)
        :param use_tls: (optional) True, if the connection should use TLS to encrypt.
        :param header: (optional) Additional header fields as dictionary.
            You can use this parameter to add additional header fields.
            Allready (internal) used header fields are: "From", "Reply-To", "To",
            "Cc", "Date", "User-Agent" and "Subject". (case sensitive)
            The items of this dictionary replace internal used header fields.
        """

        self.from_address = from_address
        if isinstance(from_caption, unicode):
            from_caption = str(email.header.Header(from_caption, charset = "utf-8"))
        self.from_caption = from_caption
        self.recipients = Recipients()
        self.cc_recipients = CCRecipients()
        self.bcc_recipients = BCCRecipients()
        if to_address:
            self.recipients.add(to_address, to_caption)
        self.subject = subject
        self.message = message
        self.smtp_server = smtp_server
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.attachments = Attachments()
        if attachment_file:
            self.attachments.add_filename(attachment_file)
        self.content_subtype = "plain"
        self.content_charset = "utf-8"
        self.header_charset = "us-ascii"
        self.statusdict = None
        if user_agent:
            self.user_agent = user_agent
        else:
            self.user_agent = (
                "SimpleMail Python/%s (http://www.python-forum.de/post-18144.html)"
            ) % sys.version.split()[0]
        self.reply_to_address = reply_to_address
        if isinstance(reply_to_caption, unicode):
            reply_to_caption = str(
                email.header.Header(reply_to_caption, charset = "utf-8")
            )
        self.reply_to_caption = reply_to_caption
        self.use_tls = use_tls
        self.header_fields = header or {}


    def send(self):
        """
        de: Sendet die Email an den Empfaenger.
            Wird das Email nur an einen Empfaenger gesendet, dann wird bei
            Erfolg <True> zurueck gegeben. Wird das Email an mehrere Empfaenger
            gesendet und wurde an mindestens einen der Empfaenger erfolgreich
            ausgeliefert, dann wird ebenfalls <True> zurueck gegeben.

            Wird das Email nur an einen Empfaenger gesendet, dann wird bei
            Misserfolg <False> zurueck gegeben. Wird das Email an mehrere
            Empfaenger gesendet und wurde an keinen der Empfaenger erfolgreich
            ausgeliefert, dann wird <False> zurueck gegeben.
        """

        #
        # pruefen ob alle notwendigen Informationen angegeben wurden
        #
        if len(self.from_address.strip()) == 0:
            raise NoFromAddressException()
        if self.recipients.count() == 0:
            if (
                (self.cc_recipients.count() == 0) and
                (self.bcc_recipients.count() == 0)
            ):
                raise NoToAddressException()
        if len(self.subject.strip()) == 0:
            raise NoSubjectException()

        #
        # Wenn die Nachricht oder Subject UNICODE sind,
        # dann nach self.content_charset umwandeln
        #
        if isinstance(self.subject, unicode):
            if self.header_charset.lower() != "us-ascii":
                self.subject = self.subject.encode(self.header_charset)
        if isinstance(self.message, unicode):
            self.message = self.message.encode(self.content_charset)

        #
        # Email zusammensetzen
        #
        if self.attachments.count() == 0:
            # Nur Text
            msg = MIMEText(
                _text = self.message,
                _subtype = self.content_subtype,
                _charset = self.content_charset
            )
        else:
            # Multipart
            msg = MIMEMultipart()
            if self.message:
                att = MIMEText(
                    _text = self.message,
                    _subtype = self.content_subtype,
                    _charset = self.content_charset
                )
                msg.attach(att)

        assert isinstance(msg, Message)

        # Empfänger, CC, BCC, Absender, User-Agent, Antwort-an
        # und Betreff hinzufügen
        from_str = email.utils.formataddr((self.from_caption, self.from_address))
        msg["from"] = from_str
        if self.reply_to_address:
            reply_to_str = email.utils.formataddr(
                (self.reply_to_caption, self.reply_to_address)
            )
            msg["reply-to"] = reply_to_str
        if self.recipients.count() > 0:
            msg["to"] = ", ".join(self.recipients.get_list())
        if self.cc_recipients.count() > 0:
            msg["cc"] = ", ".join(self.cc_recipients.get_list())
        msg["date"] = email.utils.formatdate(time.time())
        msg["user-agent"] = self.user_agent
        try:
            msg["subject"] = email.header.Header(
                self.subject, self.header_charset
            )
        except UnicodeDecodeError:
            msg["subject"] = email.header.Header(
                self.subject, self.content_charset
            )
        # User defined header_fields
        if self.header_fields:
            for key, value in self.header_fields.items():
                msg[key] = value

        msg.preamble = "You will not see this in a MIME-aware mail reader.\n"
        msg.epilogue = ""

        # Falls MULTIPART --> zusammensetzen
        if self.attachments.count() > 0:
            for filename in self.attachments.get_list():
                # Pruefen ob Datei existiert
                if not os.path.isfile(filename):
                    raise AttachmentNotFoundException(filename = filename)
                # Datentyp herausfinden
                ctype, encoding = mimetypes.guess_type(filename)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                if maintype == 'text':
                    fp = file(filename)
                    # Note: we should handle calculating the charset
                    att = MIMEText(fp.read(), _subtype=subtype)
                    fp.close()
                elif maintype == 'image':
                    fp = file(filename, 'rb')
                    att = MIMEImage(fp.read(), _subtype=subtype)
                    fp.close()
                elif maintype == 'audio':
                    fp = file(filename, 'rb')
                    att = MIMEAudio(fp.read(), _subtype=subtype)
                    fp.close()
                else:
                    fp = file(filename, 'rb')
                    att = MIMEBase(maintype, subtype)
                    att.set_payload(fp.read())
                    fp.close()
                    # Encode the payload using Base64
                    email.Encoders.encode_base64(att)
                # Set the filename parameter
                att.add_header(
                    "Content-Disposition",
                    "attachment",
                    filename = os.path.split(filename)[1].strip()
                )
                msg.attach(att)

        #
        # Am SMTP-Server anmelden
        #
        smtp = smtplib.SMTP()
        if self.smtp_server:
            smtp.connect(self.smtp_server)
        else:
            smtp.connect()

        # TLS-Verschlüsselung
        if self.use_tls:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

        # authentifizieren
        if self.smtp_user:
            smtp.login(user = self.smtp_user, password = self.smtp_password)

        #
        # Email versenden
        #
        self.statusdict = smtp.sendmail(
            from_str,
            (
                self.recipients.get_list() +
                self.cc_recipients.get_list() +
                self.bcc_recipients.get_list()
            ),
            msg.as_string()
        )
        smtp.close()

        # Rueckmeldung
        return True


