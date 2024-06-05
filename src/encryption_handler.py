import seal
import json
import logging

with open('config/config.json') as config_file:
    config = json.load(config_file)

POLY_MODULUS_DEGREE = config['encryption']['poly_modulus_degree']
PLAIN_MODULUS = config['encryption']['plain_modulus']

# Setup SEAL context
parms = seal.EncryptionParameters(seal.scheme_type.BFV)
parms.set_poly_modulus_degree(POLY_MODULUS_DEGREE)
parms.set_coeff_modulus(seal.CoeffModulus.BFVDefault(POLY_MODULUS_DEGREE))
parms.set_plain_modulus(PLAIN_MODULUS)

context = seal.SEALContext(parms)

# Key Generation
keygen = seal.KeyGenerator(context)
public_key = keygen.public_key()
secret_key = keygen.secret_key()
relin_keys = keygen.relin_keys()

encryptor = seal.Encryptor(context, public_key)
decryptor = seal.Decryptor(context, secret_key)
evaluator = seal.Evaluator(context)
batch_encoder = seal.BatchEncoder(context)

def save_key(key, file_name):
    with open(file_name, 'wb') as f:
        f.write(key.save())
    logging.info("Key saved: %s", file_name)

def load_key(key_class, file_name):
    key = key_class()
    with open(file_name, 'rb') as f:
        key.load(context, f.read())
    logging.info("Key loaded: %s", file_name)
    return key

def encrypt_data(data):
    try:
        plain = seal.Plaintext()
        batch_encoder.encode(data, plain)
        encrypted = seal.Ciphertext()
        encryptor.encrypt(plain, encrypted)
        logging.info("Data encrypted successfully")
        return encrypted
    except Exception as e:
        logging.error("Encryption error: %s", e)
        raise

def decrypt_data(encrypted_data):
    try:
        plain = seal.Plaintext()
        decryptor.decrypt(encrypted_data, plain)
        data = batch_encoder.decode_int64(plain)
        logging.info("Data decrypted successfully")
        return data
    except Exception as e:
        logging.error("Decryption error: %s", e)
        raise

def add_encrypted_data(encrypted1, encrypted2):
    try:
        result = seal.Ciphertext()
        evaluator.add(encrypted1, encrypted2, result)
        logging.info("Addition on encrypted data performed successfully")
        return result
    except Exception as e:
        logging.error("Error in addition operation: %s", e)
        raise

def multiply_encrypted_data(encrypted1, encrypted2):
    try:
        result = seal.Ciphertext()
        evaluator.multiply(encrypted1, encrypted2, result)
        evaluator.relinearize_inplace(result, relin_keys)
        logging.info("Multiplication on encrypted data performed successfully")
        return result
    except Exception as e:
        logging.error("Error in multiplication operation: %s", e)
        raise
