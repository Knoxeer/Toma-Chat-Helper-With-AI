import logging

def echo(message):
    ...    
#     for id in chat_id_1:
#         if "Toma" in message.text or "toma" in message.text or "скайнет" in message.text or "Скайнет" in message.text or "ботинок" in message.text or "Ботинок" in message.text or "Тома" in message.text or "тома" in message.text:
#             bot.send_chat_action(message.chat.id, 'typing')
#             message.text = re.sub(r'(Toma|toma|скайнет|Скайнет|ботинок|Ботинок|Тома|тома)', '', message.text)
#             response = openai.Completion.create(model="text-davinci-003", prompt=message.text, max_tokens=1000)
#             full_response = response['choices'][0]['text']  # Use the text property of the first element of the choices list to access the full response
#             lines = full_response.splitlines()  # Split the response into individual lines
#             for line in lines:  # Iterate over the lines
#                 try:
#                     bot.send_message(message.chat.id, line)  # Send each line back to the user as a separate message
#                 except Exception as e:
#                     print(e)

#         elif message.text.lower() in ('я тебя люблю', 'ты моя любовь', 'это секс', 'секс', 'это любовь'):
#             bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBm9pjxoJdN99yNA3oUGIpjP7EH3S2TgACTgIAAladvQow_mttgTIDby0E')

#         if any(x in message.text for x in # намнного лучше работает, чем if message.text.lower()
#                ("Она отмечала?", "Уже отмечала?", "Она отмечает?", "А она уже отметила?", "отмечала?", "Уже отмечала?", "отмечает?")):
#             responses = ['Советую поторопиться', 'Кто его знает', 'Пока что не знаю', 'Лучше ускориться', '50/50', 'Я сказала, что ты задержишься', 'Ага ага']
#             response = random.choice(responses)
#             bot.send_message(message.chat.id, response)

#         if message.text.lower() in ('преподы', 'список преподавателей', 'викладачі'):
#             bot.send_message(message.chat.id, codecs.open('prepods.txt', "r", "utf_8_sig").read())
#         if message.text.lower() in ('группа', 'список учеников', 'список'):
#             bot.send_message(message.chat.id, codecs.open('students.txt', "r", "utf_8_sig").read())
#         if message.text.lower() in ('орков', 'статистика', 'мертвых орков', 'сколько мертвых орков?'):
#             r = requests.get('https://www.pravda.com.ua/rus/')
#             soup = BS(r.content, 'html.parser')
#             orks = soup.select('.war_num')[0].text
#             bot.send_message(message.chat.id,f"Мертвых орков уже: {orks}")
#         return