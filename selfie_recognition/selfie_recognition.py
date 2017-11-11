import face_detection
import os


def is_selfie(file, selfie=None):
    if face_detection.num_of_faces(file) != 1:
        return False


def remove_non_selfies(directory):
    for image in [os.path.join(directory, image_path) for image_path
                  in os.listdir(directory)]:
        if not is_selfie(image):
            os.remove(image)


if __name__ == '__main__':
    pass