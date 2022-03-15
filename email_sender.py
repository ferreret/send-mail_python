import smtplib
import sys
from email.message import EmailMessage

password = sys.argv[1]

email = EmailMessage()
email['from'] = 'Nicolás Barceló'
email['to'] = 'ferreret@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ferreret.develop@gmail.com', password)
    smtp.send_message(email)
    print('All good boss!')
