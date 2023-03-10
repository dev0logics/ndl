import telebot
import socket
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', category=InsecureRequestWarning)


# Crea un oggetto bot Telegram
bot = telebot.TeleBot("6125221226:AAEh_ADmdNPTLglNDGeBI-SB3fqfA1nskRQ")

# Questa funzione viene chiamata ogni volta che il bot riceve un messaggio di testo
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_message(message):
    # Avvia una connessione TCP con il server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 2025))

    # Invia e riceve messaggi tramite la connessione TCP
    message1 = client.recv(1024).decode()
    client.send(message.text.encode())
    message2 = client.recv(1024).decode()
    client.send(message.text.encode())
    message3 = client.recv(1024).decode()

    # Invia la risposta ricevuta dal server come messaggio al bot Telegram
    bot.reply_to(message, message3)

# Avvia il bot Telegram
bot.polling()