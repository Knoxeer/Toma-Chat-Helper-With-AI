import telebot
import time
import schedule
import openai
import random
import re
from threading import Thread
import requests
import datetime
from datetime import datetime
import configparser
import telebot

config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")
bot_api = config['Telegram']['bot_api']
openai_api = config['OpenAI']['ai_api']
bot = telebot.TeleBot(bot_api)
openai.api_key = openai_api

@bot.message_handler(content_types=['text'])
def lalala(message):
    print(f'Имя: {message.from_user.first_name}Логин: {message.from_user.username} UserID: {message.from_user.id} Написал: {message.text} ChatID: {message.chat.id}')
    id = (-1001895899920, -1001341272726, -1001534946044)
    for id in id:
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
            #bot.send_message(message.chat.id, codecs.open('lists/prepods.txt', "r", "utf_8_sig").read())
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
                # 2nd
                day2 = el.select("#bd2 .date")[0].text
                month2 = el.select("#bd2 .month")[0].text
                wday2 = el.select("#bd2 .day-link")[0].text
                t_min2 = el.select(".temperature .min")[1].text
                t_max2 = el.select(".temperature .max")[1].text
                # 3nd
                day3 = el.select("#bd3 .date")[0].text
                month3 = el.select("#bd3 .month")[0].text
                wday3 = el.select("#bd3 .day-link")[0].text
                t_min3 = el.select(".temperature .min")[2].text
                t_max3 = el.select(".temperature .max")[2].text
                # 4nd
                day4 = el.select("#bd4 .date")[0].text
                month4 = el.select("#bd4 .month")[0].text
                wday4 = el.select("#bd4 .day-link")[0].text
                t_min4 = el.select(".temperature .min")[3].text
                t_max4 = el.select(".temperature .max")[3].text
                # 5nd
                day5 = el.select("#bd5 .date")[0].text
                month5 = el.select("#bd5 .month")[0].text
                wday5 = el.select("#bd5 .day-link")[0].text
                t_min5 = el.select(".temperature .min")[4].text
                t_max5 = el.select(".temperature .max")[4].text
                vologist = html.find_all('td', 'cur')[5].text
                #city = el.select("#bd5 .cityName")[0].text
                now_temp = html.select_one('.imgBlock .today-temp').text.strip()
                #city = el.select(".cityName .cityNameShort")[0].text
                current_date = str(datetime.now().date())
                weekdays = ["Понеделник", "Вторник", "Среда", "Четверг", "Пятница", "Субота", "Воскресенье"]
                now = datetime.now()
                current_day = weekdays[now.weekday()]
                bot.send_message(message.chat.id,
                                 f"Сейчас: {now_temp}, {current_day} \nВлажность: {vologist}% \nТемпература: " + t_min + ', ' + t_max + "\n---------------------------------------------------\n" + text + "\n\n🌥 " + day2 + " " + month2 + " | " + wday2 + "\n" + "💨Температура: " + t_min2 + " " + t_max2 + "\n" + "\n" + "🌥 " + day3 + " " + month3 + " | " + wday3 + "\n" + "💨Температура: " + t_min3 + " " + t_max3 + "\n" + "\n" + "🌥 " + day4 + " " + month4 + " | " + wday4 + "\n" + "💨Температура: " + t_min4 + " " + t_max4 + "\n" + "\n" + "🌥 " + day5 + " " + month5 + " | " + wday5 + "\n" + "💨Температура: " + t_min5 + " " + t_max5)
                #bot.send_message(id,
                #                 f"Погода на {current_day} \nТемпература: " + t_min + ', ' + t_max + "\n---------------------------------------------------\nСегодня: " + text + "\n\n🌥Варшава " + day2 + " " + month2 + " " + wday2 + "\n"")
                #bot.send_message(message.chat.id,
                #                    "\nПрогноз погоды на :\n" + date + '\n' + current_date
                #                    + '\n' + t_min + ', ' + t_max + '\n' + '\n' + description + '\n')

        if message.text.lower() in ('преподы', 'список преподавателей', 'викладачі'):
            bot.send_message(message.chat.id,
                             "\n<b>Людмила Просандєєва</b> - Керув. люд. ресурс. у інформ. проектах"
                             "\n<b>Тадеуш Мілош</b> - Мат. аналіз та лін. алгебра"
                             "\n<b>Сергій Хрипко</b> - Осн. електротехн. та електроніки"
                             "\n<b>Ганна Мітрофанова</b> - Осн. економіки"
                             "\n<b>Олена Майборода</b> - Архітектура комп'ютерних систем"
                             "\n<b>Юлія Барачевська</b> - Методол. дослідж. у тех. науках"
                             "\n<b>Олена Майборода</b> - Основи комп'ютерних мереж"
                             "", parse_mode="HTML")
        if message.text.lower() in ('группа', 'список учеников', 'список'):
            bot.send_message(message.chat.id,
                                 "\n1 Adylin Andrii"
                                 "\n2 Aleksenko Artemii"
                                 "\n3 Aleksieiev Serhii"
                                 "\n4 Arutiunian Marharyta"
                                 "\n5 Arziev Alinur"
                                 "\n6 Bielkin Oleksandr"
                                 "\n7 Bilousov Kyrylo"
                                 "\n8 Borovyi Andrii"
                                 "\n9 Burtovyi Yaroslav"
                                 "\n10 Chaika Mykhailo"
                                 "\n11 Demianchuk Oleksandr"
                                 "\n12 Demydov Dmytro"
                                 "\n13 Diachenko Tetiana"
                                 "\n14 Fesenko Illia"
                                 "\n15 Henaliuk Volodymyr"
                                 "\n16 Hololobov Zakhar"
                                 "\n17 Horokhovskyi Volodymyr"
                                 "\n18 Hrushko Oleksii"
                                 "\n19 Kabisov Serhii"
                                 "\n20 Kononikhina Kateryna"
                                 "\n21 Koval Dmytro"
                                 "\n22 Kukh Nazarii"
                                 "\n23 Liutova Viktoriia"
                                 "\n24 Lutsenko Bohdan"
                                 "\n25 Mazurets Maksym"
                                 "\n26 Miniailenko Yevhenii"
                                 "\n27 Nikolayuk Andriy"
                                 "\n28 Osadchyi Davyd"
                                 "\n29 Parkhomenko Vadym"
                                 "\n30 Pedchenko Anton"
                                 "\n31 Penkivska Daria"
                                 "\n32 Perlovskyi Stanislav"
                                 "\n33 Pisotskyi Illia"
                                 "\n34 Puhachov Danil"
                                 "\n35 Rashevskyi Danyl"
                                 "\n36 Rubezhanskyi Oleksii"
                                 "\n37 Rudenko Mykola"
                                 "\n38 Rudenko Vladyslav"
                                 "\n39 Shaikina Olha"
                                 "\n40 Shanchuk Dmytro"
                                 "\n41 Shaposhnykov Andrii"
                                 "\n42 Shcherbak Artur"
                                 "\n43 Shmid Konstiantyn"
                                 "\n44 Stoianova Hanna"
                                 "\n45 Sultanov Ruslan"
                                 "\n46 Sydorov Mykyta"
                                 "\n47 Tolok Anton"
                                 "\n48 Tymoshenko Danylo"
                                 "\n49 Ushakov Oleksii"
                                 "\n50 Uspenskyi Yevheneii"
                                 "\n51 Veretilnyi Anatolii"
                                 "\n52 Voinova Oleksandra"
                                 "\n53 Voloshaniuk Tymofii"
                                 "\n54 Voronenko Sviatoslav"
                                 "\n55 Yelakov Dmytro"
                                 "\n56 Yurchenko Volodymyr"
                                 "\n57 Yurinov Dmytro"
                                 "\n58 Zemlianyi Valerii"
                                 "\n59 Zolotarov Vadym"
                                 "\n60 Zymohliad Dmytro"
                                 "\n61 Ihnatovych Dmytro"
                                 "", parse_mode="HTML")
        return

def happybirthday_bot():
    id = (-1001895899920, -1001341272726, -1001534946044)
    for id in id:
        if time.strftime('%d.%m') == "29.01":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nЯрослава и Виктории!")
            bot.send_sticker(id,'CAACAgIAAxkBAAEBm9pjxoJdN99yNA3oUGIpjP7EH3S2TgACTgIAAladvQow_mttgTIDby0E')
        elif time.strftime('%d.%m') == "11.06":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nКости!") #2
        elif time.strftime('%d.%m') == "11.04":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nНазара!") #3
        elif time.strftime('%d.%m') == "18.09":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nВадима!") #4
        elif time.strftime('%d.%m') == "18.01":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nМарго!")  #5
        elif time.strftime('%d.%m') == "14.12":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nИлльи!")  #6
        elif time.strftime('%d.%m') == "25.03":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nКатерины!")  #7
        elif time.strftime('%d.%m') == "12.01":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nАндрея!")  #8
        elif time.strftime('%d.%m') == "11.01":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nАнатолия!")  #9
        elif time.strftime('%d.%m') == "3.03":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nДаниила!")  #10
        elif time.strftime('%d.%m') == "23.10":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nЗахара!")  #11
        elif time.strftime('%d.%m') == "6.03":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nДанила!")  #12
        elif time.strftime('%d.%m') == "22.01":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nКирила!")  #13
        elif time.strftime('%d.%m') == "26.10":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nАнтона!")  #14
        elif time.strftime('%d.%m') == "13.05":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nДимы!")  #15
        elif time.strftime('%d.%m') == "20.02":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nДимы!")  #16
        elif time.strftime('%d.%m') == "11.02":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nДани!")  #17
        elif time.strftime('%d.%m') == "5.04":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nДимы!")  #18
        elif time.strftime('%d.%m') == "7.04":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nНиколая!")  #19
        elif time.strftime('%d.%m') == "23.01":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nСергея!")  #20
        elif time.strftime('%d.%m') == "26.07":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nЭвгения!")  #21
        elif time.strftime('%d.%m') == "12.06":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nИлльи!")  #22
        elif time.strftime('%d.%m') == "18.10":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nНикиты!")  #23
        elif time.strftime('%d.%m') == "15.11":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nМиши!")  #24
        elif time.strftime('%d.%m') == "12.11":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nОли!")  #25
        elif time.strftime('%d.%m') == "30.6":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nДмитрия!")  #26
        elif time.strftime('%d.%m') == "5.12":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nДмитрия!")  #27
        elif time.strftime('%d.%m') == "27.01":
            bot.send_message(id, "[INFO] Сегодня день рождения:\nДмитрия!")  #28

def start_monday_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        r = requests.get(f'https://ua.sinoptik.ua/погода-варшава')
        html = BS(r.content, 'html.parser')
        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
        weekdays = ["Понеделник", "Вторник", "Среда", "Четверг", "Пятница", "Субота", "Воскресенье"]
        now = datetime.now()
        current_day = weekdays[now.weekday()]
        bot.send_message(id,
                         f"Доброе утро ⛅ \nВаршава, {current_day} \nТемпература: " + t_min + ', ' + t_max + "\n---------------------------------------------------\nПара начнется через 30 минут")

def start_monday_1para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 1/2 Пара только что началась")

def end_monday_1para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 1/2 Пара только что закончилась")

def start_monday_2para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 2/2 Пара только что началась")

def end_monday_2para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 2/2 Пара только что закончилась")
    #monday

def start_tuesday_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        r = requests.get(f'https://ua.sinoptik.ua/погода-варшава')
        html = BS(r.content, 'html.parser')
        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
        weekdays = ["Понеделник", "Вторник", "Среда", "Четверг", "Пятница", "Субота", "Воскресенье"]
        now = datetime.now()
        current_day = weekdays[now.weekday()]
        bot.send_message(id,
                         f"Доброе утро ⛅ \nВаршава, {current_day} \nТемпература: " + t_min + ', ' + t_max + "\n---------------------------------------------------\nПара начнется через 30 минут")

def start_tuesday_1para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 1/2 Пара только что началась")

def end_tuesday_1para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 1/2 Пара только что закончилась")

def start_tuesday_2para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 2/2 Пара только что началась")

def end_tuesday_2para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 2/2 Пара только что закончилась")

def start_wednesday_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        r = requests.get(f'https://ua.sinoptik.ua/погода-варшава')
        html = BS(r.content, 'html.parser')
        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
        weekdays = ["Понеделник", "Вторник", "Среда", "Четверг", "Пятница", "Субота", "Воскресенье"]
        now = datetime.now()
        current_day = weekdays[now.weekday()]
        bot.send_message(id,
                         f"Доброе утро ⛅ \nВаршава, {current_day} \nТемпература: " + t_min + ', ' + t_max + "\n---------------------------------------------------\nПара начнется через 30 минут")

def start_wednesday_1para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 1/3 Пара только что началась")

def end_wednesday_1para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 1/3 Пара только что закончилась")

def start_wednesday_2para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 2/3 Пара только что началась")

def end_wednesday_2para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 2/3 Пара только что закончилась")

def start_wednesday_3para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 3/3 Пара только что началась")

def end_wednesday_3para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 3/3 Пара только что закончилась")
    # wednesday

def start_thursday_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        r = requests.get(f'https://ua.sinoptik.ua/погода-варшава')
        html = BS(r.content, 'html.parser')
        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
        weekdays = ["Понеделник", "Вторник", "Среда", "Четверг", "Пятница", "Субота", "Воскресенье"]
        now = datetime.now()
        current_day = weekdays[now.weekday()]
        bot.send_message(id,
                         f"Доброе утро ⛅ \nВаршава, {current_day} \nТемпература: " + t_min + ', ' + t_max + "\n---------------------------------------------------\nПара начнется через 30 минут")

def start_thursday_1para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 1/4 Пара только что началась")

def end_thursday_1para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 1/4 Пара только что закончилась")

def start_thursday_2para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 2/4 Пара только что началась")

def end_thursday_2para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 2/4 Пара только что закончилась")

def start_thursday_3para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 3/4 Пара только что началась")

def end_thursday_3para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 3/4 Пара только что закончилась")

def start_thursday_4para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 4/4 Пара только что началась")

def end_thursday_4para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 4/4 Пара только что закончилась")
    # thursday

def start_friday_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        r = requests.get(f'https://ua.sinoptik.ua/погода-варшава')
        html = BS(r.content, 'html.parser')
        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
        weekdays = ["Понеделник", "Вторник", "Среда", "Четверг", "Пятница", "Субота", "Воскресенье"]
        now = datetime.now()
        current_day = weekdays[now.weekday()]
        bot.send_message(id,
                         f"Доброе утро ⛅ \nВаршава, {current_day} \nТемпература: " + t_min + ', ' + t_max + "\n---------------------------------------------------\nПара начнется через 30 минут")

def start_friday_1para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
     bot.send_message(id, "[INFO] 1/2 Пара только что началась")

def end_friday_1para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 1/2 Пара только что закончилась")

def start_friday_2para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 2/2 Пара только что началась")

def end_friday_2para_bot():
    id = (-1001895899920, -1001534946044)
    for id in id:
        bot.send_message(id, "[INFO] 2/2 Пара только что закончилась")
    #friday

def ched():
        # monday
        schedule.every().monday.at("10:15").do(start_monday_bot)
        schedule.every().monday.at("10:45").do(start_monday_1para_bot)
        schedule.every().monday.at("14:00").do(end_monday_1para_bot)
        schedule.every().monday.at("14:30").do(start_monday_2para_bot)
        schedule.every().monday.at("17:45").do(end_monday_2para_bot)
        #tuesday
        schedule.every().tuesday.at("10:15").do(start_tuesday_bot)
        schedule.every().tuesday.at("10:45").do(start_tuesday_1para_bot)
        schedule.every().tuesday.at("14:00").do(end_tuesday_1para_bot)
        schedule.every().tuesday.at("14:30").do(start_tuesday_2para_bot)
        schedule.every().tuesday.at("17:45").do(end_tuesday_2para_bot)
        #wednesday
        schedule.every().wednesday.at("10:15").do(start_wednesday_bot)
        schedule.every().wednesday.at("10:45").do(start_wednesday_1para_bot)
        schedule.every().wednesday.at("14:00").do(end_wednesday_1para_bot)
        schedule.every().wednesday.at("14:30").do(start_wednesday_2para_bot)
        schedule.every().wednesday.at("17:45").do(end_wednesday_2para_bot)
        schedule.every().wednesday.at("19:45").do(start_wednesday_3para_bot)
        schedule.every().wednesday.at("21:15").do(end_wednesday_3para_bot)
        #thursday
        schedule.every().thursday.at("08:30").do(start_thursday_bot)
        schedule.every().thursday.at("09:00").do(start_thursday_1para_bot)
        schedule.every().thursday.at("12:15").do(end_thursday_1para_bot)
        schedule.every().thursday.at("12:30").do(start_thursday_2para_bot)
        schedule.every().thursday.at("16:00").do(end_thursday_2para_bot)
        schedule.every().thursday.at("16:15").do(start_thursday_3para_bot)
        schedule.every().thursday.at("19:30").do(end_thursday_3para_bot)
        schedule.every().thursday.at("19:45").do(start_thursday_4para_bot)
        schedule.every().thursday.at("21:15").do(end_thursday_4para_bot)
        #friday
        schedule.every().day.at("19:51").do(start_friday_bot)
        schedule.every().friday.at("09:45").do(start_friday_1para_bot)
        schedule.every().friday.at("13:00").do(end_friday_1para_bot)
        schedule.every().friday.at("13:30").do(start_friday_2para_bot)
        schedule.every().friday.at("16:45").do(end_friday_2para_bot)
        schedule.every().day.at("13:00").do(happybirthday_bot)
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    thr = Thread(target=ched, daemon=True)
    thr.start()
    bot.polling(none_stop=True, interval=0)
    print("Бот приостановил свою работу!")
