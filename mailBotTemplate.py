import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import mail_credentials #personal file named mail_credentials.py
### Also have a .csv file saved in the same folder


sender_email = ""#Insert sender name here
html = """\
<html>
    <body>
        <p>
            Dear {name},<br>
            <br>
            THIS IS A SAMPLE EMAIL SENT BY PYTHON<br>
            SAMPLE SAMPLE SAMPLE<br>
            Lets say I am trying to schedule interviews<br>
            I have attached below a link to my weekly schedule. Please let me know a specific date and time that works best for you.<br>
            <br>
            Best,<br>
            <br>
            YOUR NAME WOULD GO HERE<br>
            YOUR UNIVERSITY WOULD GO HERE<br>
            Candidate for YOUR MAJOR WOULD GO HERE<br>
            <a href="tel:5551234567">(555) 123-4567</a> | <a href="mailto:SAMPLE@SAMPLE.COM">NAME OF CLICKABLE LINK</a><br>
            <br>
            <a href="ATTACH GOOGLE CALENDAR LINK IF YOU WANT">Weekly Schedule</a>
        </p>
    </body>
</html>
"""

port = 465 #for SSL


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    ### mail_credentials is a separate file to store email username and password for protection
    ### mail_credentials.py looks something like:
    ### IMAP_USER = 'ENTER EMAIL HERE'
    ### IMAP_PASS = 'ENTER PASSWORD HERE'
    server.login(mail_credentials.IMAP_USER, mail_credentials.IMAP_PASS)
    ### Create a .csv file with following structure:
    ### name, email
    ### NAME1, EMAIL1
    ### NAME2, EMAIL2
    ### and so on...
    with open("INSERT_FILE_NAME_HERE.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for name, email in reader:
            print(f"sending email to {name}")
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = email
            message["Subject"] = "INSERT SUBJECT NAME HERE"
            message.attach(MIMEText(html,"html"))
            server.sendmail(sender_email, email, message.as_string().format(name = name, email = email))
