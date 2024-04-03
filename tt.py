import telebot
import webbrowser
import sqlite3

bot = telebot.TeleBot('7153347445:AAGN-Cfum5EdNU79UTsR0z0e-mY3AZ88tJg')
name = None
@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('tg.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users(id int auto_increment print key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'привет, тебя сейчас зарегистируем! Ведите ваше имя')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id,  'Ведите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('tg.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользвателей', callback_data='user'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)



@bot.message_handler(commands=['instagram'])
def instagram(message):
    webbrowser.open('https://www.instagram.com/ota_bekkkkkkkk/')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'привет, {message.from_user.first_name} {message.from_user.first_name}')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'привет, {message.from_user.first_name} {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id}')


bot.polling(none_stop=True)
