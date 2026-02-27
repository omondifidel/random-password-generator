import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage() #thi is the email object

email['from'] = 'fidelmike03@gmail.com'
email['to'] = 'fidelomondi17@gmail.com'
email['subject'] = 'You are a millionare in Dollars!'

email.set_content(html.substitute(name= 'Deutch') ,'html')#Here we an set any content we want , text , html , pdf
#we want to use the smtplib to log in to our email client and send our email from there 
with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()#setting up the server we want to run from
    smtp.starttls()#encrytpion mechanism , we cant to connect securely to the server
    smtp.login('fidelmike03@gmail.com', 'qzojccoagliizmyy')#logging in my credentials in the server
    smtp.send_message(email)
    print('All Good Boss✅')