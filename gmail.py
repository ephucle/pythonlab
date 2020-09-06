#!/usr/bin/env python3
#https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
import smtplib,json
import sys, os


def sendemail(tolist, body, subject):
	try:
		#with open(os.getenv("HOME")+ os.sep +"netrc.json") as json_file:
		with open(os.path.expanduser('~')+ os.sep +"netrc.json") as json_file:
			data = json.load(json_file)
	except:
		print(os.getenv("HOME")+ os.sep +"netrc.json", "does not exist")
	gmail_user = data['login']
	gmail_password = data['password']
	sent_from = gmail_user
	email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(tolist), subject, body)
	print(email_text)
	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		print("Sending email....")
		server.sendmail(sent_from, tolist, email_text)
		server.close()
		print ('Email sent! to:\n', "\n".join(tolist))
	except:
		print ('Something went wrong...')

if __name__ == "__main__":
	sendemail(
		tolist = ['lephuchoang@gmail.com', 'hoang.p.le@ericsson.com'], 
		body="Hello World !!! New ==> main", 
		subject='Message from python gmail==>simplify script'
		)



