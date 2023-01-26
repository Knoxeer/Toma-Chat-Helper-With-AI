import telebot
from app_logging import logger

class BotMiddleware(telebot.BaseMiddleware):

    def __init__(self) -> None:
        self.update_types = ['message'] # mechanism based, do not remove

        
    def pre_process(self, message, data):
        logger.info(f"ChatID: {message.chat.id}, User: {message.from_user.username}|{message.from_user.id}")
        
        
    def post_process(self, message, data, exception):
        ...