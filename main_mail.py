from mail_correct import Mail

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"
login = 'login@gmail.com'
password = 'qwerty'


if __name__ == '__main_mail__':
    mail = Mail()
    mail.send_message('Hey!', login, password)
    mail.receive_message(login, password)
