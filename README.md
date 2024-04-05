

<img src="https://cdn.discordapp.com/attachments/843729542413025300/1225599032903204896/garden-1300347_1280.png?ex=6621b70b&is=660f420b&hm=9ef78e7867e2d57d8875a64fe944f4545d48a7b9e5f3ef856c7aaa17f382edad&" alt="Opis obrazu" width="800">
<br>

# Grabki v1.2

**Grabki** to prosty program napisany w języku Python, który zbiera podstawowe informacje o użytkowniku i komputerze. Jest to narzędzie, które umożliwia szybkie uzyskanie istotnych danych dotyczących systemu i użytkownika bez konieczności ręcznego przeszukiwania wielu miejsc w systemie operacyjnym.

## Funkcje:
- Pobiera informacje o nazwie użytkownika i systemie operacyjnym.
- Wyświetla datę i czas uruchomienia i zebrania danych..

## Sposób użycia:
1. Uruchom program "Grabki".
2. Program automatycznie zbierze potrzebne informacje o użytkowniku i komputerze.
3.Program wyśle te dane na wpisanego maila.

## Wymagania:
- Python 3.x

## Wymagane biblioteki:

- smtplib
- datetime
- platform
- email.mime.multipart (MIMEMultipart)
- email.mime.text (MIMEText)
- email.mime.base (MIMEBase)
- email.encoders (encoders)
- socket
- os
- getpass


## Instalacja bibliotek i pierwsze uruchomienie:
```bash
pip install -r requirements.txt
```
```
python main.py
```

