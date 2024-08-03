from cgitb import text
import email
from http import server
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_user = 'sender mail'
email_send = 'receiving mail'
subject = 'subject'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'body mail'
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, 'password') 

server.sendmail(email_user, email_send, text)
server.quit
