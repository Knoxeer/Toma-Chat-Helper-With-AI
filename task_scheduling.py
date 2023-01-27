import schedule
import telebot
from dataclasses import dataclass

class BotScheduler(schedule.Scheduler):
    def __init__(self, bot:telebot.TeleBot) -> None:
        super().__init__()
        self.bot = bot

    def add_lesson(self):
        ...

    def _create_lesson(self):
        ...

class LessonJob(schedule.Job):
    def __init__(self, interval: int, scheduler: schedule.Scheduler = None, ):
        super().__init__(interval, scheduler)

