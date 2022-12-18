import intelligence as mi
import numpy as np

__IMG = np.array([
    [[0, 255, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255]],
    [[0, 0, 0, 255], [0, 255, 0, 255], [0, 0, 0, 255]],
    [[0, 0, 0, 255], [0, 0, 0, 255], [0, 255, 0, 255]],
])


def __is_green(_r, g, _b):
    return g == 255


def test_find_pixels():
    assert np.array_equal(mi.__find_pixel(__IMG, __is_green), np.array([
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255],
    ]))

    # Limited test cases because this is a private function and will never receive invalid parameters.