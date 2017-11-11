from selfie_recognition.aws_credentials import create_client


def num_of_faces(file):
    client = create_client()

    with open(file, 'rb') as image_file:
        image = image_file.read()

    return len(client.detect_faces(Image={'Bytes': image})['FaceDetails'])
