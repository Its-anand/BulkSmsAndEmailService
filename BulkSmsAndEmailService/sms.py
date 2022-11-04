# works with both python 2 and 3
from __future__ import print_function


import africastalking

class SMS:
    def __init__(self):
            # Set your app credentials
            self.username = "sandbox"
            self.api_key = "50f74bfd1bbececd64c74f681a63c60e4b75b90bec701810ecdb7ece93f373b5"

            # Initialize the SDK
            africastalking.initialize(self.username, self.api_key)

            # Get the SMS service
            self.sms = africastalking.SMS

    def send(self):
            # Set the numbers you want to send to in international format
            recipients = ["+917049011575","+918815594055"]
#+91 (976) 006-4000 
            # Set your message
            message = "hello"

            # Set your shortCode or senderId
            sender = "104"
            try:
				# Thats it, hit send and we'll take care of the rest.
                response = self.sms.send(message, sender,recipients)
                print (response)
            except Exception as e:
                print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send()