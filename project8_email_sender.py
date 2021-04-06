#!/usr/bin/env python3
#https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
sender_address = 'piraspberryvn@gmail.com'
sender_pass = 'xxxx'
receiver_address = 'hoang.p.le@ericsson.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
print("Start login session...")
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port

session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
print("Login seccessful!")
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')