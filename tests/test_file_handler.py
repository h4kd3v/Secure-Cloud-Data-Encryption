import unittest
from src.file_handler import save_encrypted_data, load_encrypted_data
from src.encryption_handler import encrypt_data

class TestFileHandler(unittest.TestCase):

    def test_save_load_encrypted_data(self):
        data = [1, 2, 3, 4, 5]
        encrypted_data = encrypt_data(data)
        save_encrypted_data(encrypted_data, 'tests/encrypted_data.bin')
        loaded_encrypted_data = load_encrypted_data('tests/encrypted_data.bin', context)
        decrypted_data = decrypt_data(loaded_encrypted_data)
        self.assertEqual(data, decrypted_data)

if __name__ == '__main__':
    unittest.main()
