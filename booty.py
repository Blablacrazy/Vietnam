import telebot
import constants
bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_murkup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_murkup.row('🍽Меню')
    user_murkup.row('🏎Доставка')
    user_murkup.row('⚠️Резерв столика')
    user_murkup.row('📱Контакты')
    user_murkup.row('📌Местоположение')
    bot.send_message(message.from_user.id, 'Привет я ВьетБот и добро пожаловать!', reply_markup=user_murkup)

@bot.message_handler(func=lambda message: message.text == '🍽Меню')
def handle_start(message):
    user_murkup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_murkup.row('🌯Нэмы и Бань Куон')
    user_murkup.row('🍗Птица, мясо и тофу')
    user_murkup.row('🍝Рис и лапша')
    user_murkup.row('🍵Супы')
    user_murkup.row('🥙Холодные закуски и салаты')
    user_murkup.row('🍱Расширяем границы Азии')
    user_murkup.row('🍤Рыба и морепродукты')
    user_murkup.row('🍔Бао бургеры')
    user_murkup.row('🍭Детское меню')
    user_murkup.row('🍰Десерты')
    user_murkup.row('🍚Гарниры')
    user_murkup.row('🍹Бар')
    user_murkup.row('🔚В начало')
    bot.send_message(message.from_user.id, 'Выбирай категорию меню', reply_markup=user_murkup)

@bot.message_handler(func=lambda message: message.text == '🏎Доставка')
def handle_start(message):
    user_murkup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_murkup.row('1️⃣Алматы')
    user_murkup.row('2️⃣Астана')
    user_murkup.row('🔚В начало')
    bot.send_message(message.from_user.id, 'Выбирай город', reply_markup=user_murkup)


@bot.message_handler(func=lambda message: message.text == '⚠️Резерв столика')
def handle_start(message):
    user_murkup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_murkup.row('✅Курящий')
    user_murkup.row('🚭Некурящий')
    user_murkup.row('🔚В начало')
    bot.send_message(message.from_user.id, 'У нас есть несколько залов!', reply_markup=user_murkup)


@bot.message_handler(func=lambda message: message.text == '🔚В начало')
def handle_start(message):
    user_murkup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_murkup.row('🍽Меню')
    user_murkup.row('🏎Доставка')
    user_murkup.row('⚠️Резерв столика')
    user_murkup.row('📱Контакты')
    user_murkup.row('📌Местоположение')
    bot.send_message(message.from_user.id, 'Давайте попрбуем еще раз!', reply_markup=user_murkup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = 'ты не умеешь играть в эту игру'
    if message.text == '📌Местоположение':
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, 43.20241207, 76.89248893)
    elif message.text == 'a':
        bot.send_message(message.chat.id, 'b')
    else:
        bot.send_message(message.chat.id, answer)


#@bot.message_handler(content_types=['text'])
#def handle_text(message):
#    if message.text == '📱Контакты':






print(bot.get_me())
def log(message, answer):
    print()
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0) {1). (id = {2]) /n Текст - {3]".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)









bot.polling(none_stop=True)