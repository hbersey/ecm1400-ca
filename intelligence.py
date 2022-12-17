from skimage.io import imread, imsave
import numpy.typing as npt
import numpy as np
from utils import NDQueue


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

    f = open("cc-output-2a.txt", "w")

    marked = np.zeros(IMG.shape, dtype=np.uint8)
    queue = NDQueue(initial_size=32, dtype="2u2")

    component_n = 0
    for p_x, p_y in np.ndindex(IMG.shape):
        if IMG[p_x, p_y] == 255 and marked[p_x, p_y] == 0:
            marked[p_x, p_y] = 1
            queue.enqueue((p_x, p_y))

            pixels_n = 0
            component_n += 1

            while not queue.is_empty():
                pixels_n += 1
                q_m, q_n = queue.dequeue()
                for n_s in range(q_m - 1, q_m + 2):
                    for n_t in range(q_n - 1, q_n + 2):
                        if (n_s == q_m and n_t == q_n) or n_s < 0 or n_s >= IMG.shape[0] or n_t < 0 or n_t >= IMG.shape[1]:
                            continue
                        if IMG[n_s, n_t] == 255 and marked[n_s, n_t] == 0:
                            marked[n_s, n_t] = 1
                            queue.enqueue((n_s, n_t))
            f.write(
                f"Connected Component {component_n}, number of pixels = {pixels_n}\n")

    f.write(f"Total number of connected components = {component_n}\n")
    f.close()
    return marked


def detect_connected_components_sorted(*args, **kwargs):
    """Your documentation goes here"""
    # Your code goes here
