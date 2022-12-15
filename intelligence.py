from skimage.io import imread, imsave
import numpy.typing as npt
import numpy as np


def __find_pixel(map_filename, fn):
    map: npt.NDArray = imread(map_filename)
    width, height, _ = map.shape
    im = np.zeros((width, height), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            r, g, b, _ = map[x, y]
            if fn(r, g, b):
                im[x, y] = 255

    return im


def find_red_pixels(map_filename, upper_threshold=100, lower_threshold=50):
    """Your documentation goes here"""

    im = __find_pixel(map_filename, lambda r, g, b:
        r > upper_threshold
        and g < lower_threshold
        and b < lower_threshold)

    imsave("map-red-pixels.jpg", im)
    return im


def find_cyan_pixels(*args, **kwargs):
    """Your documentation goes here"""


def detect_connected_components(*args, **kwargs):
    """Your documentation goes here"""
    # Your code goes here


def detect_connected_components_sorted(*args, **kwargs):
    """Your documentation goes here"""
    # Your code goes here
