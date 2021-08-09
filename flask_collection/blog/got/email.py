'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Archlinux
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		email.py
  > Created Time:	2016-12-11 Sun 21:16
'''''''''''''''''''''''''''''''''''''''''''''''''''
                default
MAIL_SERVER     localhost
MAIL_PORT       25
MAIL_USE_TLS    False
MAIL_USE_SSL    False
MAIL_USERNAME   None
MAIL_PASSWORD   None

import flask_mail
mail = flask_mail.Mail(app)
message = flask_mail.Message(subject='', recipients=None, body=None, html=None, sender=None, cc=None, bcc=None, attachments=None, reply_to=None, date=None, charset=None, extra_headers=None, mail_options=None, rcpt_options=None)
message.send(mail) or mail.send(message)
