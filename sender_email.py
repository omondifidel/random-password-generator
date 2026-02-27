import smtplib
from email.message import EmailMessage

email = EmailMessage()

# Fix the key (removed the space after 'from')
email['from'] = 'fidelmike03@gmail.com'
email['to'] = 'fidelomondi17@gmail.com'
email['subject'] = 'You are a millionaire in Dollars!'

email.set_content("I am a Python Master")

# Use a context manager for the SMTP connection
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() # Secure the connection
    
    # IMPORTANT: Use an App Password here, NOT your login password
    # Replace 'xxxx xxxx xxxx xxxx' with your generated code
    smtp.login('fidelmike03@gmail.com', 'qzojccoagliizmyy')
    
    smtp.send_message(email)
    print('All Good Boss ✅')