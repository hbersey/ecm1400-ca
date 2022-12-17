from skimage.io import imread, imsave
import numpy.typing as npt
import numpy as np
from queue import Queue


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


def find_red_pixels(map_filename: str, upper_threshold: int = 100, lower_threshold: int = 50) -> npt.NDArray[np.float16]:
    """Returns a binary image with the red pixels of the map."""

    im = __find_pixel(map_filename, lambda r, g, b:
                      r > upper_threshold
                      and g < lower_threshold
                      and b < lower_threshold)

    imsave("map-red-pixels.jpg", im)
    return im


def find_cyan_pixels(map_filename, upper_threshold=100, lower_threshold=50) -> npt.NDArray[np.float16]:
    """Your documentation goes here"""

    im = __find_pixel(map_filename, lambda r, g, b:
                      r < lower_threshold
                      and g > upper_threshold
                      and b > upper_threshold)

    imsave("map-cyan-pixels.jpg", im)
    return im


def detect_connected_components(IMG: npt.NDArray[np.uint]):
    """Your documentation goes here"""

    MARK = np.zeros(IMG.shape, dtype=np.uint8)
    Q = Queue()

    for x, y in np.ndindex(IMG.shape):
        if IMG[x, y] == 255 and MARK[x, y] == 0:
            MARK[x, y] = 1
            Q.put((x, y))
            while not Q.empty():
                m, n = Q.get()
                for s in range(m - 1, m + 2):
                    for t in range(n - 1, n + 2):
                        if (s == m and t == n) or s < 0 or s >= IMG.shape[0] or t < 0 or t >= IMG.shape[1]:
                            continue
                        if IMG[s, t] == 255 and MARK[s, t] == 0:
                            MARK[s, t] = 1
                            Q.put((s, t))

    return MARK


def detect_connected_components_sorted(*args, **kwargs):
    """Your documentation goes here"""
    # Your code goes here
