import boto3
import logging
from botocore.exceptions import NoCredentialsError
import json

with open('config/config.json') as config_file:
    config = json.load(config_file)

AWS_ACCESS_KEY = config['aws']['access_key']
AWS_SECRET_KEY = config['aws']['secret_key']
BUCKET_NAME = config['aws']['bucket_name']

def upload_to_aws(local_file, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    try:
        s3.upload_file(local_file, BUCKET_NAME, s3_file)
        logging.info("Upload Successful: %s", s3_file)
        return True
    except FileNotFoundError:
        logging.error("The file was not found: %s", local_file)
        return False
    except NoCredentialsError:
        logging.error("Credentials not available")
        return False

def download_from_aws(s3_file, local_file):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    try:
        s3.download_file(BUCKET_NAME, s3_file, local_file)
        logging.info("Download Successful: %s", s3_file)
        return True
    except FileNotFoundError:
        logging.error("The file was not found: %s", s3_file)
        return False
    except NoCredentialsError:
        logging.error("Credentials not available")
        return False
