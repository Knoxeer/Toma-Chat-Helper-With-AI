import telebot; import time; import schedule; import openai; import random; import configparser; import telebot
import re; from threading import Thread; import requests; import datetime; from datetime import datetime
from bs4 import BeautifulSoup as BS; import codecs

config = configparser.ConfigParser();       config.read("settings.ini", encoding="utf-8")
bot_api = config['Telegram']['bot_api'];    openai_api = config['OpenAI']['ai_api']
bot = telebot.TeleBot(bot_api);             openai.api_key = openai_api
id_chat_config = config['Telegram']['id_chat'];

weekdays = ["Понеделник", "Вторник", "Среда", "Четверг", "Пятница", "Субота", "Воскресенье"]
now = datetime.now()
current_day = weekdays[now.weekday()]
def send_msg(message): # ДР + Пары
    ids = (-1001895899920, -1001341272726, -1001534946044)
    for id in ids:
        bot.send_message(id, message)
@bot.message_handler(content_types=['text'])
def lalala(message):
    print(f'Имя: {message.from_user.first_name}Логин: {message.from_user.username} UserID: {message.from_user.id} Написал: {message.text} ChatID: {message.chat.id}')
    id_chat_config
    for id in id_chat_config:
        if "Toma" in message.text or "toma" in message.text or "скайнет" in message.text or "Скайнет" in message.text or "ботинок" in message.text or "Ботинок" in message.text or "Тома" in message.text or "тома" in message.text:
            bot.send_chat_action(message.chat.id, 'typing')
            message.text = re.sub(r'(Toma|toma|скайнет|Скайнет|ботинок|Ботинок|Тома|тома)', '', message.text)
            response = openai.Completion.create(model="text-davinci-003", prompt=message.text, max_tokens=1000)
            full_response = response['choices'][0]['text']  # Use the text property of the first element of the choices list to access the full response
            lines = full_response.splitlines()  # Split the response into individual lines
            for line in lines:  # Iterate over the lines
                try:
                    bot.send_message(message.chat.id, line)  # Send each line back to the user as a separate message
                except Exception as e:
                    print(e)

        if any(x in message.text for x in
               ("сук", "лох", "кака", "какашка", "пенис", "писюн", "lox", "blat", "suka", "блять", "пизда", "блядь", "хуи",
                "на хуй", "на хуи", "блят", "блеат", "взьеб", "вьеб", "вжопу", "высрал", "вжопе", "гавню", "гнида", "засран",
                "дибил", "бляд", "гомик", "гандон", "гондон", "залуп", "мудил", "обосал", "педик", "пидар", "пздц", "пох",
                "суки", "ублюдок", "ублюдки", "сосать", "уебок", "пидорас", "шлюха", "заебали", "пошли нахуй", "нахуй", "выебал")):
            responses = ['Не материтесь (>_<)', 'Пожалуйста, не используйте такие слова', 'Пожалуйста, будьте вежливы',
                         'Пожалуйста, обращайтесь к другим с уважением', 'Не используйте оскорбительную лексику',
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
            bot.send_message(message.chat.id,f"Мертвых орков уже: {orks}")
        return
def happybirthday_bot():
    birthdays = {}
    with open("birthdays.txt", "r") as f:
        for line in f:
            date, name = line.strip().split("|")
            birthdays[date] = name
    today = time.strftime('%d.%m')
    if today in birthdays:
        send_msg(f"[INFO] Сегодня день рождения:\n{birthdays[today]}")

def dead_orks_bot():
    r = requests.get('https://www.pravda.com.ua/rus/')
    soup = BS(r.content, 'html.parser')
    orks = soup.select('.war_num')[0].text
    send_msg(f"Мертвых орков на сегодня:{orks}")
def start_mooooooooooooooooooorning_bot():
    r = requests.get('https://sinoptik.ua/погода-варшава')
    soup = BS(r.content, 'html.parser')
    temp = soup.select('.temperature .min')[0].text + ', ' + soup.select('.temperature .max')[0].text
    send_msg(f"Доброе утро ⛅ \nВаршава, {current_day} \nТемпература: {temp} \n---------------------------------------------------\nПара начнется через 30 минут")
def end_eveeeeeeeeeeeeeeeeeeeeening_bot():
    send_msg("Мучения закончены, можно идти отдыхать")
def start_para_bot():
    send_msg("[INFO] Пара только что началась!")
def five_minutes_before_start_bot():
    send_msg("[INFO] Пара начнется через 5 минут!")
def end_para_bot():
    send_msg("[INFO] Пара только что закончилась!")
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