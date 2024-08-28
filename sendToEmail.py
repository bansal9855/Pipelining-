import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

def send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, directory_path):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    # Check if the given path is a directory
    if os.path.isdir(directory_path):
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Check if it's a file before attempting to read
            if os.path.isfile(file_path):
                with open(file_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={filename}")
                message.attach(part)
            else:
                print(f"Skipping {file_path} because it's not a file.")
    else:
        print(f"The provided path {directory_path} is not a directory.")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully with attachments!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server.quit()

if len(sys.argv) < 3:
    print(f"Usage: python script_name.py <directory_path> <receiver_email>")
    sys.exit(1)

sender_email = "lbansal1_be22@thapar.edu"
load_dotenv()
sender_password =os.getenv("password") 
receiver_email = sys.argv[2]
subject = "Zip images"
body = "attached zip file"
directory_path = sys.argv[1]

send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, directory_path)
