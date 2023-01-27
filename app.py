from typing import Optional
import config_manager
import telebot
from middleware import BotMiddleware
import handlers

class CustomBot(telebot.TeleBot):
    
    def __init__(self, 
        parse_mode: Optional[str] = None, 
        threaded: Optional[bool] = True, 
        skip_pending: Optional[bool] = False, 
        num_threads: Optional[int] = 2, 
        next_step_backend: Optional[telebot.HandlerBackend] = None, 
        reply_backend: Optional[telebot.HandlerBackend] = None, 
        exception_handler: Optional[telebot.ExceptionHandler] = None, 
        last_update_id: Optional[int] = 0, 
        suppress_middleware_excepions: Optional[bool] = False, 
        state_storage: Optional[telebot.StateStorageBase] = ..., 
        use_class_middlewares: Optional[bool] = False, 
        disable_web_page_preview: Optional[bool] = None, 
        disable_notification: Optional[bool] = None, 
        protect_content: Optional[bool] = None, 
        allow_sending_without_reply: Optional[bool] = None, 
        colorful_logs: Optional[bool] = False):

        self.config_mng: Optional[config_manager.BotConfig] = None        
        self._configure_config_mng()
        super().__init__(self.config_mng.tgbot_key, parse_mode, threaded, skip_pending, num_threads, next_step_backend, reply_backend, exception_handler, last_update_id, suppress_middleware_excepions, state_storage, use_class_middlewares, disable_web_page_preview, disable_notification, protect_content, allow_sending_without_reply, colorful_logs)    
        
        self._configure_middleware()
        
    def _configure_handlers(self):        
        self.handle_message(handlers.echo, content_types=["text"])

    def _configure_config_mng(self):
        self.config_mng = config_manager.BotConfig()
        
    def _configure_middleware(self):
        self.setup_middleware(BotMiddleware())

    def _configure_scheduler(self):
        ...

    def handle_message(self, handler, **params):
        self.message_handler(**params)(handler)
    