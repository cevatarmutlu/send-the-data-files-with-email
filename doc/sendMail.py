import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Send Simple Mail Using Python

msg = MIMEMultipart('alternative')
msg['Subject'] = "Python ile gönderilen maillerden" # Mail Subject
msg['From']    = "cevat1803_korkusuz@hotmail.com" # Mail Sender
msg['To']      = "cevatarmutlu@outlook.com" # Mail Reciever

msg.attach(MIMEText("Bu mail Python ile gönderilmiştir. Evet evet Python ile Gönderilmiştir.", 'plain')) # Mail Message


s = smtplib.SMTP('smtp.live.com', 587) # SMTP HOST and PORT of Mail Service
s.ehlo() # what is this i don't know .
s.starttls() # Güvenlik protokolu olması gerekiyor. 587 portu zaten güvenlik protokolu olan Port. 25. Portta ise SSL ya da TSL yoktu.
s.login('cevat1803_korkusuz@hotmail.com', '11411935') # Your mail address and password
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
print(" - Mail sent. ")
