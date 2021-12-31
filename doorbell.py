# Imports
import time
import os
import signal
import subprocess
import uuid
from gpiozero import Button

# Variables
button_GPIO = 16
meeting_duration = 60 # in seconds

class Doorbell:
    def __init__(self, button_gpio):
        self._button = Button(button_gpio)
        self._busy = False
        self._loop()
    
    def _loop(self):
        while(True):
            self._button.wait_for_press()
            if(self._busy == False):
                self._busy = True
                self._start_video_call()
    
    def _start_video_call(self):
        meeting_id = str(uuid.uuid4())
        meeting_link = "http://meet.jit.si/{}#config.prejoinPageEnabled=false".format(meeting_id)
        process = subprocess.Popen(["chromium", "-kiosk",meeting_link])
        time.sleep(meeting_duration)
        self._end_video_call(process)

    def _end_video_call(self,process):
        self._busy = False
        os.kill(process.pid,signal.SIGTERM)
    
if __name__ == "__main__":
    doorbell = Doorbell(button_GPIO)


