from skimage.io import imread, imsave
import numpy.typing as npt
import numpy as np
import utils
import typing as t


def __find_pixel(map: npt.NDArray, fn: t.Callable[[int, int, int], bool]) -> npt.NDArray[np.uint8]:
    """
    Returns a binary image with the pixels of the map that match the given function, ``fn``.

    Parameters
    ----------
    map_filename: str
        The filename of the map image
    fn: Callable[[int, int, int], bool]
        A function that takes the red, green and blue values of a pixel and returns True if the pixel is over the threshold

    Returns
    -------
    np.ndarray
        A binary image with the pixels of the map that match the given function.
        (255 for White, 0 for Black)

    See Also
    --------
    ``find_red_pixels`` : Finds the red pixels of the map, uses this function.
    ``find_cyan_pixels`` : Finds the cyan pixels of the map, uses this function.
    """
    width, height, _ = map.shape
    im = np.zeros((width, height), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            r, g, b, _ = map[x, y]
            if fn(r, g, b):
                im[x, y] = 255

    return im


def find_red_pixels(map_filename: str, upper_threshold: int = 100, lower_threshold: int = 50) -> npt.NDArray[np.float16]:
    """
    Returns a binary image with the red pixels of the map in the ``map_filename`` file.

    Parameters
    ----------
    map_filename: str
        The filename of the map image
    upper_threshold: int
        The upper threshold for the red value of a pixel
    lower_threshold: int
        The lower threshold for the green and blue values of a pixel

    Returns
    -------
    np.ndarray
        A binary image with the red pixels of the map.

    See Also
    --------
    ``__find_pixel`` : Finds the pixels of the map that match the given function, used by this function.
    ``find_cyan_pixels`` : Finds the cyan pixels of the map
    """

    map = imread(map_filename)
    im = __find_pixel(map, lambda r, g, b:
                      r > upper_threshold
                      and g < lower_threshold
                      and b < lower_threshold)

    imsave("map-red-pixels.jpg", im)
    return im


def find_red_pixels_interface() -> None:
    """
    Interface for the ``find_red_pixels`` function.

    See Also
    --------
    ``find_red_pixels`` : Finds the red pixels of the map
    """
    print("\nPress enter to use default values (data/map.png, 100, 50)\n")

    map_filename = input("Map path (data/map.png): ")
    if map_filename == "":
        map_filename = "data/map.png"

    while True:
        try:
            upper_threshold_s = input("Upper threshold for red pixels (100): ")
            upper_threshold = 100 if upper_threshold_s == "" else int(
                upper_threshold_s)

            lower_threshold_s = input(
                "Lower threshold for green and blue pixels (50): ")
            lower_threshold = 50 if lower_threshold_s == "" else int(
                lower_threshold_s)

            if upper_threshold >= 0 or upper_threshold <= 255 or lower_threshold >= 0 or lower_threshold < 255:
                break

            print("\nInvalid threshold values, must be between 0 and 255 (inclusive).")
        except ValueError:
            print("\nInvalid threshold values, must be integers.")

    im = find_red_pixels(map_filename, upper_threshold, lower_threshold)
    print("Red Pixels Found. Saved as map-red-pixels.jpg")

    return im


def find_cyan_pixels(map_filename: str, upper_threshold: int = 100, lower_threshold: int = 50) -> npt.NDArray[np.float16]:
    """
    Returns a binary image with the cyan pixels of the map in the ``map_filename`` file.

    Parameters
    ----------
    map_filename: str
        The filename of the map image
    upper_threshold: int
        The upper threshold for the green and blue values of a pixel
    lower_threshold: int
        The lower threshold for the red value of a pixel

    Returns
    -------
    np.ndarray
        A binary image with the cyan pixels of the map.

    See Also
    --------
    ``__find_pixel`` : Finds the pixels of the map that match the given function, used by this function.
    ``find_red_pixels`` : Finds the red pixels of the map
    """

    map = imread(map_filename)
    im = __find_pixel(map, lambda r, g, b:
                      r < lower_threshold
                      and g > upper_threshold
                      and b > upper_threshold)

    imsave("map-cyan-pixels.jpg", im)
    return im


def find_cyan_pixels_interface() -> None:
    """
    Interface for the ``find_cyan_pixels`` function.

    See Also
    --------
    ``find_cyan_pixels`` : Finds the cyan pixels of the map
    """
    print("\nPress enter to use default values (data/map.png, 100, 50)\n")

    map_filename = input("Map path (data/map.png): ")
    if map_filename == "":
        map_filename = "data/map.png"

    while True:
        try:
            upper_threshold_s = input(
                "Upper threshold for green and blue pixels (100): ")
            upper_threshold = 100 if upper_threshold_s == "" else int(
                upper_threshold_s)

            lower_threshold_s = input(
                "Lower threshold for red pixels (50): ")
            lower_threshold = 50 if lower_threshold_s == "" else int(
                lower_threshold_s)

            if upper_threshold >= 0 or upper_threshold <= 255 or lower_threshold >= 0 or lower_threshold < 255:
                break

            print("\nInvalid threshold values, must be between 0 and 255 (inclusive).")
        except ValueError:
            print("\nInvalid threshold values, must be integers.")

    im = find_cyan_pixels(map_filename, upper_threshold, lower_threshold)
    print("Red Pixels Found. Saved as map-red-pixels.jpg")

    return im


def detect_connected_components(IMG: npt.NDArray[np.uint]) -> npt.NDArray[np.uint8]:
    """
    Detects the connected components of the given image, ``IMG``.
    Saves data about the connected components to the file ``cc-output-2a.txt``.

    Parameters
    ----------
    IMG: np.ndarray
        The image to detect the connected components of.

    Returns
    -------
    np.ndarray
        The image with the connected components marked with different colors.

    See Also
    --------
    ``utils.NDQueue`` : The queue used to implement the algorithm. (Uses np.ndarray as the underlying data structure.)
    ``find_red_pixels`` : Finds the red pixels of the map, returns a binary image (``IMG``).
    ``find_cyan_pixels`` : Finds the cyan pixels of the map, returns a binary image (``IMG``).
    """

    f_2a = open("cc-output-2a.txt", "w")

    marked = np.zeros(IMG.shape, dtype=np.uint8)
    queue = utils.NDQueue(initial_size=32, dtype="2u2")

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
            f_2a.write(
                f"Connected Component {component_n}, number of pixels = {pixels_n}\n")

    f_2a.write(f"Total number of connected components = {component_n}\n")
    f_2a.close()

    return marked


# I think it would be better to return the equivalent of ``component_pixels`` instead of the marked image from detect_connected_components.
# This way we wouldn't have to run essentially the same algorithm twice.
# Or just combine both functions into one, if they were only ever used together.

def detect_connected_components_sorted(MARK: npt.NDArray[np.uint8]) -> None:
    """
    Sorts the connected components of the given marked array, ``MARK``, by size.

    Parameters
    ----------
    MARK: np.ndarray
        The marked array to sort the connected components of.

    See Also
    --------
    ``utils.quick_sort`` : The sorting algorithm used to sort the connected components.
    ``detect_connected_components`` : Detects the connected components of the given image, ``IMG``, returns a marked image (``MARK``).
    """

    print("A")
    print(MARK)

    marked = np.zeros(MARK.shape, dtype=np.uint8)
    queue = utils.NDQueue(initial_size=32, dtype="2u2")

    component_pixels = []

    print(MARK.shape, np.ndindex(MARK.shape))

    component_n = 0
    for p_x, p_y in np.ndindex(MARK.shape):
        if MARK[p_x, p_y] == 1 and marked[p_x, p_y] == 0:
            marked[p_x, p_y] = 1
            queue.enqueue((p_x, p_y))

            pixels_n = 0
            component_n += 1

            while not queue.is_empty():
                pixels_n += 1
                q_m, q_n = queue.dequeue()
                for n_s in range(q_m - 1, q_m + 2):
                    for n_t in range(q_n - 1, q_n + 2):
                        if (n_s == q_m and n_t == q_n) or n_s < 0 or n_s >= MARK.shape[0] or n_t < 0 or n_t >= MARK.shape[1]:
                            continue
                        if MARK[n_s, n_t] == 1 and marked[n_s, n_t] == 0:
                            marked[n_s, n_t] = 1
                            queue.enqueue((n_s, n_t))

            component_pixels.append([component_n, pixels_n])

    f_2b = open("cc-output-2b.txt", "w")

    print("B")
    print(component_pixels)

    # I'm using quick sort because it's been reliable and fast.
    # Merge sort would have been as good but I needed more practice with quick sort.

    component_pixels = np.array(component_pixels)

    print("B")
    print(component_pixels)

    def at(i):
        return component_pixels[i][1]

    def swap(i, j):
        component_pixels[[i, j]] = component_pixels[[j, i]]

    utils.quick_sort(at, swap, 0, len(component_pixels) - 1)

    for n, p in component_pixels:
        f_2b.write(f"Connected Component {n}, number of pixels = {p}\n")

    f_2b.write(f"Total number of connected components = {component_n}\n")
    f_2b.close()


def detect_connected_components_interface() -> None:
    """
    Interface for the ``detect_connected_components`` and ``detect_connected_components_sorted`` functions.
    """

    sel = utils.menu("Red or Cyan Pixels", [
        ("R", "Red Pixels")
        ("C", "Cyan Pixels")
    ])
    if sel == "R":
        im = find_red_pixels_interface()
    else:
        im = find_cyan_pixels_interface()

    print("\nDetecting Connected Components...")
    mark = detect_connected_components(im)
    print("\nConnected Components Detected. Saved as cc-output-2a.txt")

    sel = utils.menu("Sort Components?", [
        ("Y", "Yes"),
        ("N", "No")
    ])

    if sel == "N":
        return

    detect_connected_components_sorted(mark)
    print("Connected Components Detected and Sorted. Saved as cc-output-2b.txt")
