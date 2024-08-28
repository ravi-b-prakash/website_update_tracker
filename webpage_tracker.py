import requests
import hashlib
import time
import smtplib
webpage = input("enter webpage: ")
sender_email = input("enter sender email address: ")
sender_password = input("enter sender email password: ")
receiver_email = input("enter reciever email: ")
x = requests.get(webpage)
result = hashlib.sha256(x.text.encode())
hash = result.hexdigest()
print(hash)

while(True):
    x = requests.get(webpage)
    result = hashlib.sha256(x.text.encode())
    print(hash)
    if result.hexdigest() != hash:
        print("webpage has been updated.")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, sender_password)
        message = "webpage has been updated."
        s.sendmail(sender_email, receiver_email, message)
        s.quit()
        hash = result.hexdigest()
    else:
        pass
    time.sleep(2)
