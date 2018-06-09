import yagmail
from draft import My_HTML_Mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def main():
    f=open("log.txt","w")
    emailid=sys.argv[3]
    username=sys.argv[2]
    role=sys.argv[4]
    password=sys.argv[5]
    name=sys.argv[1]
    ok=True
    try:
        yag=yagmail.SMTP("endogreen.dev@gmail.com","endogreen@dev")
        f.write("Authenticated\n")
    except:
        ok=False
        f.write("Connection Error\n")
    if ok:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Club Ayurveda Credentials"
        msg['From'] = "endogreen.dev@gmail.com"
        msg['To'] = emailid
        html=My_HTML_Mail(name,username,role,password)
        part1 = MIMEText(html, 'html')
        msg.attach(part1)
    yag.send(to=emailid,subject="Club Ayurveda Credentials",contents=html)
    f.write("Done\n")
    f.close()

main()
