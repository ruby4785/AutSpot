from twilio.rest import Client
account_sid = "AC67c7e90f107213ca1855d2fd2d1c9e4d"
auth_token = "9849fa2fb4cc4c8661e3494e7420dc46"
client = Client(account_sid, auth_token)
def send_alert(emg_contact):
    message = client.messages.create(body = "Your contact is having an autism  episode", from_ = '+18559254969', to = emg_contact)
    print(message.sid)