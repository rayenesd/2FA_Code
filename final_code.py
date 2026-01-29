import random
import smtplib
from email.message import EmailMessage

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

from_mail = 'rsaoudi461@gmail.com'
server.login(from_mail, 'hfdn zqoa pboq upnc')

# register
print("Register")
email = input("Enter your email: ")
password = input("Enter your password: ")

# Login
print("Login")
log_email =input("Enter your email: ")
log_password = input("Enter your password: ")

# verification

if log_email == email and log_password == password:
    print("email and password correct")
    otp_code = random.randrange(00000, 99999)
    msg = EmailMessage()
    msg['subject'] = "OTP verification"
    msg['from'] = from_mail
    msg['to'] = email
    msg.set_content("Your OTP code: "+ str(otp_code))
    server.send_message(msg)

    print("Email sent")

    ver_otp_code = int(input("verify OTP code: "))
    if ver_otp_code == otp_code :
        print("Login successful") 
else :
    print("email and password incorrect")





