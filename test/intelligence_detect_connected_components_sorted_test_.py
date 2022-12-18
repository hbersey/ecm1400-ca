import numpy as np
import intelligence as mi

__IMG = np.array([
    [255, 0, 0, 0, 0],
    [255, 255, 0, 0, 0],
    [0, 0, 0, 255, 255],
    [0, 0, 0, 255, 255],
    [0, 0, 0, 0, 0]
])

__MARK = np.array([
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0]
])


def test_detect_connected_components():
    im = mi.find_red_pixels("data/map.png")
    marked = mi.detect_connected_components(im)
    mi.detect_connected_components_sorted(marked)

    f = open("cc-output2b.txt", "r")
    lines = f.readlines()
    f.close()

    assert lines[0] == "Connected Component 130, number of pixels = 12364"
    assert lines[1] == "Connected Component 110, number of pixels = 8172"
    assert lines[2] == "Connected Component 117, number of pixels = 4716"

    assert lines[len(lines) - 1] == "Total number of connected components = 223"