from datetime import date, datetime
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mail_content = '''Hello,
In this email we have attached the report.
Thank You
'''

#The mail addresses and password
sender_address = 'redserver78@gmail.com'
sender_pass = 'sqa123red'
#sender_pass = input("enter password")
receiver_address = 'vinasa67.vr@gmail.com'

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
#d1 = datetime.now()
message['Subject'] = "FiberSafe Report "+ str(date.today())

#The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))

attach_file_name = 'report1.html'
# Open the file as binary mode
with open(attach_file_name, 'rb') as attachment:
#attach_file = open(attach_file_name, 'rb') 
    payload = MIMEBase('application', 'octet-stream')
    payload.set_payload(attachment.read())
#encode the attachment
encoders.encode_base64(payload) 

#add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')