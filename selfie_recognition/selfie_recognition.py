import face_detection
import selfie_training
import os
import numpy as np
from PIL import Image
from sklearn import linear_model


def is_selfie(file, selfie=None):
    if face_detection.num_of_faces(file) != 1:
        return False

    x, y = selfie_training.classifier('is', 'is_not')

    clf = linear_model.SGDClassifier()

    clf.fit(x, y)

    print(clf.predict(np.array(Image.open(file).resize(
        selfie_training.PICTURE_RESIZE_X,
        selfie_training.PICTURE_RESIZE_Y).convert('L'))))


def remove_non_selfies(directory):
    for image in [os.path.join(directory, image_path) for image_path
                  in os.listdir(directory)]:
        if not is_selfie(image):
            os.remove(image)


if __name__ == '__main__':
    pass