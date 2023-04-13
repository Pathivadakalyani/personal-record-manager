import smtplib
import random
recpt=input('enter to mail')
otp=random.randint(1242,99999)
#from smtplib import SMTP
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()#Starts the server
server.login('kpathivada6@gmail.com','fhtihhjtflxgbaqh')
server.sendmail('kpathivada6@gmail.com',recpt,'The otp is-'+str(otp))

server.close()
print('mail sent')
otp2=int(input('enter otp'))
if otp==otp2:
    print('the otp is valid')
else:
        print('invalid otp-check your eyesight')
