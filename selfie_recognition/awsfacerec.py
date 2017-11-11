import boto3
import pprint
import os
import json


def get_client():
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    if not access_key or not secret_key:
        raise Exception('Missing AWS_ACCESS_KEY_ID or AWS_SECRET_ACCESS_KEY')
    return boto3.client('rekognition', region_name='us-east-1',
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key)


if __name__ == '__main__':
    client = get_client()

    with open('images/sample_1.jpg', 'rb') as image_file_1, \
            open('images/sample_2.jpg', 'rb') as image_file_2:
        image_1 = image_file_1.read()
        image_2 = image_file_2.read()

    response = client.detect_faces(Image={'Bytes': image_1})

    print(len(response['FaceDetails']))

    response = client.detect_faces(Image={'Bytes': image_2})

    pprint.pprint(response)

    print(len(response['FaceDetails']))

    response = client.compare_faces(SourceImage={'Bytes': image_1},
                                    TargetImage={'Bytes': image_2})

    pprint.pprint(response)


