import logging

def save_encrypted_data(encrypted_data, file_name):
    try:
        with open(file_name, 'wb') as f:
            f.write(encrypted_data.save())
        logging.info("Encrypted data saved: %s", file_name)
    except Exception as e:
        logging.error("Error saving encrypted data: %s", e)
        raise

def load_encrypted_data(file_name, context):
    try:
        encrypted_data = seal.Ciphertext()
        with open(file_name, 'rb') as f:
            encrypted_data.load(context, f.read())
        logging.info("Encrypted data loaded: %s", file_name)
        return encrypted_data
    except Exception as e:
        logging.error("Error loading encrypted data: %s", e)
        raise
