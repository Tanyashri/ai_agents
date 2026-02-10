import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secrets import sender_email, receiver_email, password

def send_email(receiver_email: str, content: str) -> str:
    """Sends an email to the receiver_email with the given content."""
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = "Test Email from Python 🚀"

        # Use the content parameter instead of hardcoded body
        body = content 
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP server
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Error sending email: {e}"

if __name__ == "__main__":
    send_email(receiver_email, "I LOVE YOU MY PRETTYY LADYY!!!")