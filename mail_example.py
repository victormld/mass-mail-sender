#mail server
import smtplib
#security method
import ssl
#mail manage library
from email.message import EmailMessage

#account variables
email_sender = 'sender@gmail.com'
email_password = ''
email_reciver = 'reciver@gmail.com'

#message variables
subject = 'Test'
body = 'lorem'

#instance of the object
em = EmailMessage()

#writes the account variables to the EmailMessage object
em['From'] = email_sender
em['To'] = email_sender
em['Subject'] = email_sender

#writes the actual message
em.set_content(body)

#sets the secure method to send the message
context = ssl.create_default_context()

#seting up the smtp server
#the first parameter is the mail server we are going to use
#then we passes the port and finally the context we have setted up before
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    #the method login() let us sign up to our gmail account passing the mail and password parammeters
    smtp.login(email_sender,email_password)
    #the sendmail() method takes all the prior data to create the message and send it through the smtp server
    smtp.sendmail(email_sender, email_reciver, em.as_string())