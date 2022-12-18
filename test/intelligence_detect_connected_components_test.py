import numpy as np
import intelligence as mi

__IMG = np.array([
    [255, 0, 0, 0, 0 ],
    [255, 255, 0, 0, 0 ],
    [0, 0, 0, 255, 255 ],
    [0, 0, 0, 255, 255 ],
    [0, 0, 0, 0, 0 ]
])

__MARK = np.array([
    [1, 0, 0, 0, 0 ],
    [1, 1, 0, 0, 0 ],
    [0, 0, 0, 1, 1 ],
    [0, 0, 0, 1, 1 ],
    [0, 0, 0, 0, 0 ]
])

def test_detect_connected_components():
    assert np.array_equal(mi.detect_connected_components(__IMG), __MARK)

    # alot of this is covered in test_detect_connected_components_sorted
