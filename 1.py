import random
import smtplib
from email.message import EmailMessage
otp_code = random.randrange(00000, 99999)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

from_mail = 'rsaoudi461@gmail.com'
server.login(from_mail, 'hfdn zqoa pboq upnc')
to_mail = input("enter your email: ")

msg = EmailMessage()
msg['subject'] = "OTP verification"
msg['from'] = from_mail
msg['to'] = to_mail
msg.set_content("Your OTP code: "+ str(otp_code))
server.send_message(msg)

print("Email sent")