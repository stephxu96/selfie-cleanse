import selfie_recognition.face_detection as face_detection
import selfie_recognition.selfie_training as st
import os
import numpy as np
from PIL import Image
from sklearn import linear_model


def is_selfie(file, selfie=None):
    if face_detection.num_of_faces(file) != 1:
        return False

    x, y = st.classifier('is', 'is_not')

    clf = linear_model.SGDClassifier()

    clf.fit(x, y)

    if clf.predict(np.array(Image.open(file).resize(
            st.RESIZE_X, st.RESIZE_Y).convert('L'))) == 0:
        return True
    else:
        return False


def remove_non_selfies(directory):
    for image in [os.path.join(directory, image_path) for image_path
                  in os.listdir(directory)]:
        if not is_selfie(image):
            os.remove(image)


if __name__ == '__main__':
    pass
