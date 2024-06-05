import unittest
from src.encryption_handler import encrypt_data, decrypt_data

class TestEncryptionHandler(unittest.TestCase):

    def test_encrypt_decrypt_data(self):
        data = [1, 2, 3, 4, 5]
        encrypted_data = encrypt_data(data)
        decrypted_data = decrypt_data(encrypted_data)
        self.assertEqual(data, decrypted_data)

if __name__ == '__main__':
    unittest.main()
