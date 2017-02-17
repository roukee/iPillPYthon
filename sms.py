# we import the Twilio client from the dependency we just installed
from twilio.rest import TwilioRestClient

# the following line needs your Twilio Account SID and Auth Token
client = TwilioRestClient("AC8c7f201927d27009265665e3dfc38ef7", "1bcee3861b024a73e3f8062e417c9551")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+491629460529", from_="+4915735991573", 
                       body="Tabletten von Max Mustermann wurden nicht genommen!")

