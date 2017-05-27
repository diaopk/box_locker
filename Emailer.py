#!/usr/...
# This script defines an Email object to handle everything about sending receiving emails

# Import required modules and libraries
import os
from smtplib import *
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from string import join
from poplib import POP3_SSL
from email import message_from_string

class Email:
    def __init__(self):
        # Define email addresses
        self.__admin_addr = 'junliliang1214@gmail.com'
        self.__pass = '%!&#!^^%!yyzaA'
        self.to_addr_caroline = '@gmail.com'
        self.to_addr_junli = 'diaopkaique@gmail.com'
        self.to_addr_louise = '@gmail.com'

        self.msg = MIMEMultipart()

        """
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
        """
    # Method to send an email
    def send(self, photo=None, to_addr=None, body=None):
        # Set up an address to deliver
        if to_addr is not None:
            self.__to_addr = to_addr
        else:
            self.__to_addr = self.to_addr_junli

        # Set up header information
        self.msg['From'] = self.__admin_addr
        self.msg['To'] = self.__to_addr
        self.msg['Subject'] = 'Security info'

        # If send with the photo
        if photo is not None and body is None: 
            # Set up an image
            datetime = photo.get_datetime()
            path = photo.get_path()
            self.img = open(path, 'rb').read()
            
            # Set up the body
            body = "Someone tried to access the box without permission at %s" % (datetime)

            # Set up the attachment
            self.msg.attach(MIMEText(body, 'plain'))
            self.image = MIMEImage(self.img, name=os.path.basename(path))
            self.msg.attach(self.image)
        
        # If send with new pin
        elif photo is None and body is not None:
            self.msg.attach(MIMEText(body, 'plain'))

        # Send the the email
        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.__admin_addr, self.__pass)
        text = self.msg.as_string()
        server.sendmail(self.__admin_addr, self.__to_addr, text)
        server.quit()
    
    # Method to receive an email
    # and return the content
    def receive(self):
        # Body to be returned
        body = "NO"

        # Login the admin email
        server = POP3_SSL('pop.gmail.com')
        server.user(self.__admin_addr)
        server.pass_(self.__pass)
        
        # Get the latest mail
        latest_mail_index = server.stat()[0]
        print latest_mail_index
        latest_mail = server.retr(latest_mail_index)[1]
        text = join(latest_mail, '\n') # Make email content a string
        messages = message_from_string(text) # Make text string a Message object
        #server.quit() # Quit the server

        # Vertify email addresses from senders
        if self.__to_addr_caroline in messages['From'] or self.__to_addr_junli in messages['From'] or self.__to_addr_louise in messages['From']:
            for msg in messages.walk():
                if msg.get_content_type():
                    # if everyting is fine 
                    # the body is the pin from emails
                    body = msg.get_payload(decode=True)

        # Format the body
        # the email body should be something like
        # <div dir="ltr">...body content...</div>
        # Format the body content to get the content
        if len(body.split('<div dir="ltr">')) > 1:
            body = body.split('<div dir="ltr">')[1]
            if len(body.split('</div>')) > 1:
                body = body.split('</div>')[0]
                if body.isdigit() and len(body) == 4:
                    return body
                else:
                    return "NO"
            else:
                return "NO"
        else:
            return body

# --- End of the class ---
