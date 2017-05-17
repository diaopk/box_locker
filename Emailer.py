#!/usr/...
# This script defines an Email object to handle everything about sending
# emails
# When create a new Instance of Email with required arguments, the instance
# set up everything needed. Call the send() method to send that email

# Import required modules
import os
from smtplib import *
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

class Email:
    def __init__(self, photo):
        self.__admin_addr = 'junliliang1214@gmail.com'
        self.__pass = '%!&#!^^%!yyzaA'
        self.__to_addr = 'diaopkaique@163.com'
        self.msg = MIMEMultipart()
        self.msg['From'] = self.__admin_addr
        self.msg['To'] = self.__to_addr
        self.msg['Subject'] = 'Security Info'

        # Info about the image to be sent
        self.datetime = photo.get_datetime()
        self.path = photo.get_path()
        self.img = open(self.path, 'rb').read()

        # The body of the message
        self.body = 'Someone tried to access the box without permission at ' + self.datetime
        
        # Set up the attachment
        self.msg.attach(MIMEText(self.body, 'plain'))
        self.image = MIMEImage(self.img, name=os.path.basename(self.path)) 
        self.msg.attach(self.image)
    
    # Method to send an email
    def send(self, to_addr=None):
        if to_addr is not None:
            self.__to_addr = to_addr

        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.__admin_addr, self.__pass)
        text = self.msg.as_string()
        server.sendmail(self.__admin_addr, self.__to_addr, text)
        server.quit()

    def quit(self):
        pass
""" Testing code
pm = Photo_Manager()
em = Email(pm.first().get_path(), pm.first().get_datetime())
try:
    em.send()
    print 'It works'
except Exception:
    print 'It does not workRR
    """
