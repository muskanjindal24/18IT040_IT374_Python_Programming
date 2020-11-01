from twilio.rest import Client
account_sid = 'ACf01f89256a514e843fd054bab7232e16'
auth_token = '20bd4a826a499c79c8965c81f0648023'
client = Client(account_sid, auth_token)
message = client.messages.create(from_='+12018907702',body ='Hey, Muskan here!',to ='+919016231815')
print(message.sid)