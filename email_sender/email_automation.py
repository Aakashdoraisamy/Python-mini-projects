import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html_template = Template(Path('email_sender.html').read_text())
email = EmailMessage()
email['From'] = ''
email['To'] = 'aakashdorai@gmail.com'
email['Subject'] = 'Automated Email from Python Script'

email.set_content('This is a fallback message for email clients that do not support HTML.')
email.add_alternative(html_template.substitute({'name': 'Aakash'}), subtype='html')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ad7545448@gmail.com', 'mxzlatatqyenhuem')
    smtp.send_message(email)
    print('Email sent successfully!')