import logging

logger = logging.getLogger(__name__)

def configure_logger(level):
    global logger
    
    logging.basicConfig(level=level, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    
    