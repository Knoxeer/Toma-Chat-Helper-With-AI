import tgbot
import app_logging
import argparse

# def send_msg(message): # ДР + Пары
#     ids = (-1001895899920, -1001341272726, -1001534946044)
#     for id in ids:
#         bot.send_message(id, message)
                                                                                
# def dead_orks_bot():
#     r = requests.get('https://www.pravda.com.ua/rus/')
#     soup = BS(r.content, 'html.parser')
#     orks = soup.select('.war_num')[0].text
#     send_msg(f"Мертвых орков уже:{orks}")

# def happybirthday_bot():
#     birthdays = {}
#     with open("birthdays.txt", "r") as f:
#         for line in f:
#             date, name = line.strip().split("|")
#             birthdays[date] = name
#     today = time.strftime('%d.%m')
#     if today in birthdays:
#         send_msg(f"[INFO] Сегодня день рождения:\n{birthdays[today]}")

# def start_mooooooooooooooooooorning_bot():
#     r = requests.get('https://sinoptik.ua/погода-варшава')
#     soup = BS(r.content, 'html.parser')
#     temp = soup.select('.temperature .min')[0].text + ', ' + soup.select('.temperature .max')[0].text
#     send_msg(f"Доброе утро ⛅ \nВаршава, {current_day} \nТемпература: {temp} \n---------------------------------------------------\nПара начнется через 30 минут")

# def end_eveeeeeeeeeeeeeeeeeeeeening_bot():
#     send_msg("Мучения закончены, можно идти отдыхать")

# def start_para_bot():
#     send_msg("[INFO] Пара только что началась!")

# def five_minutes_before_start_bot():
#     send_msg("[INFO] Пара начнется через 5 минут!")

# def end_para_bot():
#     send_msg("[INFO] Пара только что закончилась!")

# def ched():
#     with open("schedule.txt", "r") as file:
#         lines = file.readlines()
#     for line in lines:
#         day, time, t
#         sk = line.strip().split()
#         schedule.every(.__getattribute__(
#             day).at(time).do(eva
#     while True:
#         schedule.run_pending()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some flags.')
    parser.add_argument('-logLevel', type=str, help='A flag to choose logging level ("DEBUG","INFO")')
    args = parser.parse_args()  
    
    app_logging.configure_logger(args.logLevel)
    bot = tgbot.CustomBot(use_class_middlewares=True)
    

    # thr = Thread(target=ched, daemon=True)
    # thr.start()
    bot.polling(none_stop=True, interval=0)
