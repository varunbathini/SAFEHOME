import logging
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("HybridLogger")
    if not logger.handlers:
        handler = logging.FileHandler("logs/test_log.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
