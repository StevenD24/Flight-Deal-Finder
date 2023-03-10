from twilio.rest import Client

TWILIO_SID = "ENTER TWILIO SID HERE"
TWILIO_TOKEN = "ENTER TWILIO TOKEN HERE"
TWILIO_PHONE_NUM = "ENTER TWILIO PHONE NUM HERE"
TWILIO_VERI_NUM = "ENTER PHONE NUM THAT RECEIVES SMS HERE"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_sms(self, msg):
        msg = self.client.messages.create(
            body=msg,
            from_=TWILIO_PHONE_NUM,
            to=TWILIO_VERI_NUM
        )
        print(msg.sid)
