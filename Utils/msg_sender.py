import os
import sys
from twilio.rest import Client
sys.path.insert(1, os.path.dirname(__file__)+'/..')
from config import _twilio

def send_message(post):
    client = Client(_twilio._Asid, _twilio._AToken)

    message = client.messages.create(
    body="Your Post " + post + " is ready ;)",
    from_=_twilio._from,
    to=_twilio._to
    )