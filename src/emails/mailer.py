import smtplib,ssl

def send_mail(to,message):
    port = 465

    sender = "pruebasdaw2021@gmail.com"
    domain = "smtp.gmail.com"

    context= ssl.create_default_context()

