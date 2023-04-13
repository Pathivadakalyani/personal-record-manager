import smtplib
#from smtplib import SMTP
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('kpathivada6@gmail.com','fhtihhjtflxgbaqh')
server.sendmail('kpathivada6@gmail.com','madhumanasagurram2001@gmail.com','FROM PYTHON')

server.close()
print('mail sent')
