import telebot
from classes import Controller, Connection
from mysql.connector import connect, Error

conn = Connection()
bot = telebot.TeleBot(conn.TELEGRAM_TOKEN)

# handle '/done'
@bot.message_handler(commands=['done'])
def mark_as_done(message):
    controller = Controller(1)
    controller.set_completed(1)
    bot.send_message(message.chat.id, "🏆 *Great\! You've completed your todays exercises\.*", parse_mode="MarkdownV2")

@bot.message_handler(commands=["test"])
def test(message):
    db_conn = None

    try:
        connection = connect(
                    host = conn.DB_HOST,
                    user = conn.DB_USER,
                    password = conn.DB_PASS,
                    database="wbot"
                )
        db_conn = True
    except Error:
        db_conn = False
    
    text = ""

    if db_conn:
        text = "Bot: Up and running ✅\nDB:  Connected ✅"
    else:
        text = "Bot: Up and running ✅\nDB:  Not Connected ❌"

    bot.send_message(message.chat.id, text)

try:
    bot.polling()
except:
    bot.send_message(conn.TELEGRAM_CHAT_ID, "Error: WBOT command_handler.py")