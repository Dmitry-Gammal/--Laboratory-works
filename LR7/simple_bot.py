import telebot
from telebot import types
import random

TOKEN = "Мойтокен"
bot = telebot.TeleBot(TOKEN)

user_states = {}



@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_states[user_id] = "menu"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎮 Играть", "👤 Профиль")

    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! Выбери:",
        reply_markup=markup
    )


def show_menu(chat_id, user_id):
    user_states[user_id] = "menu"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎮 Играть", "👤 Профиль")

    bot.send_message(
        chat_id,
        "Главное меню:",
        reply_markup=markup
    )


user_numbers = {}


def show_game(chat_id, user_id):
    user_states[user_id] = "game"

    user_numbers[user_id] = random.randint(1, 10)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    markup.add("⬅️ Назад")

    bot.send_message(
        chat_id,
        "🎮 Угадай число от 1 до 10:",
        reply_markup=markup
    )


def show_profile(chat_id, user_id, username):
    user_states[user_id] = "profile"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("✏️ Изменить имя", "📊 Статистика", "⬅️ Назад")

    bot.send_message(
        chat_id,
        f"👤 Твой профиль:\nИмя: {username}\nID: {user_id}",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_id = message.from_user.id

    if user_id not in user_states:
        user_states[user_id] = "menu"

    state = user_states[user_id]

    if message.text == "⬅️ Назад":
        show_menu(message.chat.id, user_id)
        return

    if state == "menu":
        if message.text == "🎮 Играть":
            show_game(message.chat.id, user_id)
        elif message.text == "👤 Профиль":
            show_profile(message.chat.id, user_id, message.from_user.first_name)
        else:
            bot.send_message(message.chat.id, "Используй кнопки 👆")

    elif state == "game":
        if message.text.isdigit():
            guess = int(message.text)
            secret = user_numbers.get(user_id)

            if secret is None:
                secret = random.randint(1, 10)
                user_numbers[user_id] = secret

            if guess == secret:
                bot.send_message(
                    message.chat.id,
                    f"✅ Правильно! Число было {secret}",
                    reply_markup=types.ReplyKeyboardRemove()
                )
                show_menu(message.chat.id, user_id)
            elif 1 <= guess <= 10:
                if guess < secret:
                    hint = "больше"
                else:
                    hint = "меньше"

                bot.send_message(
                    message.chat.id,
                    f"❌ Не угадал. Попробуй число {hint} чем {guess}!"
                )
            else:
                bot.send_message(message.chat.id, "Число должно быть от 1 до 10!")
        else:
            bot.send_message(message.chat.id, "Введи число от 1 до 10")

    elif state == "profile":
        if message.text == "✏️ Изменить имя":
            bot.send_message(
                message.chat.id,
                "Отправь новое имя:"
            )
            user_states[user_id] = "changing_name"

        elif message.text == "📊 Статистика":
            bot.send_message(
                message.chat.id,
                "📊 Твоя статистика:\nИгр сыграно: 0\nПобед: 0"
            )

        else:
            show_profile(message.chat.id, user_id, message.from_user.first_name)

    elif state == "changing_name":
        bot.send_message(
            message.chat.id,
            f"✅ Имя изменено на: {message.text}"
        )
        show_profile(message.chat.id, user_id, message.text)


@bot.message_handler(commands=['state'])
def show_state(message):
    user_id = message.from_user.id
    state = user_states.get(user_id, "неизвестно")

    states_dict = {
        "menu": "🏠 Главное меню",
        "game": "🎮 Игра",
        "profile": "👤 Профиль",
        "changing_name": "✏️ Изменение имени"
    }

    bot.send_message(
        message.chat.id,
        f"Текущее состояние: {states_dict.get(state, state)}"
    )


@bot.message_handler(commands=['number'])
def show_number(message):
    user_id = message.from_user.id

    if user_id in user_numbers:
        secret = user_numbers[user_id]
        bot.send_message(
            message.chat.id,
            f"🔍 Загаданное число: {secret}"
        )
    else:
        bot.send_message(message.chat.id, "Сначала начни игру!")


@bot.message_handler(commands=['newgame'])
def new_game(message):
    show_game(message.chat.id, message.from_user.id)


if __name__ == "__main__":
    print("🤖 Бот запущен с 3 состояниями:")
    print("1. 🏠 Меню")
    print("2. 🎮 Игра")
    print("3. 👤 Профиль")
    print("\nДля отладки используй команды:")
    print("/number - показать загаданное число")
    print("/state - показать текущее состояние")
    print("/newgame - начать новую игру")
    bot.polling(none_stop=True)