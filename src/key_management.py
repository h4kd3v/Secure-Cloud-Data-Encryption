import logging
import seal

from encryption_handler import context

def save_key(key, file_name):
    try:
        with open(file_name, 'wb') as f:
            f.write(key.save())
        logging.info("Key saved: %s", file_name)
    except Exception as e:
        logging.error("Error saving key: %s", e)
        raise

def load_key(key_class, file_name):
    try:
        key = key_class()
        with open(file_name, 'rb') as f:
            key.load(context, f.read())
        logging.info("Key loaded: %s", file_name)
        return key
    except Exception as e:
        logging.error("Error loading key: %s", e)
        raise
