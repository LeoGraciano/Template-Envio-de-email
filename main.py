
# Usando email temporário para test.
# https://mailtrap.io/

from string import Template
from datetime import datetime
from env.dados import LOGIN, PWD

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

SEND = ''
RECEIVER = ''

with open('template.html', 'r') as html:
    template = Template(html.read())
    date_now = (datetime.now()).strftime('%d/%m/%Y %H:%M:%S')
    body_msg = template.safe_substitute(name='Leonardo', date=date_now)

msg = MIMEMultipart()
msg['from'] = 'Quem Envia'
msg['to'] = 'Cliente que recebe'
msg['subject'] = 'Atenção: este é um e-mail de testes.'

body = MIMEText(body_msg, 'html')
msg.attach(body)

# Envio de mensagem de MSG
with open('imagem-teste.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)


with smtplib.SMTP(host='smtp.mailtrap.io', port=2525) as server:
    # server.ehlo()
    # server.starttls()
    server.login(LOGIN, PWD)
    server.send_message(msg)
    server.sendmail(SEND, RECEIVER, msg)
    print('Email Enviado com sucesso')
