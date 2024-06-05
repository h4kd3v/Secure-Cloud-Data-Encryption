import unittest
from src.aws_handler import upload_to_aws, download_from_aws

class TestAWSHandler(unittest.TestCase):

    def test_upload_to_aws(self):
        result = upload_to_aws('tests/sample.txt', 'sample.txt')
        self.assertTrue(result)

    def test_download_from_aws(self):
        result = download_from_aws('sample.txt', 'tests/downloaded_sample.txt')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
