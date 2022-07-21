#! python3
# sendEmail.py - send email to recipient.

import datetime, ssl, smtplib
from email.message import EmailMessage

email_sender = "testpythonautomation2@gmail.com"
email_password = "kovpelxfvrxnqdlr"
email_receiver = "dconcio@yondu.com"

#timestamp
timenow = str(datetime.datetime.now().strftime("%b_%d_%Y-%I_%M_%p"))

subject = "Intervals Filing Report for " + timenow

body = """
Successfully Filed Intervals Today :D
"""
#set email properties
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

#SSL
context = ssl.create_default_context()

#Send Email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())