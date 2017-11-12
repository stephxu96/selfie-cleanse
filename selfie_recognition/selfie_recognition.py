import face_detection
import os
import numpy as np
from PIL import Image
from sklearn import linear_model


class SelfieCleanse:

    RESIZE_X = 640
    RESIZE_Y = 920

    def __init__(self):
        x, y = self.classifier('is', 'is_not')
        self.clf = linear_model.SGDClassifier()
        self.clf.fit(x, y)

    def create_data_set(self, directory):
        images = []
        for image_path in [os.path.join(directory, image) for image
                           in os.listdir(directory)]:
            try:
                images.append(np.array(Image.open(image_path).resize(
                    (self.RESIZE_X, self.RESIZE_Y),
                    Image.ANTIALIAS).convert('L')).flatten())
            except:
                continue

        return images

    def classifier(self, *args):
        x, y = [], []
        for id_, directory in enumerate(args):
            array = self.create_data_set(directory)
            x.extend(array)
            y.extend([id_] * len(array))

        return x, y

    def is_selfie(self, file, selfie=None):
        if face_detection.num_of_faces(file) != 1:
            return False

        if self.clf.predict([np.array(Image.open(file).resize(
                (self.RESIZE_X, self.RESIZE_Y),
                Image.ANTIALIAS).convert('L')).flatten()]) == [0]:
            return True
        else:
            return False

    def remove_non_selfies(self, directory):
        for image in [os.path.join(directory, image_path) for image_path
                      in os.listdir(directory)]:
            if not self.is_selfie(image):
                os.remove(image)

