# from flask import Flask, request
# import excel_tools

# application = Flask(__name__)

# @application.route("/")
# def hello():
#     x = excel_tools.foo(3)
#     return f"Hi, Welcome to the locator app version {x}."


##############################################################################
from flask import Flask, request
import excel_tools
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



@application.route("/")
def hello():
    x = excel_tools.foo(3)
    send()
    return f"Hi, Welcome to the locator app version {x}."
  
def send():
    mail_content = '''Hello,
    This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    Thank You'''
    #The mail addresses and password
    sender_address = 'yishaihazi@gmail.com'
    sender_pass = 'oranmmo1992'
    receiver_address = 'yishaihazi@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')    

##############################################################################






