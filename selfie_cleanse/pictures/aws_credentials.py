import boto3
import os


def create_client():
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    if not access_key or not secret_key:
        raise Exception('Missing AWS_ACCESS_KEY_ID or AWS_SECRET_ACCESS_KEY')
    return boto3.client('rekognition', region_name='us-east-1',
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key)
