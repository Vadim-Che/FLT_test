import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from test_pack.html_former import get_data_html
 
def send_mail():
    # Composing html data for sending
    _msg_html = get_data_html()

    # Checking if data is read
    if ((_msg_html is None) or (_msg_html == "")):
        print("No data read. Exiting")
        return None

    # Requesting main e-mail parameters
    _sender_mail = input("Enter sender's e-mail address: ")
    _target_mail = input("Enter target e-mail address: ")
    #  Standard function getpass doesn't work in any terminal
    #Decided not to spend too much time to find an appropriate non-standard solution
    _password = input("Enter Your password: ")

    # Composing message
    _message = MIMEMultipart()
    _message["Subject"] = "Aircraft data"
    _message["From"] = _sender_mail
    _message["To"] = _target_mail

    # Turn data into html MIMEText objects
    _msg_part = MIMEText(_msg_html, "html")

    # Add HTML part to MIMEMultipart message
    _message.attach(_msg_part)

    # Create secure connection with server and send email
    _context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = _context) as server:
            server.login(_sender_mail, _password)
            server.sendmail(
                _sender_mail, _target_mail, _message.as_string()
                )

        print("Sent successfully")
    except (Exception, smtplib.SMTPException) as error:
        print("Sending error")
        print(error)

 
if __name__ == '__main__':
    send_mail()
