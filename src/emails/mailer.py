import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_mail(to,message):
    port = 465

    sender = "pruebasdaw2021@gmail.com"
    domain = "smtp.gmail.com"

    context= ssl.create_default_context()

