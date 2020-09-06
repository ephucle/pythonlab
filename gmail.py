#!/usr/bin/env python3
#https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
import smtplib
import json, sys, os
with open(os.getenv("HOME")+ os.sep +"netrc.json") as json_file:
	data = json.load(json_file)

gmail_user = data['login']
gmail_password = data['password']

sent_from = gmail_user
to = ['lephuchoang@gmail.com', 'hoang.p.le@ericsson.com']
subject = 'Super Important Message from python gmail'
body = 'Hello World !!!'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print ('Email sent! to \n', "\n".join(to))
except:
    print ('Something went wrong...')