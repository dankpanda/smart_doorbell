import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'psefinalproject@gmail.com' #THIS EMAIL IS FOR OUR RASPBERRY TO SEND
GMAIL_PASSWORD = 'pervasive1'

class Emailer:
    def sendmail(self,recipient,subject,content,file):

        message = MIMEMultipart()
        message["From"] = GMAIL_USERNAME
        message["To"] = recipient
        message['Subject'] = subject
        
        body = MIMEText(content)
        message.attach(body)

        attachment = open(file,'rb')
        obj = MIMEBase('application','octet-stream')
        obj.set_payload((attachment).read())
        encoders.encode_base64(obj)
        obj.add_header('Content-Disposition',"attachment; filename= "+file)

        message.attach(obj)

        mymessage = message.as_string()

        # headers = ["From:"+GMAIL_USERNAME,"Subject:"+subject,"To:"+recipient,
        # "MIME-Version:1.0","Content-Type:text/html"]
        # headers="\r\n".join(headers)

        session = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        session.login(GMAIL_USERNAME,GMAIL_PASSWORD)

        session.sendmail(GMAIL_USERNAME,recipient,mymessage+ "\r\n\r\n"+ content)
        session.quit


# while True:
#     if #ADD THE EVENT FOR WHEN YOUR button is pressed:

#TAKE PICTURE IF DETECTED MOVEMENT, AND ADD FILE TO THIS VARIABLE
        # file = "IMAGE.png"

        # sendTo="radisahussein@gmail.com" #CHANGE THIS EMAIL TO USER EMAIL
        # emailSubject="HOME ALERT NOTIFICATION!"
        # emailContent="We detected movement from our device! \nBelow is a snapshot:"
        # sender.sendmail(sendTo,emailSubject,emailContent,file)
        # print("Email Sent")
        # time.sleep(0.1)
    


#TESTING ===========================

#TAKE PICTURE IF DETECTED MOVEMENT, AND ADD FILE TO THIS VARIABLE
# file = "IMAGE.png"

# sendTo="ros2nd@gmail.com" #CHANGE THIS EMAIL TO USER EMAIL
# emailSubject="HOME ALERT NOTIFICATION!"
# emailContent="Someone has pushed your doorbell button! \nBelow is a snapshot:"
# sender.sendmail(sendTo,emailSubject,emailContent, file)
# print("Email Sent")
    
# time.sleep(0.1)
