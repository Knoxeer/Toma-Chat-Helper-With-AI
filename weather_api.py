import requests
import time

class WeatherForecasting:
    
    @classmethod
    def get_weather(): 
        ...
        # if "погода" in message.text or "прогноз" in message.text or "Погода" in message.text or "Прогноз" in message.text:
        #     message.text = re.sub(r'(погода|прогноз|Погода|Прогноз)', '', message.text)
        #     url = 'https://sinoptik.ua/погода-{}'.format(str.lower(message.text))
        #     print(url)
        #     r = requests.get(url)
        #     html = BS(r.content, 'html.parser')
        #     for el in html.select('#content'):
        #         t_min = el.select('.temperature .min')[0].text
        #         t_max = el.select('.temperature .max')[0].text
        #         text = el.select('.wDescription .description')[0].text
        #         day2 = el.select("#bd2 .date")[0].text
        #         month2 = el.select("#bd2 .month")[0].text
        #         wday2 = el.select("#bd2 .day-link")[0].text
        #         t_min2 = el.select(".temperature .min")[1].text
        #         t_max2 = el.select(".temperature .max")[1].text
        #         day3 = el.select("#bd3 .date")[0].text
        #         month3 = el.select("#bd3 .month")[0].text
        #         wday3 = el.select("#bd3 .day-link")[0].text
        #         t_min3 = el.select(".temperature .min")[2].text
        #         t_max3 = el.select(".temperature .max")[2].text
        #         day4 = el.select("#bd4 .date")[0].text
        #         month4 = el.select("#bd4 .month")[0].text
        #         wday4 = el.select("#bd4 .day-link")[0].text
        #         t_min4 = el.select(".temperature .min")[3].text
        #         t_max4 = el.select(".temperature .max")[3].text
        #         day5 = el.select("#bd5 .date")[0].text
        #         month5 = el.select("#bd5 .month")[0].text
        #         wday5 = el.select("#bd5 .day-link")[0].text
        #         t_min5 = el.select(".temperature .min")[4].text
        #         t_max5 = el.select(".temperature .max")[4].text
        #         vologist = html.find_all('td', 'cur')[5].text
        #         now_temp = html.select_one('.imgBlock .today-temp').text.strip()
        #         current_date = str(datetime.now().date())
        #         bot.send_message(message.chat.id,f"Сейчас: {now_temp}, {current_day} \nВлажность: {vologist}% \nТемпература: " + t_min + ', ' + t_max + "\n---------------------------------------------------\n" + text + "\n\n🌥 " + day2 + " " + month2 + " | " + wday2 + "\n" + "💨Температура: " + t_min2 + " " + t_max2 + "\n" + "\n" + "🌥 " + day3 + " " + month3 + " | " + wday3 + "\n" + "💨Температура: " + t_min3 + " " + t_max3 + "\n" + "\n" + "🌥 " + day4 + " " + month4 + " | " + wday4 + "\n" + "💨Температура: " + t_min4 + " " + t_max4 + "\n" + "\n" + "🌥 " + day5 + " " + month5 + " | " + wday5 + "\n" + "💨Температура: " + t_min5 + " " + t_max5)
