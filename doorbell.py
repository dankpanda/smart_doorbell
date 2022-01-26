# Imports
import time
import os
import signal
import subprocess
import uuid
from gpiozero import Button
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from testing import Emailer
from picamera import PiCamera

# Variables
button_GPIO = 16
meeting_duration = 90 # in seconds
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'psefinalproject@gmail.com' #THIS EMAIL IS FOR OUR RASPBERRY TO SEND
GMAIL_PASSWORD = 'pervasive1'
sender = Emailer()
camera = PiCamera()
class Doorbell:
    def __init__(self, button_gpio, emailer, camera):
        self._button = Button(button_gpio)
        self._busy = False
        self.emailer = emailer
        self.camera = camera
        self._loop()
    
    def _loop(self):
        while(True):
            self._button.wait_for_press()
            if(self._busy == False):
                self._busy = True
                
                self._start_video_call()
    
    def _start_video_call(self):
        self.camera.capture("IMAGE.png")
        self.emailer.sendmail("nakamarujc@gmail.com", "DOORBELL NOTIFICATION", "Someone has pushed your doorbell button! \nBelow is a snapshot:", "IMAGE.png")
        meeting_id = str("rardohernando")
        meeting_link = "http://meet.jit.si/{}#config.prejoinPageEnabled=false".format(meeting_id)
        process = subprocess.Popen(["chromium", "-kiosk",meeting_link])
        time.sleep(meeting_duration)
        self._end_video_call(process)

    def _end_video_call(self,process):
        self._busy = False
        os.kill(process.pid,signal.SIGTERM)
    


if __name__ == "__main__":
    doorbell = Doorbell(button_GPIO, sender, camera)