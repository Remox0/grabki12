

<img src="https://cdn.discordapp.com/attachments/843729542413025300/1225599032903204896/garden-1300347_1280.png?ex=6621b70b&is=660f420b&hm=9ef78e7867e2d57d8875a64fe944f4545d48a7b9e5f3ef856c7aaa17f382edad&" alt="Opis obrazu" width="800">
<br>

# Grabki v1.2 🇵🇱

**Grabki** to prosty program napisany w języku Python, który zbiera podstawowe informacje o użytkowniku i komputerze. Jest to narzędzie, które umożliwia szybkie uzyskanie istotnych danych dotyczących systemu i użytkownika bez konieczności ręcznego przeszukiwania wielu miejsc w systemie operacyjnym. Po pobraniu edytuj potrzebne dane w kodzie aby program poprawnie działał. W nie dalekiej przyszłości będę aktualizował program z większą ilością funkcji i możliwości ;)

```
git clone https://github.com/Remox0/grabki12.git
```

## Funkcje 🪛:
- Pobiera informacje o nazwie użytkownika i systemie operacyjnym.
- Wyświetla datę i czas uruchomienia i zebrania danych..

## Sposób użycia ⚙️:
1. Uruchom program "Grabki".
2. Program automatycznie zbierze potrzebne informacje o użytkowniku i komputerze.
3. Program wyśle te dane na wpisanego maila.

## Wymagania ✅:
- Python 3.x

## Biblioteki 📕:

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


## Pierwsze uruchomienie 🚀:
```
git clone https://github.com/Remox0/grabki12.git
```
```
cd grabki12
```
```
python main.py
```

## Porady 👍:
-Najlepiej jak skompilujesz program do .exe jeżeli chcesz korzystac z programu bez pythona.

-Zanim skompilujesz do .exe wpisz w odpowiednie pola odpowidnie informacje takie jak mail odbiorcy, adresat,hasło.

-Jak skompilowac do exe? To bradzo proste! Poniżej znajdziesz poradnik:
1. Uruchom terminal shell (windows)
2. Pobierz pyinstaller (jeśli nie masz)
```
pip install pyinstaller
```
3. Przejdź do katalogu grabki12
```
cd ~\grabki12
```
4.Wpisz polecene pyinstaller
```
pyinstaller main.py
```
5. Powinneś uzyskać 2 nowe foldery i jedn plik
6. Skopiuj w inne miejsce folder build a później mozesz usunąć reszcze plików.
UPEWNIJ SIĘ ŻE WCZEŚNIEJ UZUPEŁNIŁĘŚ BRAKUJĄCE MIEJSCA W PLIK main.py!!!

Teraz powinneś mieć w folderze build main i tam jest plik .exe
Jeżeli go uruchomisz wszystko zadziała tak jak trzeba :)
Tylko pamiętaj o tym że nie możesz odzielić pliku .exe od folderu _internal!!! Inaczej nie zadziała. 

## W celach edukacyjnych TYLKO 🤓
Nie używaj na drugiej osobie bez jej pozwolenia!

## Coś o mnie 📝:
-Jestem nowym twórcą na GitHubie 
-**Grabki** to mój pierwszy poważny jaki kolwiek program który zbiera infopramcje o użytkowniku
-W razie jakich kolwiek niedopatrzeń z mojej strony w kodzie lub o jakieś propozycję prosze pisać
