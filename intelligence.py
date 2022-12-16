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


def __binary_image(im: npt.NDArray[np.uint8]) -> npt.NDArray[np.float16]:
    """Converts an image to a binary image."""
    return np.float16(1.0) * (im > 0)


def find_red_pixels(map_filename: str, upper_threshold: int = 100, lower_threshold: int = 50) -> npt.NDArray[np.float16]:
    """Returns a binary image with the red pixels of the map."""

    im = __find_pixel(map_filename, lambda r, g, b:
                      r > upper_threshold
                      and g < lower_threshold
                      and b < lower_threshold)

    imsave("map-red-pixels.jpg", im)
    return __binary_image(im)


def find_cyan_pixels(map_filename, upper_threshold=100, lower_threshold=50) -> npt.NDArray[np.float16]:
    """Your documentation goes here"""

    im = __find_pixel(map_filename, lambda r, g, b:
                      r < lower_threshold
                      and g > upper_threshold
                      and b > upper_threshold)

    imsave("map-cyan-pixels.jpg", im)
    return __binary_image(im)


def detect_connected_components(*args, **kwargs):
    """Your documentation goes here"""
    # Your code goes here


def detect_connected_components_sorted(*args, **kwargs):
    """Your documentation goes here"""
    # Your code goes here
