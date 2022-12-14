import telebot
from telebot import types

bot = telebot.TeleBot('5491744010:AAHmVVE0oi_u3T1Sxvm5SSMQpW5NWqWaFSE')


@bot.message_handler(commands=['start'])
def start(message):
    app_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    app_keyboard1 = types.KeyboardButton(text="Оформить заявку")
    app_markup.add(app_keyboard1)
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_message(chat_id, f"Привет {first_name} !\n"
                     f"Здесь Вы можете оставить заявку и администратор свяжеться с вами!", reply_markup = app_markup)



@bot.message_handler(content_types=["text"])
def text(message):
    admin_id = 1103116594
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == "Оформить заявку":
            bot.send_message(chat_id, "Укажите адрес, телефон и наименование товара в любой удобной для Вас форме!")
            bot.register_next_step_handler(message, send_z)


def send_z(message):
    first_name = message.chat.first_name
    chat_id = message.chat.id
    user_name = message.chat.username
    z = message.text
    admin_id = 1103116594
    app_text = []
    app_name = []
    app_username = []
    app_name.append(first_name)
    app_username.append(user_name)
    app_text.append(z)
    bot.send_message(admin_id, f"Поступила заявка от {app_name[0]} !\n"
                               f"Пользователь = @{app_username[0]}\n"
                               f"Вот его данные:\n"
                               f"{app_text[0]} \n")


    app_name.clear()
    app_text.clear()
    app_username.clear()
    bot.send_message(chat_id, "Заявка отправлена!")




bot.polling(none_stop=True)
