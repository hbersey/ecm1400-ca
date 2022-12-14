from skimage.io import imread, imsave
import numpy.typing as npt
import numpy as np

def find_red_pixels(map_filename, upper_threshold=100, lower_threshold=50):
    """Your documentation goes here"""
    map: npt.NDArray = imread(map_filename)
    width, height, _ = map.shape
    im = np.zeros((width, height))

    for y in range(height):
        for x in range(width): 
            r, g, b, _ = map[x,y]
            if r > upper_threshold and g < lower_threshold and b < lower_threshold:
                im[x, y] = 1

    imsave("map-red-pixels.jpg", im)


def find_cyan_pixels(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here


def detect_connected_components(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

