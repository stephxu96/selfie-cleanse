import os
import numpy as np
from PIL import Image

PICTURE_RESIZE_X = 640
PICTURE_RESIZE_Y = 920


def create_data_set(directory):
    images = [np.array(Image.open(image_path).resize(
        (PICTURE_RESIZE_X, PICTURE_RESIZE_Y), Image.ANTIALIAS).convert('L'))
              for image_path in [os.path.join(directory, image) for image
                                 in os.listdir(directory)]]

    return images


def classifier(*args):
    x, y = np.array([]), np.array([])
    for id_, directory in enumerate(args):
        array = create_data_set(directory)
        x = np.append(x, [id_] * len(array))
        y = np.append(y, array)

    return x, y


def main():
    classifier('is', 'is_not')


if __name__ == '__main__':
    main()
