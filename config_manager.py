import configparser
import openai

class BotConfig:
    def __init__(self) -> None:
        self.config_parser = configparser.ConfigParser()
        self._read_config() 
        self.__openai_key = self.config_parser['API_KEYS']['OpenAI']
        self.__tgbot_key = self.config_parser['API_KEYS']['TelegramBot']
        self.__chat_id = self.config_parser['SETTINGS']['ChatID']


    def _read_config(self):
        self.config_parser.read("config.ini", encoding="utf-8")

    def __getitem__(self, item):
        return self.config_parser[item]
    
    @property
    def openai_key(self):
        return self.__openai_key
    
    @property
    def tgbot_key(self):
        return self.__tgbot_key

    @property
    def chat_id(self):
        return self.__chat_id