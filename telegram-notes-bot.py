import telebot

bot = telebot.TeleBot("TOKEN")

notes = {}

@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, "Привет! Пиши заметку, я сохраню.")

@bot.message_handler(content_types=["text"])
def save(m):
    notes[m.chat.id] = notes.get(m.chat.id, []) + [m.text]
    bot.send_message(m.chat.id, "Записал!")

bot.polling(none_stop=True)
