import telebot
import schedule
import requests
import wikipedia
import datetime
import configparser
import time
import openai
import random
import telebot
import sqlite3
import codecs
import os # для определения директории проекта
import re
from threading import Thread
from telebot import types
from datetime import datetime
from bs4 import BeautifulSoup as BS;

# Чтение конфигурационного файла
config = configparser.ConfigParser()
config.read("settings.ini", encoding="utf-8")

# Получение ключей для бота и OpenAI
bot_api = config['Telegram']['bot_api']
openai_api = config['OpenAI']['ai_api']

# Инициализация бота и OpenAI
bot = telebot.TeleBot(bot_api)
openai.api_key = openai_api

# Получение ID чата
id_chat_config = config['Telegram']['id_chat']

# Список дней недели
weekdays = ["Понеделник", "Вторник", "Среда", "Четверг", "Пятница", "Субота", "Воскресенье"]

# Получение текущего дня
now = datetime.now()
current_day = weekdays[now.weekday()]

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Здесь указываем путь к файлу базы данных
#engine = create_engine('postgresql://username:password@host:port/main.bd')

# Создаем сессию
#Session = sessionmaker(bind=engine)
#session = Session()

# Извлекаем информацию из таблицы 'whitelist' и колонки 'allowed_ids'
#allowed_ids = session.query("allowed_ids").from_statement("SELECT allowed_ids FROM whitelist").all()

#print(allowed_ids)

# Подключение к базе данных
conn = sqlite3.connect('main.db')
cursor = conn.cursor()

# Извлечение ID из таблицы 'whitelist'
cursor.execute("SELECT allowed_ids FROM whitelist")
allowed_ids = [row[0] for row in cursor.fetchall()]

# Закрытие подключения
cursor.close()
conn.close()

def add_to_file(file_name, date, name):
    with open(file_name, 'a') as file:
        file.write(f"{date}|{name}\n")

def remove_from_file(file_name, date, name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    with open(file_name, 'w') as file:
        for line in lines:
            if line.strip() != f"{date}|{name}":
                file.write(line)

allowed_users = [5071555320, 347081774, 432153909, 476049995, 610687824, 610687824, 292769304, 917813838, 1012375116, 476055977, 638214956, 451593243, 395466608, 527478181, 597625068, 474589496, 2041843983, 5783129042, 1782900598, 374400865, 420010587, 2035255973, 635408613, 505524954, 799997126, 5449431424, 660477751, 647631865, 691817178, 798326616, 788984733, 428478715, 394030943, 5707489544, 566760716, 1129618092, 543346384, 581571765, 5582410569, 521041989, 573612999, 711705684, 1630006436, 744768160, 1375470191, 824940739, 749146762, 990663557, 1911916295, 397955776, 867978891, 569712179, 829708722, 815897771, 541546135, 356081461, 813345609, 5512205977, 851478921, 1427342741] # add the user IDs here
@bot.message_handler(commands=['меню','menu'])
def handle_menu(message):
    if message.from_user.id not in allowed_users:
        bot.send_message(message.chat.id, "Извините, вам доступ запрещен.")
        return
    keyboard = types.InlineKeyboardMarkup()

    #reklama_button = types.InlineKeyboardButton(text='Тест', callback_data='add')
    add_button = types.InlineKeyboardButton(text='Добавить день рождения', callback_data='add')
    remove_button = types.InlineKeyboardButton(text='Удалить день рождения', callback_data='remove')
    list_button = types.InlineKeyboardButton(text='Показать всех именинников', callback_data='list')
    add_homework_button = types.InlineKeyboardButton(text='Записать домашнее задание', callback_data='add_homework')
    view_homework_button = types.InlineKeyboardButton(text='Показать домашнее задание', callback_data='view_homework')
    remove_homework_button = types.InlineKeyboardButton(text='Удалить домашнее задание', callback_data='remove_homework')

    #keyboard.add(reklama_button)
    keyboard.add(add_button)
    keyboard.add(remove_button)
    keyboard.add(list_button)

    keyboard.add(add_homework_button)
    keyboard.add(view_homework_button)
    keyboard.add(remove_homework_button)

    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data == 'add_homework')
    def handle_add_homework(call):
        if call.from_user.id not in allowed_users:
            bot.answer_callback_query(callback_query_id=call.id, text="Извините, вам доступ запрещен.")
            return

        bot.send_message(call.message.chat.id, 'Введите домашнее задание:')
        bot.register_next_step_handler(call.message, process_homework_step)

    def process_homework_step(message):
        with open('dz.txt', 'a') as file:
            file.write(f"{message.text}\n")
        send_msg(f"Новое домашнее задание добавил(а): {message.from_user.first_name} /dz - для просмотра\n")
        #send_msg(f"Добавлено новое домашнее задание! /dz для просмотра\n")
        #bot.send_message(message.chat.id, 'Домашнее задание успешно добавлено!')
        #send_msg(f"[INFO] 🎂 Сегодня День Рождения:\n{birthdays[today]}")
    @bot.callback_query_handler(func=lambda call: call.data == 'view_homework')
    def handle_show_homework(call):
        if call.from_user.id not in allowed_users:
            bot.answer_callback_query(callback_query_id=call.id, text="Извините, вам доступ запрещен.")
            return
            bot.send_message(message.chat.id, "Извините, вам доступ запрещен.")
            return
        with open('dz.txt', 'r') as file:
            homework = file.read()
            numbers = "\n".join([f"{i + 1}. {line}" for i, line in enumerate(homework.splitlines())])
        #bot.send_message(call.message.chat.id, f"Домашняя работа:\n\n{homework}")
        bot.send_message(call.message.chat.id, f"Домашняя работа:\n\n{numbers}")

    @bot.callback_query_handler(func=lambda call: call.data == 'remove_homework')
    def handle_remove_homework(call):
        if call.from_user.id not in allowed_users:
            bot.answer_callback_query(callback_query_id=call.id, text="Извините, вам доступ запрещен.")
            return
        with open('dz.txt', 'r') as file:
            homework = file.read()
            numbers = "\n".join([f"{i + 1}. {line}" for i, line in enumerate(homework.splitlines())])
        bot.send_message(call.message.chat.id, f"Домашняя работа:\n\n{numbers}")
        bot.send_message(call.message.chat.id, 'Необходимый пункт для удаления:')
        bot.register_next_step_handler(call.message, process_remove_homework_step)

    def process_remove_homework_step(message):
        try:
            line_number = int(message.text) - 1
            with open("dz.txt", "r") as file:
                lines = file.readlines()
            with open("dz.txt", "w") as file:
                for i, line in enumerate(lines):
                    if i != line_number:
                        file.write(line)
            send_msg(f"Домашняя работа удалена Пользвателем {message.from_user.first_name}\n/dz для просмотра\n")
        except:
            bot.send_message(message.chat.id, 'Вы ввели букву(ы) вместо цифры с необходимым для удаления заданием. Заходите заново в меню и пробуйте /menu')

@bot.callback_query_handler(func=lambda call: call.data == 'add')
def handle_add_birthday(call):
    if call.from_user.id not in allowed_users:
        bot.answer_callback_query(callback_query_id=call.id, text="Извините, вам доступ запрещен.")
        return
    bot.send_message(call.message.chat.id, 'Введите имя и дату рождения через пробел (например: Иван 28.01)')
    bot.register_next_step_handler(call.message, process_birthday_step)
def process_birthday_step(message):
    try:
        name, date = message.text.strip().split(' ')
        with open('birthdays.txt', 'a') as file:
            file.write(f"{name}|{date}\n")
        send_msg(f"День рождения {name} {date} добавил(а) в список: {message.from_user.first_name}")
        #bot.send_message(message.chat.id, f"День рождения {name} {date} добавлен в список")
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат, попробуйте еще раз (например: Иван 28.01)')


@bot.callback_query_handler(func=lambda call: call.data == 'remove')
def handle_remove_birthday(call):
    if call.from_user.id not in allowed_users:
        bot.answer_callback_query(callback_query_id=call.id, text="Извините, вам доступ запрещен.")
        return
    with open('birthdays.txt', 'r') as file:
        homework = file.read()
        numbers = "\n".join([f"{i + 1}. {line}" for i, line in enumerate(homework.splitlines())])
    bot.send_message(call.message.chat.id, f"День рождения:\n\n{numbers}")
    bot.send_message(call.message.chat.id, 'Необходимый пункт для удаления:')
    bot.register_next_step_handler(call.message, remove_birthday)
def remove_birthday(message):
    try:
        line_number = int(message.text) - 1
        with open("birthdays.txt", "r") as file:
            lines = file.readlines()
        with open("birthdays.txt", "w") as file:
            for i, line in enumerate(lines):
                if i != line_number:
                    file.write(line)
        name, date = lines[line_number].strip().split("|")
        date = datetime.strptime(date, '%d.%m').date()
        send_msg(f"День рождения {name} {date.strftime('%d.%m')} удалил(а): {message.from_user.first_name}")
    except:
        send_msg("Ошибка! Пожалуйста, выберите правильный пункт из меню. Заходите заново в меню и пробуйте /menu")
@bot.callback_query_handler(func=lambda call: call.data == 'list')
def handle_show_list(call):
    if call.from_user.id not in allowed_users:
        bot.answer_callback_query(callback_query_id=call.id, text="Извините, вам доступ запрещен.")
        return
    with open('birthdays.txt', 'r') as file:
        birthdays = file.readlines()
    birthdays = ['{}. {}'.format(i + 1, b.replace('|', ' ')) for i, b in enumerate(birthdays)]
    bot.send_message(call.message.chat.id, ''.join(birthdays))



# bot.send_message(call.message.chat.id, f"Домашняя работа:\n\n{homework}")
#bot.send_message(call.message.chat.id, f"Домашняя работа:\n\n{numbers}")

@bot.message_handler(commands=['dz', 'domashka', 'дз','домашка','lp','ljvfirf'])
def handle_show_birthdays(message):
    with open('dz.txt', 'r') as file:
        birthdays = file.readlines()
        if birthdays:
            response = ''.join(birthdays)
            with open('dz.txt', 'r') as file:
                homework = file.read()
                numbers = "\n".join([f"{i + 1}. {line}" for i, line in enumerate(homework.splitlines())])
            # bot.send_message(call.message.chat.id, f"Домашняя работа:\n\n{homework}")
            bot.reply_to(message, f"Хочешь дополнить? /menu \n\nДомашняя работа:\n\n{numbers}")
            #bot.reply_to(message, f'Хочешь дополнить? /menu \n\nДомашка:\n\n{response}')
        else:
            bot.reply_to(message, 'Домашки нет.\n\nХочешь добавить? /menu')
def send_msg(message): # ДР + Пары + schedule
    ids = [int(x) for x in config['Telegram']['id_chat'].split(',')]
    for id in ids:
        bot.send_message(id, message)

def send_sticker(message): # Sticker happy
    ids = [int(x) for x in config['Telegram']['id_chat'].split(',')]
    for id in ids:
        bot.send_sticker(id, message)
@bot.message_handler(content_types=['text'])
def lalala(message):
    print(f'Имя: {message.from_user.first_name}Логин: {message.from_user.username} UserID: {message.from_user.id} Написал: {message.text} ChatID: {message.chat.id}')
    id_chat_config
    for id in id_chat_config:
        if message.from_user.id in allowed_ids:
            if "Toma" in message.text or "toma" in message.text or "Тома" in message.text or "тома" in message.text:
                bot.send_chat_action(message.chat.id, 'typing')
                message.text = re.sub(r'(Toma|toma|Тома|тома)', '', message.text)
                response = openai.Completion.create(model="text-davinci-003", prompt=message.text, max_tokens=1000)
                full_response = response['choices'][0]['text']  # Use the text property of the first element of the choices list to access the full response
                lines = full_response.splitlines()  # Split the response into individual lines
                for line in lines:  # Iterate over the lines
                    try:
                        bot.send_message(message.chat.id, line)  # Send each line back to the user as a separate message
                    except Exception as e:
                        print(e)

            banned_words = []
            with open('badwords.ini', 'r') as f:
                banned_words = f.readlines()
            banned_words = [word.strip().lower() for word in banned_words]

            words = message.text.split()
            for word in words:
                if word.lower() in banned_words:
                    responses = ['Не материтесь (>_<)', 'Пожалуйста, не используйте такие слова',
                                 'Пожалуйста, будьте вежливы',
                                 'Пожалуйста, обращайтесь к другим с уважением',
                                 'Не используйте оскорбительную лексику',
                                 'Пожалуйста, будьте уважительны к другим участникам. Мат никому не интересен']

                    response = random.choice(responses)
                    bot.send_message(message.chat.id, response)

        elif message.text.lower() in ('я тебя люблю', 'ты моя любовь', 'это секс', 'секс', 'это любовь'):
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBm9pjxoJdN99yNA3oUGIpjP7EH3S2TgACTgIAAladvQow_mttgTIDby0E')

        if any(x in message.text for x in # намнного лучше работает, чем if message.text.lower()
               ("Она отмечала?", "Уже отмечала?", "Она отмечает?", "А она уже отметила?", "отмечала?", "Уже отмечала?", "отмечает?")):
            responses = ['Советую поторопиться', 'Кто его знает', 'Пока что не знаю', 'Лучше ускориться', '50/50', 'Я сказала, что ты задержишься', 'Ага ага']
            response = random.choice(responses)
            bot.send_message(message.chat.id, response)

        if "погода" in message.text or "прогноз" in message.text or "Погода" in message.text or "Прогноз" in message.text:
            message.text = re.sub(r'(погода|прогноз|Погода|Прогноз)', '', message.text)
            url = 'https://sinoptik.ua/погода-{}'.format(str.lower(message.text))
            print(url)
            r = requests.get(url)
            html = BS(r.content, 'html.parser')
            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                text = el.select('.wDescription .description')[0].text
                day2 = el.select("#bd2 .date")[0].text
                month2 = el.select("#bd2 .month")[0].text
                wday2 = el.select("#bd2 .day-link")[0].text
                t_min2 = el.select(".temperature .min")[1].text
                t_max2 = el.select(".temperature .max")[1].text
                day3 = el.select("#bd3 .date")[0].text
                month3 = el.select("#bd3 .month")[0].text
                wday3 = el.select("#bd3 .day-link")[0].text
                t_min3 = el.select(".temperature .min")[2].text
                t_max3 = el.select(".temperature .max")[2].text
                day4 = el.select("#bd4 .date")[0].text
                month4 = el.select("#bd4 .month")[0].text
                wday4 = el.select("#bd4 .day-link")[0].text
                t_min4 = el.select(".temperature .min")[3].text
                t_max4 = el.select(".temperature .max")[3].text
                day5 = el.select("#bd5 .date")[0].text
                month5 = el.select("#bd5 .month")[0].text
                wday5 = el.select("#bd5 .day-link")[0].text
                t_min5 = el.select(".temperature .min")[4].text
                t_max5 = el.select(".temperature .max")[4].text
                vologist = html.find_all('td', 'cur')[5].text
                now_temp = html.select_one('.imgBlock .today-temp').text.strip()
                current_date = str(datetime.now().date())
                bot.send_message(message.chat.id,f"Сейчас: {now_temp}, {current_day} \nВлажность: {vologist}% \nТемпература: " + t_min + ', ' + t_max + "\n---------------------------------------------------\n" + text + "\n\n🌥 " + day2 + " " + month2 + " | " + wday2 + "\n" + "💨Температура: " + t_min2 + " " + t_max2 + "\n" + "\n" + "🌥 " + day3 + " " + month3 + " | " + wday3 + "\n" + "💨Температура: " + t_min3 + " " + t_max3 + "\n" + "\n" + "🌥 " + day4 + " " + month4 + " | " + wday4 + "\n" + "💨Температура: " + t_min4 + " " + t_max4 + "\n" + "\n" + "🌥 " + day5 + " " + month5 + " | " + wday5 + "\n" + "💨Температура: " + t_min5 + " " + t_max5)

        if message.text.lower() in ('преподы', 'список преподавателей', 'викладачі'):
            bot.send_message(message.chat.id, codecs.open('prepods.txt', "r", "utf_8_sig").read())
        if message.text.lower() in ('группа', 'список учеников', 'список'):
            bot.send_message(message.chat.id, codecs.open('students.txt', "r", "utf_8_sig").read())
        if message.text.lower() in ('орков', 'статистика', 'мертвых орков', 'сколько мертвых орков?'):
            r = requests.get('https://www.pravda.com.ua/rus/')
            soup = BS(r.content, 'html.parser')
            orks = soup.select('.war_num')[0].text
            airplane = soup.select('.war_num')[1].text
            hellicop = soup.select('.war_num')[2].text
            tanks = soup.select('.war_num')[3].text
            BBM = soup.select('.war_num')[4].text
            ARTA = soup.select('.war_num')[5].text
            PVO = soup.select('.war_num')[6].text
            RSZO = soup.select('.war_num')[7].text
            KAMAZ = soup.select('.war_num')[8].text
            KORABL = soup.select('.war_num')[9].text
            SHAHID = soup.select('.war_num')[10].text
            WARDAY = soup.select('.war_title')[0].text
            now = datetime.now()
            daymonth = now.strftime("%d.%m")
            stats = {
                'Орков💀':   orks,
                'Танков':     tanks,
                'Самолетов':  airplane,
                'Вертолетов': hellicop,
                'Бронемашин': BBM,
                'Артиллерия': ARTA,
                'ПВО':        PVO,
                'РСЗО':       RSZO,
                'КАМАЗЫ':     KAMAZ,
                'Катеры':     KORABL,
                'БПЛА':       SHAHID,
            }
            #message_text = f"Потери захватчиков на утро {daymonth}\n{WARDAY}\n"
            message_text = f"{WARDAY}\n\n"
            for key, value in stats.items():
                message_text += f"{key}: {value.replace('+', ' | 🔥 +').replace('~', ' ')}\n"
            bot.send_message(message.chat.id, message_text)

        return
def dead_orks_bot():
    r = requests.get('https://www.pravda.com.ua/rus/')
    soup = BS(r.content, 'html.parser')
    orks = soup.select('.war_num')[0].text
    airplane = soup.select('.war_num')[1].text
    hellicop = soup.select('.war_num')[2].text
    tanks = soup.select('.war_num')[3].text
    BBM = soup.select('.war_num')[4].text
    ARTA = soup.select('.war_num')[5].text
    PVO = soup.select('.war_num')[6].text
    RSZO = soup.select('.war_num')[7].text
    KAMAZ = soup.select('.war_num')[8].text
    KORABL = soup.select('.war_num')[9].text
    SHAHID = soup.select('.war_num')[10].text
    WARDAY = soup.select('.war_title')[0].text
    now = datetime.now()
    daymonth = now.strftime("%d.%m")
    stats = {
        'Орков💀': orks,
        'Танков': tanks,
        'Самолетов': airplane,
        'Вертолетов': hellicop,
        'Бронемашин': BBM,
        'Артиллерия': ARTA,
        'ПВО': PVO,
        'РСЗО': RSZO,
        'КАМАЗЫ': KAMAZ,
        'Катеры': KORABL,
        'БПЛА': SHAHID,
    }
    message_text = f"{WARDAY}\n\n"
    for key, value in stats.items():
        message_text += f"{key}: {value.replace('+', ' | 🔥 +').replace('~', ' ')}\n"
    send_msg(message_text)
def happybirthday_bot():
    birthdays = {}
    with open("birthdays.txt", "r") as f:
        for line in f:
            name, date = line.strip().split("|")
            formatted_date = '{:02d}.{:02d}'.format(int(date.split(".")[0]), int(date.split(".")[1]))
            if formatted_date in birthdays:
                birthdays[formatted_date].append(name)
            else:
                birthdays[formatted_date] = [name]
    today = time.strftime('%d.%m')
    formatted_today = '{:02d}.{:02d}'.format(int(today.split(".")[0]), int(today.split(".")[1]))
    if formatted_today in birthdays:
        names = ", ".join(birthdays[formatted_today])
        send_msg(f"[INFO] 🎂 Сегодня День Рождения празднует: {names}")
        send_sticker('CAACAgQAAxkBAAEBo4Zj2pl459Tj2dLyqA4H_k8orzNKlAACFAMAAtkjZCFxGBEXrJo-iC4E')
def start_mooooooooooooooooooorning_bot():
    r = requests.get('https://sinoptik.ua/погода-варшава')
    soup = BS(r.content, 'html.parser')
    temp = int(re.search(r'\d+', soup.select('.today-temp')[0].text).group())
    send_msg(f"Доброе утро ⛅ \nВаршава, {current_day} \nТемпература: {temp}°c \n---------------------------------------------------\nПара начнется через 30 минут")
def end_eveeeeeeeeeeeeeeeeeeeeening_bot():
    messages = ["💃 Мучения закончены, можно идти отдыхать", "🫶 Пары на сегодня окончены", "🥹 Это была последняя пара, расходимся", "😏 Сегодня пар больше не будет", "💋 Спасибо за внимание, пары закончены", "👌 Больше пар не будет"]
    send_msg(random.choice(messages))
def start_para_bot():
    messages = ["🔔 Пара только что началась!", "🔔 Пара начинается!", "🔔 Пара началась!", "🔔 Занятие началось!", "🔔 Занятие только что началось!", "🔔 Занятие начинается!"]
    send_msg(random.choice(messages))
def five_minutes_before_start_bot():
    messages = ["❗️ Пара начнется через 5 минут", "❗️ Через пару минут начинается занятие", "❗️ Совсем скоро начнется пара", "❗️ Занятие начнется через 5 минут", "❗️ Пара начнется с минуты на минуту", "❗️ Через 5 минут я тебя жду на паре"]
    send_msg(random.choice(messages))
def end_para_bot():
    messages = ["🔔 Пара только что закончилась!", "🔔 Пара закончилась!", "🔔 Эта пара только что завершилась!", "🔔 Пара завершена!", "🔔 Занятие закончено!", "🔔 Пара завершилась, спасибо за внимание!"]
    send_msg(random.choice(messages))
def ched():
    with open("schedule.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        day, time, task = line.strip().split()
        schedule.every().__getattribute__(day).at(time).do(eval(task))

    while True:
        schedule.run_pending()

if __name__ == "__main__":
    thr = Thread(target=ched, daemon=True)
    thr.start()
    bot.polling(none_stop=True, interval=0)