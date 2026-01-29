import random

# register
print("Register")
email = input("Enter your email: ")
password = input("Enter your password: ")

# Login
print("Login")
log_email =input("Enter your email: ")
log_password = input("Enter your password: ")

if log_email == email and log_password == password:
    print("email and password correct")   
    otp_code = random.randrange(00000, 99999)
    print("Your OTP code: ", otp_code)
    ver_otp_code = int(input("verify OTP code: "))
    if ver_otp_code == otp_code :
        print("Login successful") 
else :
    print("email and password incorrect")
    
