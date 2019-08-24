import smtplib 
from email.mime.text  import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '52f13587969f53'
    password = 'c3e3681278f424'
    message = f"<h3>New Feedback Submission Mail</h3><ul></i>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li>"

    sender_email = 'email@jmail.com'
    receiver_email = 'emailxd@kmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #Now Send email Configure

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
