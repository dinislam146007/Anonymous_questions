import telebot
from telebot import types
import re
import sqlite3

bot_token = ''
my_user_id = None
bot = telebot.TeleBot(bot_token)
@bot.message_handler(commands=['start'])
def start(message):
    global my_user_id
    user_id = message.text.split(' ')[1] if len(message.text.split(' ')) > 1 else None
    bot.send_message(message.chat.id, f('{user_id}')
    markup1 = types.InlineKeyboardMarkup()

    connection = sqlite3.connect('anonka.sql')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (my_id INTEGER, user_id INTEGER)''')
    cursor.execute("INSERT OR IGNORE INTO users (my_id) VALUES ('%s')" % (message.chat.id))
    #user_id = message.text.split(' ')[1] if len(message.text.split(' ')) > 1 else None
    #cursor.execute("UPDATE users SET user_id = %s WHERE my_id = %s" % (user_id, message.chat.id))
    if user_id is not None:
    # Используйте параметризованный запрос
        cursor.execute("UPDATE users SET user_id = ? WHERE my_id = ?", (user_id, message.chat.id))
    connection.commit()
    cursor.close()
    connection.close()
    my_user_id = message.from_user.id
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Написать человеку анонимно")
    btn3 = types.KeyboardButton('❓ Задать вопрос или предложить идею разработчику ❓')
    btn4 = types.KeyboardButton('Пользовательское соглашение')
    markup.row(btn1)
    markup.row(btn3)
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Привет! Как ты уже понял это бот для анонимных вопросов. \nТвоя ссылка:http://t.me/anonka_vopros_bot?start={message.chat.id}\n/help - инструкция.\n Немного формальности: запуская данного бота, ты автоматически соглашаешься с пользовательским соглашением, ознакомиться с которым можно по нажатию на одноименную кнопку. \nС уважением, разработчик💻', reply_markup=markup)
    #bot.send_message(message.chat.id, 'Спонсоры', reply_markup=markup1, )
    if user_id is not None:
        bot.send_message(message.chat.id, 'Теперь любое твоё сообщение будет отправлено этому человеку!')



@bot.message_handler(func=lambda message: '❓ Задать вопрос или предложить идею разработчику ❓' in message.text)
def idea(message):
    my_id = 
    markup = types.ForceReply(selective=False)  # Форсированный реплаи (позволяет отвечать на определенное сообщение)
    bot.send_message(message.chat.id, "Введи свой вопрос или идею, которую хоти отправить разработчику", reply_markup=markup)

    def my_question(message):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Ответить', callback_data=f'programmer:{message.text}:{message.chat.id}'))
        bot.send_message(my_id, f'Вопрос разрабу: \n{message.text}', reply_markup=markup)
        bot.send_message(message.chat.id, '✅ Твоё сообщение успешно отправлено разработчику!')

    bot.register_next_step_handler(message, my_question)
@bot.message_handler(func=lambda message: 'Пользовательское соглашение' in message.text)
def sogl(message):
    bot.send_message(message.chat.id, 'Пользовательское соглашение:\n Данный бот создан в юмористических целях. За сообщения от людей администратор не несёт никакой ответственности и не имеет доступа к авторам сообщений. При продолжении воздействия с ботом, ты автоматически принимаешь пользовательское соглашение. Если не хочешь его принимать, просто заблокируй данного бота и перестань с ним взаимодействовать!\n Анонимность: Этот бот предоставляет возможность отправлять анонимные вопросы другим пользователям. Ваши вопросы будут переданы получателям анонимно, и твоё имя не будет отображаться.\n Уважение: Пожалуйста, уважай других пользователей. Не отправляй оскорбительные, угрожающие, непристойные или незаконные сообщения через этот бот.\n Ответственность: Автор и администратор бота не несёт ответственности за содержание сообщений, отправленных пользователями. И не контролирует содержание вопросов и ответов.\n Согласие: Используя этот бот, ты соглашаешься с условиями этого пользовательского соглашения и обязуешься соблюдать правила.\n Конфиденциальность: Не делись личной информацией о себе или других пользователях в этом боте. Помни, что анонимность - это ключевая часть опыта использования этого бота.\n С использованием этого бота вы подтверждаете, что вы ознакомлены с настоящим пользовательским соглашением и согласны с его условиями.')
@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.chat.id, 'Инструкция для бота Анонимных Вопросов \nДобро пожаловать в бота Анонимных Вопросов! Этот бот предоставляет тебе возможность отправлять анонимные вопросы другим пользователям Telegram. Прежде чем начать, пожалуйста, прочти следующую инструкцию:\n ID - это уникальный код, который присваивается каждому пользователю или объекту в системе. В контексте бота, установка ID позволяет боту знать, кому отправлять сообщения или откуда получать информацию. По сути, это уникальный номер, который отличает одного пользователя от другого и помогает боту определить, к кому относится определенное сообщение или действие.\n P.S ID это не то, что начинается на @, это десять уникальных цифр. \n 1. Установка и начало:\n Начни беседу с ботом, отправив команду /start.\n Бот предоставит клавиатуру с опциями: "Написать человеку анонимно", "❓ Задать вопрос или предложить идею разработчику ❓".\n 2. Узнать свой ID:\n Нажмите на кнопку "Написать человеку анонимно". Бот отправит вам ваш уникальный ID в Telegram.\n 3. Установка ID получателя:\n Нажми на кнопку "✍️ Ввести id 🆔". Введи ID человека, которому ты хочешь отправить анонимный вопрос.\n 4. Задать вопрос разработчику:\n Нажмите на кнопку "❓ Задать вопрос или предложить идею разработчику ❓". Введи своё сообщению, которое хочешь отправить разработчику.\n 5. Отправка Анонимных Вопросов:\n Если ты уже установил ID получателя, просто отправь вопрос боту.\n Бот отправит твой вопрос получателю анонимно, и ответы будут отправлены тебе.\n 6. Ответ на Анонимный Вопрос:\n Если ты получишь анонимный вопрос, то сможешь ответить на него, нажав "Ответить ✍️".\n Ответ будет отправлен отправителю анонимно.\n С уважением, разработчик 💻')
@bot.message_handler(func=lambda message: 'Написать человеку анонимно' in message.text)
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row(types.KeyboardButton('✍️ Ввести id 🆔'))
    bot.send_message(message.chat.id, f'Твой id:{message.chat.id}. Если хочешь узнать id другого пользователя, перешли сюда его сообщение. Или введи id если знаешь. Нажав на кнопку ниже', reply_markup=markup)
@bot.message_handler(func=lambda message: '✍️ Ввести id 🆔' in message.text)
def input_id(message):
    markup = types.ForceReply(selective=False)  # Форсированный реплаи (позволяет отвечать на определенное сообщение)
    bot.send_message(message.chat.id, "Введите id или введите 'Отмена' для завершения ввода:", reply_markup=markup)

    def is_valid_number(text):
        # Проверяем, что текст состоит только из цифр и имеет длину 10 символов
        return bool(re.match(r'^\d{10}$', text))

    def handle_text_input(message):
        if message.text == str(message.chat.id):
            bot.send_message(message.chat.id, 'Введи id другого пользователя или введи "Отмена"', reply_markup=markup)
            bot.register_next_step_handler(message, handle_text_input)  # Ожидаем нового сообщения от пользователя
        elif is_valid_number(message.text) and message.text != str(my_user_id):
            bot.reply_to(message, '✅id успешно установлено✅. \nТеперь любое сообщение, отправленное мне, будет отправлено этому пользователю анонимно!')
            connection = sqlite3.connect('anonka.sql')
            cursor = connection.cursor()
            cursor.execute("UPDATE users SET user_id = %s WHERE my_id = %s" % (message.text, message.chat.id))
            connection.commit()
            cursor.close()
            connection.close()
        elif message.text == 'Отмена':
            pass
        else:
            bot.send_message(message.chat.id, '🔴 Введи корректный id', reply_markup=markup)
            bot.register_next_step_handler(message, handle_text_input)  # Ожидаем нового сообщения от пользователя
    bot.register_next_step_handler(message, handle_text_input)  # Ожидаем первого сообщения с ID от пользователя
@bot.message_handler(func=lambda message: message.forward_from is not None)
def handle_forwarded_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Установить id', callback_data=f'forward_id:{message.forward_from.id}:{message.chat.id}'))
    bot.send_message(message.chat.id, f'ID пересланного пользователя: {message.forward_from.id}', reply_markup=markup)
@bot.message_handler()
def send(message):
    markup = types.InlineKeyboardMarkup()
    def get_user_id_by_my_id():
        connection = sqlite3.connect('anonka.sql')
        cursor = connection.cursor()
        # Проверяем, существует ли запись с заданным my_id
        cursor.execute("SELECT user_id FROM users WHERE my_id=?", (message.chat.id,))
        result = cursor.fetchone()
        connection.close()
        return result[0] if result else None
      # Получаем user_id здесь
    user = get_user_id_by_my_id()
    markup.add(types.InlineKeyboardButton('Ответить ✍️', callback_data=f'otvet:{get_user_id_by_my_id()}:{message.text}:{message.chat.id}'))
    if user is None:
        bot.reply_to(message, 'Пожалуйста, введи id пользователя.')
    elif user == message.chat.id:
        bot.reply_to(message, 'Пожалуйста, введи id другого пользователя.')
    else:
        try:
            bot.send_message(int(user), f'🟢Новый анонимный вопрос: \n{message.text}', reply_markup=markup)
            bot.send_message(message.chat.id, '✅ Твоё сообщение успешно отправлено! ✅')
        except telebot.apihelper.ApiTelegramException as e:
            error_message = str(e)
            if "Forbidden: bot can't initiate conversation with a user" in error_message:
                # Если бот не может начать чат с пользователем, отправьте сообщение о том, что пользователь не зарегистрирован
                bot.send_message(message.chat.id, "❌ Я не могу отправить ваше сообщение, так как этот пользователь не запустил меня. \nПопросите его или её это сделать и всё получится!")
            else:
                # Обработка других ошибок
                bot.send_message(message.chat.id, "❌ Произошла ошибка при отправке сообщения ❌")
@bot.callback_query_handler(func=lambda call: call.data.startswith('otvet'))
def answer(call):
    # vopros = call.data.split(':')[2]
    # ser = call.data.split(':')[1]
    markup = types.ForceReply(selective=False)
    bot.send_message(call.data.split(':')[1], f'Введите ответ на вопрос:\n{call.data.split(":")[2]}', reply_markup=markup)
    def handle_text_input(message):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Ответить ✍️',
                                              callback_data=f'answer:{call.data.split(":")[3]}:{message.text}:{message.chat.id}'))

        bot.send_message(call.data.split(':')[3], f'❓ Вопрос:\n{call.data.split(":")[2]} \n💬 Ответ: \n{message.text}', reply_markup=markup1)
        bot.send_message(message.chat.id, '✅ Твоё сообщение успешно отправлено! ✅')
    bot.register_next_step_handler(call.message, handle_text_input)
@bot.callback_query_handler(func=lambda call: call.data.startswith('forward_id'))
def forward(call):
    user_id = call.data.split(':')[1]
    my = call.data.split(':')[2]
    bot.send_message(my, '✅ id успешно установлено!✅ \n Теперь любое сообщение которое вы отправите боту, будет отправлено этому человеку анонимно')
    connection = sqlite3.connect('anonka.sql')
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET user_id = %s WHERE my_id = %s" % (call.data.split(':')[1], call.data.split(':')[2]))
    connection.commit()
    cursor.close()
    connection.close()
@bot.callback_query_handler(func=lambda call: call.data.startswith('programmer'))
def answer(call):
    markup = types.ForceReply(selective=False)
    bot.send_message(1027971912, f'Введите ответ на вопрос:\n{call.data.split(":")[1]}', reply_markup=markup)
    def handle_text_input(message):
        bot.send_message(call.data.split(':')[2], f'❓ Вопрос разрабу:\n{call.data.split(":")[1]} \n💬 Ответ: \n{message.text}')
    bot.register_next_step_handler(call.message, handle_text_input)
@bot.callback_query_handler(func=lambda call: call.data.startswith('answer'))
def answer(call):
    # vopros = call.data.split(':')[2]
    # ser = call.data.split(':')[1]
    markup = types.ForceReply(selective=False)
    bot.send_message(call.data.split(':')[1], f'Введите ответ на вопрос:\n{call.data.split(":")[2]}', reply_markup=markup)
    def handle_text_input(message):
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Ответить ✍️',
                                              callback_data=f'otvet:{call.data.split(":")[3]}:{message.text}:{message.chat.id}'))
        bot.send_message(message.chat.id, '✅ Твоё сообщение успешно отправлено! ✅')
        bot.send_message(call.data.split(':')[3], f'❓ Вопрос:\n{call.data.split(":")[2]} \n💬 Ответ: \n{message.text}', reply_markup=markup1)
    bot.register_next_step_handler(call.message, handle_text_input)
bot.infinity_polling()
