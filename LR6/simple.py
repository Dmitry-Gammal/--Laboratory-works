import telebot
from telebot import types
import random

TOKEN = "Мойтокен"
bot = telebot.TeleBot(TOKEN)


def create_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("🎲 Число")
    btn2 = types.KeyboardButton("ℹ️ Инфо")
    btn3 = types.KeyboardButton("👋 Привет")

    markup.add(btn1, btn2, btn3)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я простой бот.\nВыбери действие:",
        reply_markup=create_keyboard()
    )


@bot.message_handler(content_types=['text'])
def handle_buttons(message):
    if message.text == "🎲 Число":
        num = random.randint(1, 10)
        bot.send_message(message.chat.id, f"Твоё число: {num}")

    elif message.text == "ℹ️ Инфо":
        bot.send_message(message.chat.id, "Я тестовый бот с 3 кнопками.")

    elif message.text == "👋 Привет":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!")


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
