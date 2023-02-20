from twilio.rest import Client

TWILIO_SID = "AC87200e152a3ae161e232d6d55eab1cbe"
TWILIO_TOKEN = "1a98e435f02556b8eb5eccaa482c804a"
TWILIO_PHONE_NUM = "19793644145"
TWILIO_VERI_NUM = "15875772189"


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