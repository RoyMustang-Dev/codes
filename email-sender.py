import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = 'Aditya Mishra'
email['to'] = 'adityamishra0996@gmail.com'
email['subject'] = 'Won 1000000$'

email.set_content('I am a Data Scientist!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('learn.coding0996@gmail.com','LEARN0996@@')
    smtp.send_message(email)
    print('email sent')
