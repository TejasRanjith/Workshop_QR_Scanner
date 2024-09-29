import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.utils import formataddr
from email import encoders
import openpyxl

name="NULL"

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
# os.environ['tester']='hiiii'
# print(os.environ.get('TESTER2'))
# print(os.environ.get('windir'))

def send_email(sender_email,sender_password,receiver_email, i,name):
    qrcode='{float: right;width: 150px;height: 150px;}'
    body='{font-family: Arial, sans-serif;text-align: center;}'
    ticket='{border: 2px solid black;padding: 20px;width: 400px;margin: 20px auto;}'
    ticket_header='{font-weight: bold;font-size: 18px;}'
    ticket_details='{margin-top: 10px;}'

    html_content=f'''
    <!DOCTYPE html>
    <html>
    <head>
      <title>Your Registration Ticket</title>
      <style>
        .qr-code {
          qrcode
        }

        body {
          body
        }

        .ticket {
          ticket
        }

        .ticket-header {
          ticket_header
        }

        .ticket-details {
          ticket_details
        }
      </style>
    </head>
    <body>
      <h3>Points to note</h3>
        <p>1. Don't forget: Make sure to bring your laptop.</p>
        <p>2. Please bring extension cords to accommodate workshop setup.</p>
        <p>3. If you have any questions, please contact us.</p>
      <h3>Your Registration Ticket</h3>
      <div class="ticket">
        <div class="ticket-header">Your Registration Ticket</div>
        <div class="ticket-details">
          <div class="qr-code">
            <img src="cid:image1" alt="QR Code">
          </div>
          <p><b>Name:</b> {name}</p>
          <p><b>Event:</b> CyberSecurity WorkShop</p>
          <p><b>Date:</b> 30th September 2024</p>
          <p><b>Time:</b> 10:00 AM</p>
          <p><b>Location:</b> Decenial Hall</p>
        </div>
      </div>
    </body>
    </html>
    '''
    message = MIMEMultipart("related")  # "related" is necessary for embedding images
    message["From"] = formataddr(("AIDA TEAM", sender_email))
    message["To"] = receiver_email
    message["Subject"] = "Your Ticket to CyberSecurity Workshop - Confirmation and Event Details"
    message.attach(MIMEText(html_content, "html"))
    with open(f"images/qr_code{i}.png", "rb") as image_file:
        img = MIMEImage(image_file.read())
        img.add_header('Content-ID', '<image1>')
        img.add_header('attachement','TestImage.png')
        message.attach(img)
    with open(f"banner.png", "rb") as image_file:
        img = MIMEImage(image_file.read())
        img.add_header('Content-ID', '<image2>')
        img.add_header('attachement','TestImage.png')
        message.attach(img)
    message.attach(MIMEImage(open(f"images/qr_code{i}.png", "rb").read()))
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
            message=None
    except Exception as e:
        print("Error sending email:", e)

def read_all_emails(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    return data

# info = read_all_emails("data.xlsx")
# for i in range(len(info)):
#     if info[i][1] == info[i][7]:
#         send_email("emptyyyyy", "emptyyyyy", info[i][1], i, info[i][2])
#     else:
#         send_email("emptyyyyy", "emptyyyyy", info[i][1], i, info[i][2])
#         send_email("emptyyyyy", "emptyyyyy", info[i][7], i, info[i][2])
send_email('tejasranjith035611@gmail.com','xkxj kvxv baie ulwl','tejascoder035611@gmail.com',2,'Tejas')
# sachinraj2323@gmail.com
# send_email('tejasranjith035611@gmail.com','xkxj kvxv baie ulwl','sachinraj',2,'Tejas')
