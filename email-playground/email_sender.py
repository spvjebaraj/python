import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email["from"] = "Philip"
email["to"] = "philip.jebaraj@hotmail.com"
email["subject"] = 'Email from Python!'

email.set_content(html.substitute({'name': 'Udemy'}), 'html')

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("pv.jebaraj@gmail.com", "blahblah")
    smtp.send_message(email)
    print("all good boss!!!")

# email = EmailMessage()
# email["from"] = "Philip"
# email["to"] = "philip.jebaraj@hotmail.com"
# email["subject"] = 'Email from Python!'

# email.set_content('I am learning Python from Udemy')

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("pv.jebaraj@gmail.com", "blahblah")
#     smtp.send_message(email)
#     print("all good boss!!!")
