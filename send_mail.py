import smtplib 
from email.mime.text import MIMEText
import os

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = os.environ.get('user-mailtrap')
    password = os.environ.get('pass-mailtrap')
    message = f"<h3>Novo envio de feedback !! </h3><ul><li>Cliente: {customer}</li><li>Revendedor: {dealer}</li><li>Avaliação: {rating}</li><li>Comentários: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'ACME Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())