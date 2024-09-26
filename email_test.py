import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.utils import formataddr
from email import encoders

sender_email = input("Enter Sender_Email:")  # Replace with your actual email
sender_password = input("Enter Sender_Password:")  # Replace with your actual password
receiver_email = input("Enter Receiver_Email:")  # Replace with the email you want to send the email to

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Newsletter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #f8f8f8;
            padding: 20px;
            border-radius: 5px;
            text-align:center;
        }
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #0073e6;
            color: white;
            border-radius: 0 0 5px 5px;
        }
        .footer p {
            margin: 0;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #0073e6;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin-bottom:20px;
            margin-top:20px;
        }
        .button:hover {
            background-color: #005bb5;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="cid:image1" alt="Sample Image" style="width: 100%; border-radius: 5px;">
        <a class="button" href="https://tharang2024.vercel.app/event-details/44">Register Now</a>
        <!-- Footer -->
        <div class="footer">
            <p>&copy; 2024 Your Company. All rights reserved.</p>
            <p>If you no longer wish to receive these emails, <a href="#" style="color: white; text-decoration: underline;">unsubscribe here</a>.</p>
        </div>
    </div>
</body>
</html>

"""

for i in range(1,3):
    message = MIMEMultipart("related")  # "related" is necessary for embedding images
    message["From"] = formataddr(("WORKSHOP", sender_email))
    message["To"] = receiver_email
    message["Subject"] = "QR CODE TESTER"
    message.attach(MIMEText(html_content, "html"))
    with open(f"qr_code{i}.png", "rb") as image_file:
        img = MIMEImage(image_file.read())
        img.add_header('Content-ID', '<image1>')  # This matches the cid in the HTML
        message.attach(img)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
            message=None
    except Exception as e:
        print("Error sending email:", e)


input("presss  enterrrrr")