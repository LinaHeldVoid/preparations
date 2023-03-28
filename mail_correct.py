import email
import imaplib

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"
login = 'login@gmail.com'
password = 'qwerty'


class Mail:

    def send_message(self, data, login, password):
        login = login
        password = password
        ms.login(login, password)
        subject = 'Subject'
        recipients = ['vasya@email.com', 'petya@email.com']
        message = data
        header = None
        msg = MIMEMultipart()
        msg['From'] = login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

    def receive_message(self, login, password):
        login = login
        password = password
        header = None
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(login, password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
