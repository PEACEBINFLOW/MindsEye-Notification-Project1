import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mindseye_email(to_email, subject, body):
    sender_email = "your-email@example.com"
    sender_password = "your-email-password"
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    
    message.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

subject = "MindsEye Notification Example"
body = "This is an automated message demonstrating how MindsEye can handle notifications!"
to_email = "recipient@example.com"

send_mindseye_email(to_email, subject, body)
