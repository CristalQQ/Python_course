from email.message import EmailMessage
import smtplib

my_email = EmailMessage()

my_email['from'] = 'Vladislav'
my_email['to'] = 'test@gmail.com'
my_email['subject'] = "Hellow from Python"
my_email.set_content("Hey! How are you doing?")

with smtplib.SMTP(host='79.137.205.83', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was sent!")
