import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(to,message):
    port = 465

    sender = "pruebasdaw2021@gmail.com"
    domain = "smtp.gmail.com"

    message = MIMEMultipart("alternative")

    html = "<html><body><h1>{}</h1></body></html>".format(message)

    context= ssl.create_default_context()


