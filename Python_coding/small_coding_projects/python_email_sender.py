# go over our email account and setup 3 factor authentication
# generate app password
#  create a function to send email
import ssl
import smtplib
from email.message import EmailMessage
from app2 import password

email_sender = 'allohnkeforr@gmail.com'
email_password = password

email_receiver = 'allohnkeforrodrick@gmail.com'
subject = 'Nobleman testing the email'
body = """
The Noble man is testing the backend of email system
this is cool, to the Noble man
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())



