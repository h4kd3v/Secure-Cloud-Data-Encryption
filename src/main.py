import logging
import json
from encryption_handler import encrypt_data, decrypt_data, add_encrypted_data, multiply_encrypted_data
from aws_handler import upload_to_aws, download_from_aws
from file_handler import save_encrypted_data, load_encrypted_data
from key_management import save_keys, load_keys

with open('config/config.json') as config_file:
    config = json.load(config_file)

logging.basicConfig(filename=config['logging']['log_file'], level=config['logging']['log_level'])

def main():
    try:
        # Example: Encrypt, upload, download, and decrypt data
        data_to_encrypt = [100, 200, 300, 400, 500]
        encrypted_data = encrypt_data(data_to_encrypt)
        save_encrypted_data(encrypted_data, 'encrypted_data.bin')
        upload_to_aws('encrypted_data.bin', 'encrypted_data.bin')

        download_from_aws('encrypted_data.bin', 'downloaded_data.bin')
        loaded_encrypted_data = load_encrypted_data('downloaded_data.bin', context)
        decrypted_data = decrypt_data(loaded_encrypted_data)
        logging.info("Decrypted Data after Download: %s", decrypted_data)

        # Example: Perform computations on encrypted data
        encrypted_data1 = encrypt_data([50, 60, 70, 80, 90])
        encrypted_data2 = encrypt_data([5, 6, 7, 8, 9])
        save_encrypted_data(encrypted_data1, 'encrypted_data1.bin')
        save_encrypted_data(encrypted_data2, 'encrypted_data2.bin')

        upload_to_aws('encrypted_data1.bin', 'encrypted_data1.bin')
        upload_to_aws('encrypted_data2.bin', 'encrypted_data2.bin')

        download_from_aws('encrypted_data1.bin', 'downloaded_data1.bin')
        download_from_aws('encrypted_data2.bin', 'downloaded_data2.bin')

        loaded_encrypted_data1 = load_encrypted_data('downloaded_data1.bin', context)
        loaded_encrypted_data2 = load_encrypted_data('downloaded_data2.bin', context)

        encrypted_sum = add_encrypted_data(loaded_encrypted_data1, loaded_encrypted_data2)
        encrypted_product = multiply_encrypted_data(loaded_encrypted_data1, loaded_encrypted_data2)

        decrypted_sum = decrypt_data(encrypted_sum)
        decrypted_product = decrypt_data(encrypted_product)

        logging.info("Decrypted Sum after AWS Download: %s", decrypted_sum)
        logging.info("Decrypted Product after AWS Download: %s", decrypted_product)
    except Exception as e:
        logging.error("Main execution error: %s", e)

if __name__ == "__main__":
    main()
